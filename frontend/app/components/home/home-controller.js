function HomeController() {
  var that = this;
  that.foo = "Foo!";
  console.log(that); // should print out the controller object
}

angular.module("Home")
  .controller("HomeController", [
    HomeController
  ]);
