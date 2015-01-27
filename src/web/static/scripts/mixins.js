/*global Backbone Handlebars jQuery console _ google */

var Assisi = Assisi || {};

(function(NS, $) {
  'use strict';

  NS.FormSubmitMixin = {
    selectPhoneType: function(evt) {
      evt.preventDefault();
      var type = evt.target.innerHTML;

      this.ui.phoneTypeInput.val(type);
      this.ui.phoneTypeLabel.html(type);
    },
    onSubmit: function(evt) {
      evt.preventDefault();
      var self = this,
          data = this.ui.form.serializeObject();

      if (this.model) {
        this.model.save(data, {
          success: _.bind(self.onSaveSuccess, self),
          error: _.bind(self.onSaveError, self)
        });
      } else if (this.collection) {
        this.collection.create(data, {
          success: _.bind(self.onSaveSuccess, self),
          error: _.bind(self.onSaveError, self)
        });

      }
    },
    onSaveSuccess: function(model, response, options) {
      console.log('success', arguments);
    },
    onSaveError: function(model, response, options) {
      console.log('error', arguments);
    },
    initAutocomplete: function() {
      var self = this;

      console.log('init autocomplete');
      this.autocomplete = new google.maps.places.Autocomplete(this.ui.address.get(0));

      google.maps.event.addListener(this.autocomplete, 'place_changed', function() {
        var place = self.autocomplete.getPlace();

        console.log(place);
      });
    }
  };

}(Assisi, jQuery));
