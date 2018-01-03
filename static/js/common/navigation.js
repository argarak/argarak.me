// When DOM is loaded...
document.addEventListener(
  "DOMContentLoaded",
  function() {
    var highlight = document.querySelectorAll("#navigation .highlight-bar")[0];
    var subdir = window.location.pathname.split("/")[1];

    var tabElement;
    var highlightColor;

    if (subdir.length === 0) {
      tabElement = document.querySelectorAll(
        "#navigation .tab-container .tab[subdir='']"
      )[0];

      highlightColor = tabElement.firstChild.firstChild.attributes.stroke.value;
    } else {
      tabElement = document.querySelectorAll(
        "#navigation .tab-container .tab[subdir~='" + subdir + "']"
      )[0];

      highlightColor = tabElement.firstChild.firstChild.attributes.fill.value;
    }

    highlight.style.backgroundColor = highlightColor;

    var tabRect = tabElement.getBoundingClientRect();

    console.log(tabRect);

    highlight.style.right = tabRect.right + "px";
    highlight.style.left = tabRect.left + "px";
    highlight.style.width = tabRect.width + "px";

    console.log(highlightColor);
  },
  false
);
