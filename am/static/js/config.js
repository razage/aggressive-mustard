'use strict';

require.config({
    baseURL: "js",

    shim: {
        "bootstrap": {
            deps: ['jquery'],
            exports: "Bootstrap"
        }
    },

    paths: {
        "underscore": "../bower_components/underscore/underscore-min",
        "jquery": "../bower_components/jquery/dist/jquery.min",
        "bootstrap": "../bower_components/bootstrap/dist/js/bootstrap.min",
        "backbone": "../bower_components/backbone/backbone-min",
        "hbs": "../bower_components/require-handlebars-plugin/hbs",
        "backbone-forms": "../bower_components/backbone-forms/distribution.amd/backbone-forms.min",
        "bbf-bootstrap": "../bower_components/backbone-forms/distribution.amd/templates/bootstrap3"
    }
});

require([
    'jquery',
    'views/navbar'
], function($, NavbarView) {
  var navbarView = new NavbarView();
});
