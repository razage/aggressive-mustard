define([
  'backbone'
], function(Backbone) {
  var TagModel = Backbone.Model.extend({
    defaults: {
      name: "",
      category: ""
    }
  });

  return TagModel;
});
