/*global Backbone Handlebars jQuery console _ google Gatekeeper */

var Assisi = Assisi || {};

(function(NS, $) {
  'use strict';

  NS.FormSubmitMixin = {
    selectPhoneType: function(evt) {
      evt.preventDefault();
      var type = evt.currentTarget.innerHTML,
          $parent = $(evt.currentTarget).parents('.input-group'),
          $input = $parent.find('.phone_type'),
          $label = $parent.find('.phone-type-label');

      $input.val(type);
      $label.html(type);
    },
    onAddressBlur: function(evt) {
      evt.preventDefault();
      this.ui.address.get(0).setCustomValidity('');
    },
    onZipBlur: function(evt) {
      evt.preventDefault();
      this.ui.zip.get(0).setCustomValidity('');
    },
    onDistSiteBlur: function(evt) {
      evt.preventDefault();
      this.ui.dist_site.get(0).setCustomValidity('');
    },
    onZipChange: function(evt) {
      evt.preventDefault();
      var zip = this.ui.zip.val(),
          collection = this.collection || this.model.collection,
          // how many requests have been made for each site
          distSiteCounts = collection.groupBy(function(model) {
            return model.get('distribution_site');
          }),
          // get the first available dist site
          distSiteConfig = _.find(NS.Config.distribution_sites, function(config) {
            // if zip matches and the max has not been exceeded
            if (_.contains(config.zip_codes, zip) && (!distSiteCounts[config.name] ||
              config.max > distSiteCounts[config.name].length)) {
              return config;
            }
          });

      if (distSiteConfig) {
        this.ui.dist_site.val(distSiteConfig.name);
      }
    },
    onSubmit: Gatekeeper.onValidSubmit(function(evt) {
      evt.preventDefault();
      var self = this,
          data = this.ui.form.serializeObject(),
          collection = this.collection || this.model.collection,
          model = this.model ? this.model.set(data) : new Backbone.Model(data),
          dupes = collection.getDupes(model),
          validZips = _.uniq(_.flatten(_.pluck(NS.Config.distribution_sites, 'zip_codes'))),
          zip = this.ui.zip.val(),
          distSiteName = this.ui.dist_site.val(),
          distSiteConfig = _.findWhere(NS.Config.distribution_sites, {'name': distSiteName});

      this.ui.address.get(0).setCustomValidity('');
      this.ui.zip.get(0).setCustomValidity('');
      this.ui.dist_site.get(0).setCustomValidity('');

      if (dupes.length > 0) {
        this.ui.address.get(0).setCustomValidity(
          'Someone has already made a request for this address (address, apt, and zip).');
        model.set(model.previousAttributes());
        this.ui.form.submit();
        return;
      }

      // if the zip code is out of range
      if (_.contains(validZips, zip) === false) {
        this.ui.zip.get(0).setCustomValidity('We are not delivering to this zip code.');
        model.set(model.previousAttributes());
        this.ui.form.submit();
        return;
      }

      // if zip code and distribution site don't match
      if (_.contains(distSiteConfig.zip_codes, zip) === false) {
        this.ui.dist_site.get(0).setCustomValidity(distSiteName + ' does not deliver to zip code ' + zip);
        model.set(model.previousAttributes());
        this.ui.form.submit();
        return;
      }

      if (this.model) {
        this.model.save(data, {
          success: _.bind(self.onSaveSuccess, self),
          error: _.bind(self.onSaveError, self)
        });
      } else if (this.collection) {
        this.collection.create(data, {
          wait: true,
          success: _.bind(self.onSaveSuccess, self),
          error: _.bind(self.onSaveError, self)
        });
      }
    }),
    onSaveSuccess: function(model, response, options) {
      var msg = '<strong>REQUEST SAVED.</strong> ' + model.get('name') + ', ' +
        model.get('address') + ', ' + model.get('zip');

      NS.app.trigger('alert', {type: 'success', message: msg});
    },
    onSaveError: function(model, response, options) {
      var msg = '<strong>UNABLE TO SAVE.</strong>';

      try {
        if (response.responseJSON) {
          msg = msg + _.map(response.responseJSON, function(errors, name) {
            return ' <em>'+ name +'</em>: ' + errors.join(', ');
          });
        } else {
          msg = msg + ' Cannot reach the server. Check your internet connection.';
        }
      } catch(err) {
        console.log(err);
      }

      NS.app.trigger('alert', {type: 'danger', message: msg});
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

        // prefill all the address components and trigger change
        self.ui.address.val(address).change();
        self.ui.city.val(city).change();
        self.ui.state.val(state).change();
        self.ui.zip.val(zip).change();
      });
    }
  };

}(Assisi, jQuery));
