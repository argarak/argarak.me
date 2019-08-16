// When DOM is loaded...
document.addEventListener(
  "DOMContentLoaded",
  function() {
    var updateHighlight = function() {
      var highlight = document.querySelectorAll(
        "#navigation .highlight-bar"
      )[0];
      var subdir = window.location.pathname.split("/")[1];

      var tabElement;
      var highlightColor;

      if (subdir.length === 0) {
        tabElement = document.querySelectorAll(
          "#navigation .tab-container .tab[subdir='']"
        )[0];

        highlightColor =
          tabElement.firstChild.firstChild.attributes.stroke.value;
      } else {
        tabElement = document.querySelectorAll(
          "#navigation .tab-container .tab[subdir~='" + subdir + "']"
        )[0];

        var childElements = tabElement.firstChild.children;

        for (var i in childElements) {
          if (childElements[i].attributes.fill.value !== "none") {
            highlightColor = childElements[i].attributes.fill.value;
            break;
          }
        }
      }

      highlight.style.backgroundColor = highlightColor;

      var pos = tabElement.attributes.position.value;
      highlight.style.right = 448 - pos * 64 + "px";

      router.prevSub = pos;
    };

    updateHighlight();

    if (!!(window.history && history.pushState)) {
      var tabList = document.querySelectorAll(
        "#navigation .tab-container .tab"
      );

      for (var i = 0; i < tabList.length; ++i) {
        tabList[i].addEventListener("click", function(e) {
          e.preventDefault();

          var container = document.getElementById("router-container");

          router.subdir(this.attributes.subdir.value);
          updateHighlight();
        });
      }
    }
  },
  false
);
