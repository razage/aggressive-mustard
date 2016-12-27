require([
  "jquery",
  "views/navbar"
], function($, NavbarView) {
  var navbarView = new NavbarView({'el': "ul.navbar.navbar-nav"});
  navbarView.render();
  
});
