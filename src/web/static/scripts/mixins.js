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

      this.autocomplete = new google.maps.places.Autocomplete(
        this.ui.address.get(0), {
          componentRestrictions: {country: 'us'},
          types: ['geocode'],
          bounds: new google.maps.LatLngBounds(
            new google.maps.LatLng(39.628961, -77.167969),
            new google.maps.LatLng(40.492915, -74.605408)
          )
        });

      // don't submit the form on autocomplete select with the enter key
      google.maps.event.addDomListener(this.ui.address.get(0), 'keydown', function(evt) {
        if (evt.keyCode === 13) {
          evt.preventDefault();
        }
      });

      // Populate all of the address fields on successful geocode
      google.maps.event.addListener(this.autocomplete, 'place_changed', function() {
        var place = self.autocomplete.getPlace(),
            addressComponents = _.object(_.map(place.address_components, function(obj) {
                return [obj.types[0], {long_name: obj.long_name, short_name: obj.short_name}];
            })),
            street_number = addressComponents.street_number ? addressComponents.street_number.long_name : '',
            street = addressComponents.route ? addressComponents.route.long_name : '',
            city = addressComponents.locality.long_name,
            state = addressComponents.administrative_area_level_1.short_name,
            zip = addressComponents.postal_code.long_name,
            address = street_number && street ? street_number + ' ' + street : '',
            dupe;

        // blur the address field, focus on apartment
        self.ui.apt.focus();

        // prefill all the address components
        self.ui.address.val(address);
        self.ui.city.val(city);
        self.ui.state.val(state);
        self.ui.zip.val(zip);
      });
    }
  };

}(Assisi, jQuery));
