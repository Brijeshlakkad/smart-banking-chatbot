<?php include("header.php"); ?>
<body>
<div class="container well login_block" align="center">
	<div class="row center-block ">
		<div><caption><a href="index.php"><img src="images/jonsnow.png" class="img-responsive" style="margin-top:10px;width:250px;height:60px;float:center;filter:drop-shadow(0px 0px 3px #ffffff);"/></a></caption></div>
	</div>
	<div class="row" id="brij">
		<form ng-app="myapp" ng-controller="BrijController" name="myForm"  novalidate>
		<br/>
			<div class="row">
			<span class="jon_header">Account details</span>
			<hr style='background-color:#878787;width: 100px;height: 3px;'/>
			</div>
			<table class="myTable">
			<div class="form-group username">
			<tr>
			<td><label for="s_user">Username:</label><br></td>
			<td><input type="text" class="form-control" name="s_user" placeholder="Enter Username" ng-model="s_user"  ng-style="userStyle" ng-change="analyze4(s_user)" onKeyUp="check_exists(this.value,'s_user')" onBlur="check_exists(this.value,'s_user')"  required user-dir></td>
			<td>
			<span style="color:red" id="s_user" ng-show="myForm.s_user.$dirty">
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
			<td><label for="s_fname">First name:</label><br></td>
			<td><input type="text" class="form-control" name="s_fname" placeholder="Enter first name" ng-model="s_fname"  ng-style="fnameStyle" ng-change="analyze6(s_fname)" required  names-dir nameslen-dir></td>
			<td>
			<span style="color:red" id="s_fname" ng-show="myForm.s_fname.$dirty && myForm.s_fname.$invalid">
			<span ng-show="myForm.s_fname.$error.required">First name is required</span>
			<span ng-show="!myForm.s_fname.$error.required && myForm.s_fname.$error.namesvalid">Enter only characters</span>
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
			<td><label for="s_lname">Last name:</label><br></td>
			<td><input type="text" class="form-control" name="s_lname" placeholder="Enter first name" ng-model="s_lname"  ng-style="lnameStyle" ng-change="analyze7(s_lname)" required  names-dir nameslen-dir></td>
			<td>
			<span style="color:red" id="s_lname" ng-show="myForm.s_lname.$dirty && myForm.s_lname.$invalid">
			<span ng-show="myForm.s_lname.$error.required">Last name is required</span>
			<span ng-show="!myForm.s_lname.$error.required && myForm.s_lname.$error.namesvalid">Enter only characters</span>
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
			<td><label for="s_middlename">Middle name:</label><br></td>
			<td><input type="text" class="form-control" name="s_middlename" placeholder="Enter first name" ng-model="s_middlename"  ng-style="middleStyle" ng-change="analyze8(s_middlename)" required  names-dir nameslen-dir></td>
			<td>
			<span style="color:red" id="s_middlename" ng-show="myForm.s_middlename.$dirty && myForm.s_middlename.$invalid">
			<span ng-show="myForm.s_middlename.$error.required">Middle name is required</span>
			<span ng-show="!myForm.s_middlename.$error.required && myForm.s_middlename.$error.namesvalid">Enter only characters</span>
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
			<td><label for="s_email">Email:</label><br></td>
			<td><input type="email" class="form-control" name="s_email" placeholder="Enter Email" ng-model="s_email" ng-style="emailStyle" ng-change="analyze5(s_email)" onKeyUp="check_exists(this.value,'s_email')" onBlur="check_exists(this.value,'s_email')" required></td>
			<td>
			<span style="color:red" id="s_email" ng-show="myForm.s_email.$dirty">
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
			<td><label for="s_password">Password:</label><br></td>
			<td><input  type="password" class="form-control" name="s_password" placeholder="Enter Password"  ng-model="s_password" ng-style="passwordStrength" ng-change="analyze(s_password)" required pass-dir></td>
			<td><a class="badge my_badge" data-toggle="tooltip" data-placement="top" title="Password should contain at least one number and at least one character. It also have at least length of 6 characters">?</a>
			<span style="color:red" id="s_password" ng-show="myForm.s_password.$dirty && myForm.s_password.$invalid">
			<span ng-show="myForm.s_password.$error.required">Password is required</span>
			<span ng-show="!myForm.s_password.$error.required && myForm.s_password.$error.passvalid">Invalid Password</span>
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
			<td><label for="s_cpassword">Confirm Password:</label><br></td>
			<td><input ng-disabled="!myForm.s_password.$valid" type="password" class="form-control" name="s_cpassword" placeholder="Enter Confirm Password"  ng-model="s_cpassword" ng-style="cpassStyle" ng-change="analyze2(s_cpassword,s_password)" onkeyup="check_pass(this.value)" required cpass-dir></td>
			<td>
			<span style="color:red" id="s_cpassword" ng-show="myForm.s_cpassword.$dirty">
			<span ng-show="myForm.s_cpassword.$error.required && myForm.s_cpassword.$invalid">Password is required.</span>
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
			<td><label for="s_mobile">Contact number:</label><br></td>
			<td><input  type="text" class="form-control" name="s_mobile" placeholder="Enter Phone number" ng-style="mobStyle" ng-model="s_mobile" ng-change="analyze3(s_mobile)" onKeyUp="check_exists(this.value,'s_mobile')" onBlur="check_exists(this.value,'s_mobile')" required mobile-dir></td>
			<td>
			<span style="color:red" id="s_mobile" ng-show="myForm.s_mobile.$dirty">
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
				<td><label for="gender">Gender</label></td>
				<td><select class="form-control" name="gender" ng-dropdown id="gender" ng-model="gender" ng-style="genderStyle"  ng-change="analyze4(gender)" required>
			 	<option
					ng-repeat="x in genderOptions"
					ng-value="x">{{x}}</option>
				</select></td>
				<td>
					<span style="color:red" id="s_gender" ng-show="myForm.gender.$dirty && myForm.gender.$invalid">
					<span ng-show="myForm.gender.$error.required">required</span>
					</span>
				</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
				<td><label for="dob">DOB</label></td>
				<td><input class="form-control" type="date" name="dob" id="dob" ng-model="dob" max="{{maxd}}" required /></td>
				<td>
					<span style="color:red" id="s_dob" ng-show="myForm.dob.$dirty && myForm.dob.$invalid">
					<span ng-show="myForm.dob.$error.required">DOB is required</span>
					</span>
				</td>
			</tr>
			</div>
			</table>
			<div class="row">
			<br/>
			<br/>
			<span class="jon_header">Address details</span>
			<hr style='background-color:#878787;width: 100px;height: 3px;'/>
			</div>
			<table class="myTable">
			<div class="form-group">
			<tr>
			<td><label for="s_postaladd">Postal Address</label><br></td>
			<td><input type="text" class="form-control" name="s_postaladd" placeholder="Enter postaladd" ng-model="s_postaladd"  ng-style="postaladdStyle" ng-change="analyze9(s_postaladd)" required address-dir></td>
			<td>
			<span style="color:red" id="s_postaladd" ng-show="myForm.s_postaladd.$dirty && myForm.s_postaladd.$invalid">
			<span ng-show="myForm.s_postaladd.$error.required">Postal address is required</span>
			<span ng-show="!myForm.s_postaladd.$error.required && myForm.s_postaladd.$error.addressvalid">Do not use unused character.</span>
			<span ng-show="!myForm.s_postaladd.$error.required && myForm.s_postaladd.$error.addresslengthvalid">Enter more details so we can understand</span>
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
			<td><label for="s_permadd">Permanent Address</label><br></td>
			<td><input type="text" class="form-control" name="s_permadd" placeholder="Enter permadd" ng-model="s_permadd"  ng-style="permaddStyle" ng-change="analyze10(s_permadd)" required address-dir></td>
			<td><input type="checkbox" name="same_as" id="same_as" ng-model="same_as" ng-change="address_fun()" /> Same as above
			<span style="color:red" id="s_permadd" ng-show="myForm.s_permadd.$dirty && myForm.s_permadd.$invalid">
			<span ng-show="myForm.s_permadd.$error.required">Permanent address is required</span>
			<span ng-show="!myForm.s_permadd.$error.required && myForm.s_permadd.$error.addressvalid">Do not use unused character.</span>
			<span ng-show="!myForm.s_permadd.$error.required && myForm.s_permadd.$error.addresslengthvalid">Enter more details so we can understand</span>
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
			<td><label for="s_pincode">Pincode:</label><br></td>
			<td><input type="text" class="form-control" name="s_pincode" placeholder="Enter pincode name" ng-model="s_pincode"  ng-style="pincodeStyle" ng-change="analyze14(s_pincode)" required  pincode-dir></td>
			<td>
			<span style="color:red" id="s_s_pincode" ng-show="myForm.s_pincode.$dirty && myForm.s_pincode.$invalid">
					<span ng-show="myForm.s_pincode.$error.required">Pincode is required</span>
					<span ng-show="!myForm.s_pincode.$error.required && myForm.s_pincode.$error.pincodevalid">Invalid pincode</span>
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
			<td><label for="s_city">City:</label><br></td>
			<td><input type="text" class="form-control" name="s_city" placeholder="Enter city name" ng-model="s_city"  ng-style="cityStyle" ng-change="analyze11(s_city)" required  names-dir></td>
			<td>
			<span style="color:red" id="s_city" ng-show="myForm.s_city.$dirty && myForm.s_city.$invalid">
			<span ng-show="myForm.s_city.$error.required">City is required</span>
			<span ng-show="!myForm.s_city.$error.required && myForm.s_city.$error.namesvalid">Enter only characters</span>
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
			<td><label for="s_state">State:</label><br></td>
			<td><input type="text" class="form-control" name="s_state" placeholder="Enter state name" ng-model="s_state"  ng-style="stateStyle" ng-change="analyze12(s_state)" required  names-dir></td>
			<td>
			<span style="color:red" id="s_state" ng-show="myForm.s_state.$dirty && myForm.s_state.$invalid">
			<span ng-show="myForm.s_state.$error.required">State is required</span>
			<span ng-show="!myForm.s_state.$error.required && myForm.s_state.$error.namesvalid">Enter only characters</span>
			</span>
			</td>
			</tr>
			</div>
			<div class="form-group">
			<tr>
			<td><label for="s_country">Country:</label><br></td>
			<td><input type="text" class="form-control" name="s_country" placeholder="Enter country name" ng-model="s_country"  ng-style="countryStyle" ng-change="analyze13(s_country)" required  names-dir></td>
			<td>
			<span style="color:red" id="s_country" ng-show="myForm.s_country.$dirty && myForm.s_country.$invalid">
			<span ng-show="myForm.s_country.$error.required">Country is required</span>
			<span ng-show="!myForm.s_country.$error.required && myForm.s_country.$error.namesvalid">Enter only characters</span>
			</span>
			</td>
			</tr>
			</div>
			</table>
			<table class="myTable">
			<tr>
			<td><input type="submit" onClick="check_details()" id="submit_btn" value="Submit" class="btn btn-primary" ng-disabled="myForm.s_user.$invalid ||  myForm.s_email.$invalid ||  myForm.s_password.$invalid ||  myForm.s_cpassword.$invalid || myForm.s_mobile.$invalid || myForm.s_fname.$invalid ||   myForm.s_lname.$invalid || myForm.s_middlename.$invalid || myForm.gender.$invalid || myForm.s_dob.$invalid || myForm.s_postaladd.$invalid || myForm.s_permadd.$invalid || myForm.s_city.$invalid || myForm.s_state.$invalid || myForm.s_country.$invalid || myForm.s_pincode.$invalid" /></td>
			<td id="status"><img src="images/small_loader.gif" id="spinner" style="height:30px;width:30px;" alt="Loading" /></td>
			<td></td>
			</tr>
			<tr>
				<td>
					<a class="alert-link" href="login.php" >have a account?</a>
				</td>
				<td></td>
				<td></td>
			</tr>
			</table>
			</form>
	</div>
</div>

<script>

	var myApp = angular.module("myapp", []);
	var username="-99";
	myApp.controller("BrijController", function($scope,$http) {
		$scope.genderOptions = [
				"Male","Female","Other"
			];
		$scope.maxd = new Date() ;
                var strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
                var mediumRegex = new RegExp("^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})");
                $scope.passwordStrength = {
					"border-width":"1.45px"
                };
                $scope.analyze = function(value) {
                    if(strongRegex.test(value)) {
                        $scope.passwordStrength["border-color"] = "green";
                    } else if(mediumRegex.test(value)) {
                        $scope.passwordStrength["border-color"] = "orange";
                    } else {
                        $scope.passwordStrength["border-color"] = "red";
                    }
                };

				var patt = new RegExp("^[0-9]{10}$");
				$scope.mobStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze3 = function(value) {
									if(patt.test(value) && value.length>3) {
					var flag=1;
						$http({
							method : "POST",
							url : "check_exists.php",
							data: "f=s_mobile&q="+value,
							headers: {'Content-Type': 'application/x-www-form-urlencoded'}
						}).then(function mySuccess(response) {
							flag = response.data;
							// we should be using flag in only this block so logic in following
							if(flag==0)
								$scope.mobStyle["border-color"] = "green";
							else
								$scope.mobStyle["border-color"] = "red";
						}, function myError(response) {

						});

									}
				else {
											$scope.mobStyle["border-color"] = "red";
									}
                };

				var patt_for_names = /^[a-zA-Z]+$/
				$scope.fnameStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze6 = function(value) {
                    if(patt_for_names.test(value) && value.length>1) {
                        $scope.fnameStyle["border-color"] = "green";
                    }else {
                        $scope.fnameStyle["border-color"] = "red";
                    }
                };
				$scope.lnameStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze7 = function(value) {
                    if(patt_for_names.test(value)  && value.length>1) {
                        $scope.lnameStyle["border-color"] = "green";
                    }else {
                        $scope.lnameStyle["border-color"] = "red";
                    }
                };
				$scope.middleStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze8 = function(value) {
                    if(patt_for_names.test(value)  && value.length>1) {
                        $scope.middleStyle["border-color"] = "green";
                    }else {
                        $scope.middleStyle["border-color"] = "red";
                    }
                };
				$scope.cpassStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze2 = function(value1,value2) {
                    if(value1 == value2 && value2.length!=0) {
                        $scope.cpassStyle["border-color"] = "green";
                    }
					else {
                        $scope.cpassStyle["border-color"] = "red";
                    }
                };

				var patt_user = new RegExp("^[0-9a-zA-Z_.]+$");
				$scope.userStyle = {
					"border-width":"1.45px"
                };
        $scope.analyze4 = function(value) {
                    if(patt_user.test(value) && value.length>3) {
						var flag=1;
							$http({
								method : "POST",
								url : "check_exists.php",
								data: "f=s_user&q="+value,
								headers: {'Content-Type': 'application/x-www-form-urlencoded'}
							}).then(function mySuccess(response) {
								flag = response.data;
								// we should be using flag in only this block so logic in following
								if(flag==0)
									$scope.userStyle["border-color"] = "green";
								else
									$scope.userStyle["border-color"] = "red";
							}, function myError(response) {

							});

                    }
					else {
                        $scope.userStyle["border-color"] = "red";
                    }
                };

				$scope.emailStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze5 = function(value) {
					var patt2=new RegExp("^[a-z0-9._]+@[a-z]+\.[a-z.]{2,5}$");
                    if(patt2.test(value)) {

						var flag=1;
							$http({
								method : "POST",
								url : "check_exists.php",
								data: "f=s_email&q="+value,
								headers: {'Content-Type': 'application/x-www-form-urlencoded'}
							}).then(function mySuccess(response) {
								flag = response.data;
								// we should be using flag in only this block so logic in following
								if(flag==0)
									$scope.emailStyle["border-color"] = "green";
								else
									$scope.emailStyle["border-color"] = "red";
							}, function myError(response) {

							});

                    }
					else {
                        $scope.emailStyle["border-color"] = "red";
                    }
                };
				var patt_address = new RegExp("^[0-9a-zA-Z,/. ]+$");
				$scope.postaladdStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze9 = function(value) {
                    if(patt_address.test(value) && value.length >= 10) {
                        $scope.postaladdStyle["border-color"] = "green";
                    }else {
                        $scope.postaladdStyle["border-color"] = "red";
                    }
                };
				$scope.permaddStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze10 = function(value) {
                    if(patt_address.test(value) && value.length >= 10) {
                        $scope.permaddStyle["border-color"] = "green";
                    }else {
                        $scope.permaddStyle["border-color"] = "red";
                    }
                };

				var patt_pincode = new RegExp("^[0-9]{6}$");
				$scope.pincodeStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze14 = function(value) {
                    if(patt_pincode.test(value)) {
                        $scope.pincodeStyle["border-color"] = "green";
                    }else {
                        $scope.pincodeStyle["border-color"] = "red";
                    }
                };
				$scope.cityStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze11 = function(value) {
                    if(/^[a-zA-Z]+$/.test(value) && value!=null)
					{
                        $scope.cityStyle["border-color"] = "green";
                    }else {
                        $scope.cityStyle["border-color"] = "red";
                    }
                };
		$scope.stateStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze12 = function(value) {
                    if(/^[a-zA-Z]+$/.test(value) && value!=null)
					{
                        $scope.stateStyle["border-color"] = "green";
                    }else {
                        $scope.stateStyle["border-color"] = "red";
                    }
                };
		$scope.countryStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze13 = function(value) {
                    if(/^[a-zA-Z]+$/.test(value) && value!=null)
					{
                        $scope.countryStyle["border-color"] = "green";
                    }else {
                        $scope.countryStyle["border-color"] = "red";
                    }
                };
		$scope.address_fun = function() {
			if($scope.same_as)
				$scope.s_permadd=$scope.s_postaladd;
			else
				$scope.s_permadd="";
		};
});
myApp.directive('namesDir', function() {
				return {
					require: 'ngModel',
					link: function(scope, element, attr, mCtrl) {
						function myValidation(value) {
							var patt =  /^[a-zA-Z]+$/
							if (patt.test(value)) {
								mCtrl.$setValidity('namesvalid', true);
							} else {
								mCtrl.$setValidity('namesvalid', false);
							}
							return value;
						}
						mCtrl.$parsers.push(myValidation);
					}
				};
});
myApp.directive('nameslenDir', function() {
				return {
					require: 'ngModel',
					link: function(scope, element, attr, mCtrl) {
						function myValidation(value) {
							if (value.length>1) {
								mCtrl.$setValidity('nameslenvalid', true);
							} else {
								mCtrl.$setValidity('nameslenvalid', false);
							}
							return value;
						}
						mCtrl.$parsers.push(myValidation);
					}
				};
});
myApp.directive('userDir', function() {
				return {
					require: 'ngModel',
					link: function(scope, element, attr, mCtrl) {
						function myValidation(value) {
							var patt_user = new RegExp("^[0-9a-zA-Z_.]+$");
							if (patt_user.test(value) && value.length>3) {
								mCtrl.$setValidity('uservalid', true);
							} else {
								mCtrl.$setValidity('uservalid', false);
							}
							return value;
						}
						mCtrl.$parsers.push(myValidation);
					}
				};
});
myApp.directive('mobileDir', function() {
				return {
					require: 'ngModel',
					link: function(scope, element, attr, mCtrl) {
						function myValidation(value) {
							var patt = new RegExp("^[0-9]{10}$");
							if (patt.test(value)) {
								mCtrl.$setValidity('mobvalid', true);
							} else {
								mCtrl.$setValidity('mobvalid', false);
							}
							return value;
						}
						mCtrl.$parsers.push(myValidation);
					}
				};
});
myApp.directive('passDir', function() {
				return {
					require: 'ngModel',
					link: function(scope, element, attr, mCtrl) {
						function myValidation(value) {
							var patt=new RegExp("^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})");
							if (patt.test(value)) {
								mCtrl.$setValidity('passvalid', true);
							} else {
								mCtrl.$setValidity('passvalid', false);
							}
							return value;
						}
						mCtrl.$parsers.push(myValidation);
					}
				};
});
myApp.directive('addressDir', function() {
				return {
					require: 'ngModel',
					link: function(scope, element, attr, mCtrl) {
						function myValidation(value) {
							var patt = new RegExp("^[0-9a-zA-Z,/. ]+$");
							if (patt.test(value)) {
								mCtrl.$setValidity('addressvalid', true);
							} else {
								mCtrl.$setValidity('addressvalid', false);
							}
							if(value.length>=10)
							{
								mCtrl.$setValidity('addresslengthvalid', true);
							} else {
								mCtrl.$setValidity('addresslengthvalid', false);
							}
							return value;
						}
						mCtrl.$parsers.push(myValidation);
					}
				};
});
myApp.directive('pincodeDir', function() {
				return {
					require: 'ngModel',
					link: function(scope, element, attr, mCtrl) {
						function myValidation(value) {
							var patt = new RegExp("^[0-9]{6}$");
							if (patt.test(value)) {
								mCtrl.$setValidity('pincodevalid', true);
							} else {
								mCtrl.$setValidity('pincodevalid', false);
							}
							return value;
						}
						mCtrl.$parsers.push(myValidation);
					}
				};
});
function check_pass(cpass)
	{
		var pass=myForm.s_password.value;

		if(pass!=cpass && cpass!="")
			$("#s_cpassword").html("Passwords do not match");
		else if(cpass=="")
			$("#s_cpassword").html("Password is required");
		else
			$("#s_cpassword").html("");
	}
function check_exists(val_f,f)
	{
				var x=new XMLHttpRequest();
				x.onreadystatechange=function()
				{
					if(x.readyState==4 && x.status==200)
						{
							var data=this.responseText;
							if(data!=0)
								$("#"+f).html(data);
							else
								$("#"+f).html("");
						}
				};
				x.open("POST","check_exists.php",true);
				x.setRequestHeader("Content-type","application/x-www-form-urlencoded");
				x.send("f="+f+"&q="+val_f);
	}

function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();
    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
    return [year, month, day].join('-');
	}
function get_username(userid)
	{
				var x=new XMLHttpRequest();
				x.onreadystatechange=function()
				{

					if(x.readyState==4 && x.status==200)
						{
							var data=this.responseText;
							$("#brij").append("<form id='part2' action='signup_part2.php' method='post'><input type='hidden' name='Username' value='"+data+"' /></form>");
							$("#part2").submit();

						}
				};
				x.open("POST","customer_interface.py",true);
				x.setRequestHeader("Content-type","application/x-www-form-urlencoded");
				x.send("get_data_id=username"+"&userid="+userid);
	}
function check_details()
	{
		var password=myForm.s_password.value;
		var mobile=myForm.s_mobile.value;
		var user=myForm.s_user.value;
		var email=myForm.s_email.value;
		var fname=myForm.s_fname.value;
		var lname=myForm.s_lname.value;
		var middlename=myForm.s_middlename.value;
		var postaladd=myForm.s_postaladd.value;
		var permadd=myForm.s_permadd.value;
		var pincode=myForm.s_pincode.value;
		var gender=myForm.gender.value;
		var t_dob=myForm.dob.value;
		var country=myForm.s_country.value;
		var state=myForm.s_state.value;
		var city=myForm.s_city.value;
		var dob=formatDate(t_dob);
		gender=gender.substr(gender.indexOf(":")+1,gender.length);
		var x=new XMLHttpRequest();
				x.onreadystatechange=function()
				{
					if(x.readyState<4)
						{
							$("#status").empty();
							$("#spinner").show();
						}
					if(x.readyState==4 && x.status==200)
						{
							var data=this.responseText;
							if(data!=-99)
							{
								$("#spinner").hide();
								get_username(data);
							}
							else
							{
								$("#spinner").hide();
								$("#status").html("<span style='color:red;'>Please enter only valid details</span>");
							}
						}
				};
				x.open("POST","signup_data.py",true);
				x.setRequestHeader("Content-type","application/x-www-form-urlencoded");
				x.send("s_user="+user+"&s_email="+email+"&s_password="+password+"&s_mobile="+mobile+"&s_gender="+gender+"&s_dob="+dob+"&s_postaladd="+postaladd+"&s_permadd="+permadd+"&s_country="+country+"&s_state="+state+"&s_city="+city+"&s_fname="+fname+"&s_lname="+lname+"&s_middlename="+middlename+"&s_pincode="+pincode);

	}
$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
	$("#spinner").hide();
});
</script>
</body>
</html>
