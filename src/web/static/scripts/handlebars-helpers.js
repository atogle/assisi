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

  Handlebars.registerHelper('distribution_site_meal_count', function(collectionArray, siteName, options) {
    var mealsBySite = _.groupBy(collectionArray, 'distribution_site'),
        siteMeals = mealsBySite[siteName];
    return siteMeals ? siteMeals.length : 0;
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


  Handlebars.registerHelper('download_url_root', function() {
    return NS.Config.download_url_root;
  });



}(Assisi, jQuery));
