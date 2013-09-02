angular.module('talk', []).
  config(function($routeProvider) {
    $routeProvider.
      when('/discussion', {templateUrl:'static/templates/discussion.html'}).
      when('/changelog', {templateUrl:'static/templates/changelog.html'}).
      when('/questions', {templateUrl:'static/templates/questions.html', controller:QuestionsCtrl}).
      otherwise({redirectTo:'/index'});
  });
 
 
function QuestionsCtrl($scope) {
  $scope.questions = [
    {"title": "first question", "body": "first body"},
    {"title": "second question", "body": "second body"}
  ];
}
