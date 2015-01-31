/*global Backbone _ */

var Assisi = Assisi || {};

(function(NS) {
  NS.PaginatedCollection = Backbone.Collection.extend({
    resultsAttr: 'results',

    // parse: function(response) {
    //   this.metadata = response.metadata;
    //   return response[this.resultsAttr];
    // },

    fetchNextPage: function(success, error) {
      var collection = this;

      if (this.next) {
        collection.fetch({
          remove: false,
          url: collection.next,
          success: success,
          error: error
        });
      }
    },

    fetchAllPages: function(options) {
      var self = this,
          onFirstPageSuccess, onPageComplete,
          onPageSuccess, onPageError,
          onAllSuccess, onAnyError,
          attemptedPages = 0, totalPages = 1;

      options = options || {};
      options.data = options.data || {};

      if (options.error) {
        onAnyError = _.once(options.error);
      }

      onFirstPageSuccess = function(obj, data) {
        // Calculate the total number of pages based on the size of the rist
        // page, assuming all pages except the last will be the same size.
        var pageSize = data[self.resultsAttr].length, i;
        totalPages = Math.ceil(data.count / pageSize);

        if (options.success) {
          onAllSuccess = _.after(totalPages, options.success);
        }

        // Fetch all the rest of the pages in parallel.
        if (data.next) {
          for (i = 2; i <= totalPages; i++) {
            self.fetch(_.defaults({
              remove: false,
              data: _.defaults({ page: i }, options.data),
              complete: onPageComplete,
              success: onPageSuccess,
              error: onPageError
            }, options));
          }
        }

        onPageSuccess.apply(this, arguments);
      };

      onPageComplete = function() {
        attemptedPages++;
        if (options.pageComplete) { options.pageComplete.apply(this, arguments); }
        if (attemptedPages === totalPages && options.complete) { options.complete.apply(this, arguments); }
      };

      onPageSuccess = function() {
        if (options.pageSuccess) { options.pageSuccess.apply(this, arguments); }
        if (onAllSuccess) { onAllSuccess.apply(this, arguments); }
      };

      onPageError = function() {
        if (options.pageError) { options.pageError.apply(this, arguments); }
        if (onAnyError) { onAnyError.apply(this, arguments); }
      };

      this.fetch(_.defaults({
        // Note that success gets called before complete, which is imprtant
        // because complete should know whether correct total number of pages.
        // However, if the request for the first page fails, complete will
        // assume one page.
        success: onFirstPageSuccess,
        error: onPageError,
        complete: onPageComplete
      }, options));
    }
  });


  NS.RequestCollection = NS.PaginatedCollection.extend({
    url: '/api/v1/requests/',
    parse: function(response) {
      return response.results;
    }
  });

}(Assisi));
