/*global Backbone */

var Assisi = Assisi || {};

(function(NS) {
  'use strict';

  NS.RequestView = Backbone.Marionette.ItemView.extend({
    template: '#request-item-tpl',
    tagName: 'tr',
    className: 'request-item'
  });

  NS.RequestListView = Backbone.Marionette.CompositeView.extend({
    template: '#request-list-tpl',
    childView: NS.RequestView,
    childViewContainer: '.request-list'
  });

}(Assisi));