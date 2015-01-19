/*global Backbone */

var Assisi = Assisi || {};

(function(NS) {
  NS.RequestCollection = Backbone.Collection.extend({
    url: '/api/v1/requests/',
    parse: function(response) {
      return response.results;
    }
  });

}(Assisi));
