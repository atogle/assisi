/*global Backbone jQuery Handlebars */

var Assisi = Assisi || {};

(function(NS, $) {
  'use strict';

  NS.app = new Backbone.Marionette.Application();

  NS.app.addRegions({
    addRegion: '#request-add-region',
    listRegion: '#request-list-region'
  });

  // Handlebars support for Marionette
  Backbone.Marionette.TemplateCache.prototype.compileTemplate = function(rawTemplate) {
    return Handlebars.compile(rawTemplate);
  };

  NS.app.on('start', function() {
    NS.app.requestCollection = new NS.RequestCollection();

    NS.app.listRegion.show(new NS.RequestListView({
      collection: NS.app.requestCollection
    }));

    NS.formView = new NS.RequestAddView({
      collection: NS.app.requestCollection
    });

    NS.app.addRegion.show(NS.formView);

    NS.app.requestCollection.fetch();
  });

  // Init =====================================================================
  $(function() {
    NS.app.start();
  });
}(Assisi, jQuery));
