class Router {
  constructor() {
    this.httpRequest = new XMLHttpRequest();
    this.prevSub = 0;
    this.direction = "";
    this.stateName = "";
  }

  animationEndRemoveClass(e) {
    e.target.className = "";
  }

  animationEndRemove(e) {
    e.target.outerHTML = "";

    slide.animate();
  }

  renderHTML(response) {
    var container = document.getElementById("router-container");
    var routeContainer = response.getElementById("router-container");

    var routeLink = response.querySelector("link[rel*='icon']");
    var link = document.querySelector("link[rel*='icon']");

    link.type = "image/x-icon";
    link.rel = "shortcut icon";

    link.href = routeLink.href;

    var routeTitle = response.querySelector("title");
    var title = document.querySelector("title");

    title.innerHTML = routeTitle.innerHTML;

    routeContainer.addEventListener(
      "animationend",
      this.animationEndRemoveClass,
      false
    );

    container.addEventListener("animationend", this.animationEndRemove, false);

    switch (this.direction) {
      case "left":
        routeContainer.classList.add("router-move-in-left");
        document.getElementById("app").insertBefore(routeContainer, container);
        container.classList.add("router-move-out-right");
        break;
      case "right":
        routeContainer.classList.add("router-move-in-right");
        document.getElementById("app").insertBefore(routeContainer, container);
        container.classList.add("router-move-out-left");
        break;
      case "down":
        break;
      case "up":
        break;
      default:
        console.error(
          "router: direction not defined, actual value: '" +
            this.direction +
            "'"
        );
        break;
    }

    let routerComplete = new CustomEvent("routerComplete", {
      detail: this.stateName
    });

    window.dispatchEvent(routerComplete);
  }

  go(url) {
    if (!this.httpRequest) return false;

    history.pushState({}, "", url);

    this.httpRequest.onreadystatechange = () => {
      if (this.httpRequest.readyState === XMLHttpRequest.DONE) {
        if (this.httpRequest.status === 200) {
          this.renderHTML(this.httpRequest.responseXML);
        } else {
          console.error(
            "Error " +
              this.httpRequest.status +
              ": there was an error routing to the specified location."
          );
        }
      }
    };
    this.httpRequest.open("GET", url);
    this.httpRequest.responseType = "document";
    this.httpRequest.send();

    return true;
  }

  subdir(dir) {
    var tabElement;

    if (dir === "") {
      tabElement = document.querySelectorAll(
        "#navigation .tab-container .tab[subdir='']"
      )[0];
    } else {
      tabElement = document.querySelectorAll(
        "#navigation .tab-container .tab[subdir~='" + dir + "']"
      )[0];
    }

    var currSub = tabElement.attributes.position.value;

    if (currSub === this.prevSub) return;

    if (currSub > this.prevSub) {
      this.direction = "right";
    } else {
      this.direction = "left";
    }

    this.stateName = dir;
    this.prevSub = currSub;
    this.go("/" + dir);
  }
}

document.addEventListener("DOMContentLoaded", function(event) {
  let path = window.location.pathname.split("/");
  let currState = "";

  if (path.length > 1) {
    currState = path[1];
  }

  let routerComplete = new CustomEvent("routerComplete", {detail: currState});
  window.dispatchEvent(routerComplete);
});

var router = new Router();
