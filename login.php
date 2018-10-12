<?php include("header.php"); ?>

<div class="container well login_block" align="center">
	<div class="row">
		<div><caption><a href="index.php"><a href="index.php"><img src="images/jonsnow.png" class="img-responsive" style="margin-top:10px;width:250px;height:60px;float:center;filter:drop-shadow(0px 0px 3px #ffffff);"/></a></caption></div>
	</div>
	<div class="row">
		<form ng-app="myapp" ng-controller="BrijController" name="myForm" method="post" novalidate>
		<div class="row" style="padding-top: 20px;"><div class="col-md-offset-4 col-md-4 col-md-offset-4"><div ng-show="l_status_0" class="alert alert-danger">Email or password is wrong</div><div ng-show="l_status_1" class="alert alert-success">Login in..</div></div></div>
		<table class="myTable">
			<div class="form-group">
			<tr>
				<td><label for="l_email">Email:</label></td>
				<td><input type="email" class="form-control" name="l_email" placeholder="Enter Email" ng-model="l_email" ng-style="emailStyle" ng-change="analyze2(l_email)" required /></td>
				<td></td>
			</tr>
			<tr>
				<td></td>
				<td>
					<span style="color:red"  id="l_email" ng-show="myForm.l_email.$dirty && myForm.l_email.$invalid"><span ng-show="myForm.l_email.$error.required">Email is required.</span><span ng-show="myForm.l_email.$error.email">Invalid email address.</span></span>
				</td>
				<td></td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
				<td><label for="l_password" >Password:</label></td>
				<td>
					<input type="password" class="form-control" name="l_password" placeholder="Enter Password" ng-model="l_password" ng-style="passStyle" ng-change="analyze(l_password)" id="show_pass" data-toggle="password"  required />
				</td>
				<td></td>
			</tr>
			<tr>
				<td></td>
				<td>
					<span style="color:red;" id="l_password" ng-show="myForm.l_password.$dirty && myForm.l_password.$invalid">
					<span ng-show="myForm.l_password.$error.required">Password is required.</span>
					</span>
				</td>
				<td></td>
			</tr>
			</div>
			<tr>

				<td><input type="submit" class="btn btn-primary" ng-click="login_status()" ng-disabled="myForm.l_email.$invalid || myForm.l_password.$invalid"></td>
				<td></td>
				<td></td>

			</tr>
			<tr>
				<td>
					<a class="alert-link" href="signup.php" >or create new account?</a>
				</td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>
					<a class="alert-link" href="forget_password.php" >Forget Password?</a>
				</td>
				<td></td>
				<td></td>
			</tr>
		</table>
		</form>
	</div>
</div>
<script type="text/javascript">
	$("#show_pass").password('toggle');
</script>
<script>
$("select[name='l_email']").focus();
	var myApp = angular.module("myapp", []);
	myApp.controller("BrijController", function($scope,$http) {
				$scope.addCustomClass = function (ele_id,c_name) {
                angular.element(document.querySelector("#"+ele_id)).addClass(""+c_name);
            };
            $scope.removeCustomClass = function (ele_id,c_name) {
                angular.element(document.querySelector("#"+ele_id)).removeClass(""+c_name);
            };
				$scope.emailStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze2 = function(value) {
					var patt2=new RegExp("^[a-z0-9._]+@[a-z]+\.[a-z.]{2,5}$");
                    if(patt2.test(value)) {
						$scope.emailStyle["border-color"] = "green";
                    }
					else {
                        $scope.emailStyle["border-color"] = "red";
                    }
                };
					$scope.login_status =function()
									{
										$http({
													method : "POST",
													url : "login_data.php",
													data: "l_email="+$scope.l_email+"&l_password="+$scope.l_password,
													headers: {'Content-Type': 'application/x-www-form-urlencoded'}
												}).then(function mySuccess(response) {
													flag = response.data;
													// we should be using flag in only this block so logic in following
													if(flag.startsWith("11"))
													{
														$scope.l_status_0=false;
														$scope.l_status_1=true;
														document.location=flag.substr(2);
													}
													else
													{
														$scope.l_status_1=false;
														$scope.l_status_0=true;
													}
												}, function myError(response) {

												});
									};
});
</script>
<?php include("footer.php"); ?>
