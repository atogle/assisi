/*global Backbone _ */

var Assisi = Assisi || {};

(function(NS) {
  NS.RequestModel = Backbone.Model.extend({
    url: function() {
      var origUrl = Backbone.Model.prototype.url.call(this);
      return origUrl + (origUrl.charAt(origUrl.length - 1) === '/' ? '' : '/');
    }
  });

  NS.RequestCollection = Backbone.Collection.extend({
    model: NS.RequestModel,
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
