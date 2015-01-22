/*global Backbone jQuery Handlebars */

var Assisi = Assisi || {};

(function(NS, $) {
  'use strict';

  NS.app = new Backbone.Marionette.Application();

  NS.app.addRegions({
    mainRegion: '#main'
  });

  NS.app.addInitializer(function() {
    // Handlebars support for Marionette
    Backbone.Marionette.TemplateCache.prototype.compileTemplate = function(rawTemplate) {
      return Handlebars.compile(rawTemplate);
    };

    NS.app.requestCollection = new NS.RequestCollection();

    NS.view = new NS.RequestListView({
      collection: NS.app.requestCollection
    });

    NS.app.mainRegion.show(NS.view);

    NS.app.requestCollection.fetch();
  });

  // Init =====================================================================
  $(function() {
    NS.app.start();
  });
}(Assisi, jQuery));
