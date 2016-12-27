define([
  'jquery',
  'backbone'
], function($, Backbone) {
  var EnemyModel = Backbone.Model.extend({
    url: "/enemies"
  });

  return EnemyModel;
});
