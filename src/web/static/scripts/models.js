/*global Backbone */

var Assisi = Assisi || {};

(function(NS) {
  NS.RequestModel = Backbone.Collection.extend({
    url: '/api/v1/requests/'
  });


}(Assisi));
