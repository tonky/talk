angular.module('talk', ['api']).
  config(function($routeProvider) {
    $routeProvider.
      when('/', {controller:ListCtrl, templateUrl:'static/ng/list.html'}).
      otherwise({redirectTo:'/'});
  });
 
 
function ListCtrl($scope, Post) {
  $scope.posts = Post.query();
}
