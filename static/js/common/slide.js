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

      console.log(bounds);

      slideEl.style.width = bounds.width + "px";
      slideEl.style.height = bounds.height + "px";
      slideEl.style.top = bounds.top + "px";
      slideEl.style.left = bounds.left - 5 + "px";

      console.log(slideEl);
      document.body.appendChild(slideEl);

      this.el[i].style.visibility = "visible";
    }

    var newEl = document.querySelectorAll(".slide-overlay");

    for (i = 0; i < newEl.length; i++) {
      console.log(newEl[i]);
      window.getComputedStyle(newEl[i]).width;

      newEl[i].style.width = "0px";
    }

    return true;
  }
}

var slide = new SlideTransition();

document.addEventListener("DOMContentLoaded", function(event) {
  slide.animate();
});
