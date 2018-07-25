<?php include_once("header.php"); ?>
<?php check_session(); ?>
<link rel="stylesheet" type="text/css" href="css/vertical_tab.css" />
<div class="container-fluid my_well">
	<div class="row" align="center">
		<h2 class="c_profile_header">Personal Settings</h2>
		<div class="row" style="margin-top: 20px;">

			<div class="tab">
			  <button class="tablinks" onclick="openCity(event, 'acc_details')" id="defaultOpen">Account Details</button>
			  <button class="tablinks" onclick="openCity(event, 'change_password')">Change Password</button>
			  <button class="tablinks" onclick="openCity(event, 'billing_details')">Billing Details</button>
			</div>
			<form ng-app="myapp" ng-controller="BrijController" name="myForm"  novalidate>
			<div id="acc_details" class="tabcontent">
			  <h3>Account Details</h3>
			  <div class="row">
			  	<table class="myTable">
						<div class="form-group">
						<tr>
						<td><label for="s_user">Username:</label><br></td>
						<td><input type="text" class="form-control" name="s_user" placeholder="Enter Username" ng-model="s_user"  ng-style="userStyle" ng-change="analyze4(s_user)" onKeyUp="check_exists(this.value,'s_user')" onBlur="check_exists(this.value,'s_user')"  required></td>
						<td>
						<span style="color:red" id="s_user" ng-show="myForm.s_user.$dirty">
						</span>
						</td>
						</tr>
						</div>
						<div class="form-group">
						<tr>
						<td><label for="s_fname">First name:</label><br></td>
						<td><input type="text" class="form-control" name="s_fname" placeholder="Enter first name" ng-model="s_fname"  ng-style="fnameStyle" ng-change="analyze6(s_fname)" required  names-dir></td>
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
						<td><input type="text" class="form-control" name="s_lname" placeholder="Enter first name" ng-model="s_lname"  ng-style="lnameStyle" ng-change="analyze7(s_lname)" required  names-dir></td>
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
						<td><input type="text" class="form-control" name="s_middlename" placeholder="Enter first name" ng-model="s_middlename"  ng-style="middleStyle" ng-change="analyze8(s_middlename)" required  names-dir></td>
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
						<td><input type="email" class="form-control" name="s_email" placeholder="Enter Email" ng-model="s_email" ng-style="emailStyle" ng-change="analyze5(s_email)" onKeyUp="check_exists(this.value,'s_email')" onBlur="check_exists(this.value,'s_email')" required disabled></td>
						<td>
						<span style="color:red" id="s_email" ng-show="myForm.s_email.$dirty">
						</span>
						</td>
						</tr>
						</div>
				  </table>
			  </div>
			</div>
			</form>
			<div id="change_password" class="tabcontent">
			  <h3>Change Password</h3>
			  <p>Paris is the capital of France.</p> 
			</div>

			<div id="billing_details" class="tabcontent">
			  <h3>Billing Details</h3>
			  <p>Tokyo is the capital of Japan.</p>
			</div>
			
		</div>
	</div>
</div>
<div class="please_wait_modal"></div>
<script>
$body = $("body");
$(document).on({
    ajaxStart: function() { $body.addClass("loading");    },
     ajaxStop: function() { $body.removeClass("loading"); }    
});

	var myApp = angular.module("myapp", []);
	
	myApp.controller("BrijController", function($scope,$http) {
		$scope.genderOptions = [
				"Male","Female","Other"
			];
		var userid="<?php echo $_SESSION['Userid']; ?>";
		$scope.get_any_value=function(f,user,callback)
		{
			$http({
				method : "POST",
				url : "customer_interface.py",
				data: "get_data="+f+"&user="+user,
				headers: {'Content-Type': 'application/x-www-form-urlencoded'}
			}).then(function mySuccess(response) {
				callback(response.data);
			}, function myError(response) {
			});
			
		};
		var set_val_user=function(val){
			$scope.s_user= val;
		};
		$scope.get_any_value("username",userid,set_val_user);
		var set_val_fname=function(val){
			$scope.s_fname= val;
		};
		$scope.get_any_value("fname",userid,set_val_fname);
		var set_val_lname=function(val){
			$scope.s_lname= val;
		};
		$scope.get_any_value("lname",userid,set_val_lname);
		var set_val_middle_name=function(val){
			$scope.s_middlename= val;
		};
		$scope.get_any_value("middle_name",userid,set_val_middle_name);
		var set_val_email=function(val){
			$scope.s_email= val;
		};
		$scope.get_any_value("email",userid,set_val_email);
		
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
                    if(patt.test(value)) {
                        $scope.mobStyle["border-color"] = "green";
                    }else {
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
		var x=new XMLHttpRequest();
				x.onreadystatechange=function()
				{
					if(x.readyState<4)
						{
							$("#spinner").show();
						}
					if(x.readyState==4 && x.status==200)
						{
							var data=this.responseText;
							if(data==1)
							{
								$("#spinner").hide();
								$("#status").html("<span style='color:green;'>You have registered successfully.</span>");
							}
							else
							{
								$("#spinner").hide();
								$("#status").html("<span style='color:red;'>Error! Try agian..</span>");
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
<script src="js/vertical_tab.js"></script>
<?php include("footer.php"); ?>