/*global Backbone jQuery Handlebars _ */

var Assisi = Assisi || {};

(function(NS, $) {
  'use strict';

  // Handlebars support for Marionette
  Backbone.Marionette.TemplateCache.prototype.compileTemplate = function(rawTemplate) {
    return Handlebars.compile(rawTemplate);
  };

  NS.app = new Backbone.Marionette.Application();

  NS.app.on('start', function() {
    NS.app.appView = new NS.AppView({
      el: 'body'
    });

    NS.app.requestCollection = new NS.RequestCollection();

    // Render the list of requests
    NS.app.appView.listRegion.show(new NS.RequestListView({
      collection: NS.app.requestCollection
    }));

    // Render the form for adding new requests
    NS.app.appView.addRegion.show(new NS.RequestAddView({
      collection: NS.app.requestCollection
    }));

    NS.app.appView.sidebarRegion.show(new NS.SidebarView());

    // Fetch all of the requests in all of the pages
    NS.app.requestCollection.fetchAllPages();

    // Listen for alerts to display
    NS.app.on('alert', function(data) {
      NS.app.appView.alertRegion.show(new NS.AlertView({
        model: new Backbone.Model(data)
      }));
    });

  });

  // Init =====================================================================
  $(function() {
    NS.app.start();
  });
}(Assisi, jQuery));
