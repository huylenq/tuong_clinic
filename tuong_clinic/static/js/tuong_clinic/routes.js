var app = angular.module('opal');
app.controller('WelcomeCtrl', function(){});

console.log("Route setup");

app.config(
    ['$routeProvider',
     function($routeProvider){
	 $routeProvider.when('/',  {redirectTo: '/list'})
     }]);

