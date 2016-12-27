define([
  'jquery',
  'backbone',
  'models/tags'
], function($, Backbone, TagModel) {
  var TagList = Backbone.Collection.extend({
    url: "/tags/query",
    model: TagModel
  });

  return TagList;
});
