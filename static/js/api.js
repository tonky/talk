angular.module('api', ['ngResource']).
    factory('Post', function($resource) {
      var Post = $resource('/api/posts/:id');
 
      return Post;
    });
