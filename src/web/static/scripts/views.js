/*global Backbone, Handlebars */

var Assisi = Assisi || {};

(function(NS) {
  'use strict';

  NS.RequestFormView = Backbone.Marionette.ItemView.extend({
    template: '#request-item-form-tpl',
    ui: {
      editToggle: '.edit-toggle'
    },
    events: {
      'click @ui.editToggle': 'onEditToggleClick'
    },
    initialize: function(options) {
      this.containerView = options.containerView;
    },
    onEditToggleClick: function(evt) {
      evt.preventDefault();
      this.containerView.toggleEditing();
    }

  });

  NS.RequestItemView = Backbone.Marionette.ItemView.extend({
    template: '#request-item-tpl',
    ui: {
      editToggle: '.edit-toggle'
    },
    events: {
      'click @ui.editToggle': 'onEditToggleClick'
    },
    initialize: function(options) {
      this.containerView = options.containerView;
    },
    onEditToggleClick: function(evt) {
      evt.preventDefault();
      this.containerView.toggleEditing();
    }
  });

  NS.RequestToggleView = Backbone.Marionette.LayoutView.extend({
    template: '#request-layout-tpl',
    className: 'request-item panel panel-default',
    regions: {
      toggleRegion: '.toggle-region'
    },
    onRender: function(view) {
      var View = NS.RequestItemView;
      if (view.editing) {
        View = NS.RequestFormView;
      }

      view.getRegion('toggleRegion').show(new View({
        model: this.model,
        containerView: view
      }));
    },
    toggleEditing: function() {
      this.editing = !this.editing;
      this.render();
    }
  });

  NS.RequestListView = Backbone.Marionette.CompositeView.extend({
    template: '#request-list-tpl',
    childView: NS.RequestToggleView,
    childViewContainer: '.request-list'
  });

}(Assisi));
