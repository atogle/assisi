/*global Backbone Handlebars jQuery _ google */

var Assisi = Assisi || {};

(function(NS, $) {
  'use strict';

  NS.AppView = Backbone.Marionette.LayoutView.extend({
    regions: {
      alertRegion: '#alert-region',
      addRegion: '#request-add-region',
      listRegion: '#request-list-region'
    }
  });

  NS.AlertView = Backbone.Marionette.ItemView.extend({
    template: '#alert-tpl',
    className: 'alert-container',
    onShow: function() {
      var $el = this.$el;

      _.defer(function() {
        $el.addClass('show');
      });

      _.delay(function() {
        $el.removeClass('show');
      }, 4000);
    }
  });

  NS.RequestAddView = Backbone.Marionette.ItemView.extend(
  _.extend({}, NS.FormSubmitMixin, {
    template: '#request-item-add-form-tpl',
    ui: {
      form: 'form',
      phoneTypeLink: '.phone-type-link',
      phoneTypeInput: '[name="phone_type"]',
      phoneTypeLabel: '.phone-type-label',
      apt: '[name="apt"]',
      address: '[name="address"]',
      city: '[name="city"]',
      state: '[name="state"]',
      zip: '[name="zip"]'
    },
    events: {
      'submit @ui.form': 'onSubmit',
      'click @ui.phoneTypeLink': 'selectPhoneType',
      'blur @ui.address': 'onAddressBlur'
    },
    onSaveSuccess: function(model, response, options) {
      this.ui.form.get(0).reset();

      var msg = '<strong>REQUEST SAVED.</strong> ' + model.get('name') + ', ' +
        model.get('address') + ', ' + model.get('zip');

      NS.app.trigger('alert', {type: 'success', message: msg});
    },
    onRender: function(evt) {
      if (!this.autocomplete) {
        this.initAutocomplete();
      }
    }
  }));

  NS.RequestFormView = Backbone.Marionette.ItemView.extend(
  _.extend({}, NS.FormSubmitMixin, {
    template: '#request-item-form-tpl',
    ui: {
      editToggle: '.edit-toggle',
      form: 'form',
      phoneTypeLink: '.phone-type-link',
      phoneTypeInput: '[name="phone_type"]',
      phoneTypeLabel: '.phone-type-label',
      apt: '[name="apt"]',
      address: '[name="address"]',
      city: '[name="city"]',
      state: '[name="state"]',
      zip: '[name="zip"]'
    },
    events: {
      'click @ui.editToggle': 'onEditToggleClick',
      'submit @ui.form': 'onSubmit',
      'click @ui.phoneTypeLink': 'selectPhoneType',
      'blur @ui.address': 'onAddressBlur'
    },
    initialize: function(options) {
      this.containerView = options.containerView;
    },
    onEditToggleClick: function(evt) {
      evt.preventDefault();
      this.containerView.toggleEditing();
    },
    onSaveSuccess: function(model, response, options) {
      var msg = '<strong>REQUEST SAVED.</strong> ' + model.get('name') + ', ' +
        model.get('address') + ', ' + model.get('zip');

      this.containerView.toggleEditing();
      NS.app.trigger('alert', {type: 'success', message: msg});
    },
    onRender: function(evt) {
      if (!this.autocomplete) {
        this.initAutocomplete();
      }
    }
  }));

  NS.RequestItemView = Backbone.Marionette.ItemView.extend({
    template: '#request-item-tpl',
    className: 'panel-body request-item',
    ui: {
      editToggle: '.edit-toggle',
      deleteButton: '.delete-button'
    },
    events: {
      'click @ui.editToggle': 'onEditToggleClick',
      'click @ui.deleteButton': 'onDelete'
    },
    initialize: function(options) {
      this.containerView = options.containerView;
    },
    onEditToggleClick: function(evt) {
      evt.preventDefault();
      this.containerView.toggleEditing();
    },
    onDelete: function(evt) {
      evt.preventDefault();
      if (window.confirm('Really delete this request? This cannot be undone.')) {
        this.model.destroy({
          wait: true,
          success: function(model, response, options) {},
          error: function(model, response, options) {}
        });
      }
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

}(Assisi, jQuery));
