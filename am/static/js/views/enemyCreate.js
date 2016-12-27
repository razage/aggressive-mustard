define([
  'jquery',
  'backbone',
  'collections/tagList',
  'models/enemy',
  'hbs!templates/enemies/createEnemy',
  'bootstrap',
  'validate'
], function($, Backbone, TagList, EnemyModel, CreateEnemyTemplate) {
  var EnemyCreateView = Backbone.View.extend({
    el: ".form-lightbox",

    events: {
      "submit #createEnemyForm": "createEnemy"
    },

    initialize: function() {
      console.log("EnemyCreateView loaded.");
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
    },

    createEnemy: function(e) {
      e.preventDefault();
      $(e.currentTarget).validate({
        rules: {
          eName: {
            required: true,
            rangelength: [4, 32]
          },
          rank: {
            required: true,
            digits: true
          },
          strength: {
            required: true,
            digits: true
          },
          evasion: {
            required: true,
            digits: true
          },
          health: {
            required: true,
            digits: true
          },
          dexterity: {
            required: true,
            digits: true
          },
          resistance: {
            required: true,
            digits: true
          },
          initiative: {
            required: true,
            digits: true
          },
          power: {
            required: true,
            digits: true
          },
          physDef: {
            required: true,
            digits: true
          },
          speed: {
            required: true,
            digits: true
          },
          intelligence: {
            required: true,
            digits: true
          },
          magDef: {
            required: true,
            digits: true
          },
          idDiff: {
            required: true,
            digits: true
          },
          hateMulti: {
            required: true,
            digits: true
          }
        },
        submitHandler: function(form) {
          form.submit();
        },
        invalidHandler: function(e, validator) {
          console.log(validator.numberOfInvalids());
        }
      });
    }
  });

  return EnemyCreateView;
});
