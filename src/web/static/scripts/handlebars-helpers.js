/*global Backbone jQuery Handlebars _ */

var Assisi = Assisi || {};

(function(NS, $) {
  'use strict';

  Handlebars.registerHelper('each_distribution_site', function() {
    var result = '',
        args = Array.prototype.slice.call(arguments),
        orderedSites = _.sortBy(NS.Config.distribution_sites, function(p) {
          return p.name;
        }),
        options;

    options = args.slice(-1)[0];

    _.each(orderedSites, function(p, i) {
      result += options.fn(p);
    }, this);

    return result;
  });

  Handlebars.registerHelper('select', function(value, options) {
    var $el = $('<div/>').html(options.fn(this)),
      selectValue = function(v) {
        $el.find('[value="'+v+'"]').attr({
          checked: 'checked',
          selected: 'selected'
        });
      };

    if (_.isArray(value)) {
      _.each(value, selectValue);
    } else {
      selectValue(value);
    }

    return $el.html();
  });


}(Assisi, jQuery));
