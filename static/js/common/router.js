class Router {
  constructor() {
    this.httpRequest = new XMLHttpRequest();
  }

  renderHTML(response) {
    var routeHTML = response.getElementById("router-container").innerHTML;
    document.getElementById("router-container").innerHTML = routeHTML;
  }

  go(url) {
    if (!this.httpRequest) return false;

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
    this.go("/" + dir);
  }
}

var router = new Router();
