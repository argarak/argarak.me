class SlideTransition {
  constructor() {
    this.el = [];
  }

  animate() {
    this.el = document.querySelectorAll(".slide-entry");

    if (this.el.length === 0) return false;

    // Create a rectangle around text and slide out
    for (var i = 0; i < this.el.length; i++) {
      var slideEl = document.createElement("div");
      slideEl.setAttribute("class", "slide-overlay");

      var bounds = this.el[i].getBoundingClientRect();

      let currParent = this.el[i].parentNode;
      let color = "";

      for (;;) {
        color = window
          .getComputedStyle(currParent, null)
          .getPropertyValue("background-color");

        if (color != "rgba(0, 0, 0, 0)") {
          break;
        }

        currParent = currParent.parentNode;

        if (currParent === null) {
          console.error(
            "Could not find background colour for slide animation, aborting!",
            this.el[i]
          );
          return false;
        }
      }

      slideEl.style.backgroundColor = color;
      slideEl.style.width = bounds.width + "px";
      slideEl.style.height = bounds.height + "px";
      slideEl.style.top = bounds.top + "px";
      slideEl.style.left = bounds.left - 5 + "px";

      document.body.appendChild(slideEl);

      this.el[i].style.visibility = "visible";
    }

    var newEl = document.querySelectorAll(".slide-overlay");

    for (i = 0; i < newEl.length; i++) {
      window.getComputedStyle(newEl[i]).width;

      newEl[i].style.width = "0px";

      newEl[i].addEventListener(
        "transitionend",
        function(event) {
          event.target.outerHTML = "";
        },
        false
      );
    }

    return true;
  }
}

var slide = new SlideTransition();

window.onload = function() {
  slide.animate();
};
