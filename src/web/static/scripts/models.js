/*global Backbone _ */

var Assisi = Assisi || {};

(function(NS) {
  NS.RequestCollection = Backbone.Collection.extend({
    url: '/api/v1/requests/',
    getDupes: function(model) {
      return this.filter(function(m) {
        if (model.get('address') === m.get('address') &&
            model.get('zip') === m.get('zip') &&
            model.get('apt') === m.get('apt')) {

          if (model.id !== m.id) {
            return true;
          }
        }

        return false;
      });
    }
  });

}(Assisi));
