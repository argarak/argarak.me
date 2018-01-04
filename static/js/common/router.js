class Router {
  constructor() {
    this.httpRequest = new XMLHttpRequest();
    this.prevSub = 0;
    this.direction = "";
  }

  animationEndRemoveClass(e) {
    e.target.className = "";
  }

  animationEndRemove(e) {
    e.target.outerHTML = "";
  }

  renderHTML(response) {
    var container = document.getElementById("router-container");
    var routeContainer = response.getElementById("router-container");

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
  }

  go(url) {
    if (!this.httpRequest) return false;

    history.replaceState({}, "", url);

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
      this.direction = "left";
    } else {
      this.direction = "right";
    }

    this.prevSub = currSub;
    this.go("/" + dir);
  }
}

var router = new Router();
