define([
  'jquery',
  'backbone',
  'views/enemyCreate',
  'bootstrap',
  'backbone-forms'
], function($, Backbone, EnemyCreateView) {
  var NavbarView = Backbone.View.extend({
    el: "ul.navbar-nav",

    events: {
        "click #create_enemy": "createEnemy"
    },

    initialize: function() {
      console.log("NavbarView loaded.");
    },

    render: function() {
        console.log(this.el, this.$el);
        return this;
    },

    createEnemy: function(e) {
        e.preventDefault();
        new EnemyCreateView();
        $(".form-lightbox").slideToggle(300, function() {
          $("nav, .content").css({opacity: 0.6});
        });
    }
  });

  return NavbarView;
});
