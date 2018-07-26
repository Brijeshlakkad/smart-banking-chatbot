<?php include_once("header.php"); ?>
<?php check_session(); ?>
<div class="container-fluid my_well">
	<div class="row" align="center">
		<form ng-app="myapp" ng-controller="BrijController" name="feedback"  novalidate>
		<table class="myTable">
			<div class="form-group">
			<tr> 
			<td><label for="s_email">Email:</label><br></td>
			<td><input type="email" class="form-control" name="s_email" placeholder="Enter Email" ng-model="s_email" ng-style="emailStyle" ng-change="analyze(s_email)" required></td>
			<td>
			<span style="color:red" id="s_email" ng-show="feedback.s_email.$dirty && feedback.s_email.$invalid">
			<span ng-show="feedback.s_email.$error.required">Email is required</span>
			<span ng-show="!feedback.s_email.$error.required && feedback.s_email.$error.email">Invalid email</span>
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr> 
			<td><label for="f_text">Feedback:</label><br></td>
			<td><textarea class="form-control" name="f_text" placeholder="Enter feedback here...." ng-model="f_text" cols="40" rows="10" required></textarea></td>
			<td>
			<span style="color:red" id="f_text" ng-show="feedback.f_text.$dirty && feedback.f_text.$invalid">
			<span ng-show="feedback.f_text.$error.required">Enter characters less than 50</span>
			</span>
			</td>
			</tr>
			</div>
			<tr>
			<td><input type="submit" id="submit_btn" value="Submit" class="btn btn-primary" ng-disabled="feedback.s_email.$invalid || feedback.f_text.$invalid" /></td>
			<td></td>
			</tr>
		</table>
		</form>
	</div>
</div>
<script>
var myApp = angular.module("myapp", []);
	myApp.controller("BrijController", function($scope,$http) {
		$scope.emailStyle = {
					"border-width":"1.45px"
         };
		$scope.analyze = function(value) {
					var patt_email=new RegExp("^[a-z0-9._]+@[a-z]+\.[a-z.]{2,5}$");
                    if(patt_email.test(value)) {
                   		$scope.emailStyle["border-color"] = "green";
                    } 
					else {
                        $scope.emailStyle["border-color"] = "red";
                    }
                };
	});
</script>
<?php include_once("footer.php"); ?>