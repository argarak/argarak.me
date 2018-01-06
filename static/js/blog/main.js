class Blog {
  constructor() {
    this.loadingPosition = 0;
    this.loadingElement = null;
    this.pause = false;
  }

  changeArticle(pos) {
    console.log("changing article!");
  }

  updateLoading(self) {
    if (self.pause) return;

    if (self.loadingPosition >= 100) {
      self.changeArticle(1);
      self.loadingPosition = 0;
    }

    self.loadingPosition++;
    self.loadingElement.style.width = self.loadingPosition + "%";
  }

  beginBlogSequence() {
    this.loadingElement = document.querySelectorAll(
      "#blog-loading .loading-bar"
    )[0];

    if (this.loadingElement.length === 0 || this.loadingElement === null) {
      console.error("Blog initialisation error: Loading bar not found.");
      return;
    }

    window.setInterval(() => {
      this.updateLoading(this);
    }, 100);
  }
}

var blog = new Blog();
