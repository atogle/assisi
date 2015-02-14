/*global Backbone jQuery Handlebars _ */

var Assisi = Assisi || {};

(function(NS, $) {
  'use strict';

  Handlebars.registerHelper('each_partner', function() {
    var result = '',
        args = Array.prototype.slice.call(arguments),
        orderedPartners = _.sortBy(NS.Config.partners, function(p) {
          return p.name;
        }),
        options;

    options = args.slice(-1)[0];

    _.each(orderedPartners, function(p, i) {
      result += options.fn(p);
    }, this);

    return result;
  });

}(Assisi, jQuery));
