angular.module('api', ['ngResource']).
    factory('Topic', function($resource) {
      var Topic = $resource('/api/posts/:id');
 
      return Topic;
    });
