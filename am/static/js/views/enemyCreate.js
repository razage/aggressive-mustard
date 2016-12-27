define([
  'jquery',
  'backbone',
  'collections/tagList',
  'models/enemy',
  'hbs!templates/createEnemy',
  'bootstrap'
], function($, Backbone, TagList, EnemyModel, CreateEnemyTemplate) {
  var EnemyCreateView = Backbone.View.extend({
    el: ".form-lightbox",

    events: {},

    initialize: function() {
      console.log("EnemeyCreateView loaded.");
      this.render();
    },

    render: function() {
      var that = this;
      var TList = new TagList().fetch({
        data: {category: "Enemy Type"},
        success: function(collection, response, options) {
          var createEnemyTemplate = CreateEnemyTemplate({eTypes: _.flatten(response)});
          that.$el.html(createEnemyTemplate);
        }
      });
      var enemy = new EnemyModel();

    }
  });

  return EnemyCreateView;
});
