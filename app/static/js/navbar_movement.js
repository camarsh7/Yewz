function hideNav() {
  var prevScrollPos = windows.pageYOffset;
  window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollPos > currentScrollPos) {
      document.getElementById("navbar").style.top = "0";
    }
    else {
      document.getElementById("navbar").style.top ="-50px";
    }
    prevScrollPos = currentScrollPos;
    }
  }
