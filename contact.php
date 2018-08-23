<?php include_once("header.php"); ?>
<div class="container-fluid my_well">
	<div class="row" align="center">
	<div class="row"><h2>Give us feedback</h2><br/><h3>We'd like to hear from you.</h3></div><br/>
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
			<td><input type="submit" id="submit_btn" value="Submit" class="btn btn-primary" ng-disabled="feedback.s_email.$invalid || feedback.f_text.$invalid" ng-click="send_feedback()" /></td>
			<td></td>
			</tr>
		</table>
		</form>
	</div>
</div>
<div class="modal fade" id="success_modal" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>
        <div class="modal-body">
        <div class="alert alert-success">Thanks! we have received yor feedback.</div>
        </div>
      </div>
    </div>
</div>
<div class="modal fade" id="error_modal" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>
        <div class="modal-body">
        <div class="alert alert-danger">Sorry, we are facing problem. Try again after a few minutes.</div>
        </div>
      </div>
    </div>
</div>
<div class="modal fade" id="already_modal" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>
        <div class="modal-body">
        <div class="alert alert-danger">You have sent this feedback a few minutes earlier.</div>
        </div>
      </div>
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
		$scope.send_feedback=function()
		{
			var email=$scope.s_email;
			var feedback=$scope.f_text;
							$http({
								method : "POST",
								url : "customer_interface.py",
								data: "email="+email+"&feedback="+feedback,
								headers: {'Content-Type': 'application/x-www-form-urlencoded'}
							}).then(function mySuccess(response) {
								var flag=response.data;
								if(flag==111)
									{
										$("#already_modal").modal("show");
								setTimeout(function(){
									$("#already_modal").modal("hide");
								},2000);
									}
								else if(flag==11)
									{
									$("#success_modal").modal("show");
								setTimeout(function(){
									$("#success_modal").modal("hide");
								},2000);
									}
								else{
									$("#error_modal").modal("show");
								setTimeout(function(){
									$("#error_modal").modal("hide");
								},2000);
								}

							}, function myError(response) {

							});
		};
	});
</script>
<?php include_once("footer.php"); ?>
