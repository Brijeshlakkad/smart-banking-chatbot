<?php include_once("header.php"); ?>
<?php check_session(); ?>
<link rel="stylesheet" type="text/css" href="css/vertical_tab.css" />
<div class="container-fluid my_well">
	<div class="row" align="center">
		<h2 class="c_profile_header">Personal Settings</h2>
		<div class="row"  ng-app="myapp" ng-controller="BrijController" style="margin-top: 20px;">

			<div class="tab">
		  	  <button class="tablinks" onclick="openCity(event, 'per_acc_details')" id="defaultOpen">Personal Account Details</button>
			  <button class="tablinks" onclick="openCity(event, 'bank_acc_details')">Bank Account Details</button>
			  <button class="tablinks" onclick="openCity(event, 'change_password')">Change Password</button>
			  <button class="tablinks" onclick="openCity(event, 'billing_details')">Billing Details</button>
			</div>
			<form name="myForm"  novalidate>
			<div id="per_acc_details" class="tabcontent">
			  <h3>Personal Account Details</h3>
			  <div class="row">
			  	<table class="myTable">
						<div class="form-group">
						<tr>
						<td><label for="s_user">Username:</label><br></td>
						<td><input type="text" class="form-control" name="s_user" placeholder="Enter Username" ng-model="s_user"  ng-style="userStyle" ng-change="analyze4(s_user)" onKeyUp="check_exists(this.value,'s_user')" onBlur="check_exists(this.value,'s_user')"  required user-dir></td>
						<td>
						<span style="color:red" id="s_user" ng-show="myForm.s_user.$dirty">
						</td>
						</tr>
						</div>
						<div class="form-group">
						<tr>
						<td><label for="s_email">Email:</label><br></td>
						<td><input type="text" class="form-control" name="s_email" placeholder="Enter Email" ng-model="s_email" ng-style="emailStyle" ng-change="analyze5(s_email)" onKeyUp="check_exists(this.value,'s_email')" onBlur="check_exists(this.value,'s_email')" required disabled></td>
						<td>
						<span style="color:red" id="s_email" ng-show="myForm.s_email.$dirty">
						
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
						<td><label for="s_mobile">Contact number:</label><br></td>
						<td><input  type="text" class="form-control" name="s_mobile" placeholder="Enter Phone number" ng-style="mobStyle" ng-model="s_mobile" ng-change="analyze3(s_mobile)" required mobile-dir></td>
						<td>
						<span style="color:red" id="s_mobile" ng-show="myForm.s_mobile.$dirty && myForm.s_mobile.$invalid">
						<span ng-show="myForm.s_mobile.$error.required">Contact number is required.</span>
						<span ng-show="!myForm.s_mobile.$error.required && myForm.s_mobile.$error.mobvalid">Invalid contact number</span>
						</span>
						</td>
						</tr>
						</div>
						<div class="form-group">
						<tr>
							<td><label for="dob">DOB</label></td>
							<td>{{dob}}</td>
							<td></td>
						</tr>
						</div>
						<div class="form-group">
							<tr>
								<td><input type="submit" onClick="check_part1()" id="submit_btn" value="Submit" class="btn btn-primary" ng-disabled="myForm.s_user.$invalid || myForm.s_email.$invalid || myForm.s_mobile.$invalid || myForm.s_fname.$invalid || myForm.s_lname.$invalid || myForm.s_middlename.$invalid" /></td>
								<td id="status"><img src="images/small_loader.gif" id="spinner_part1" style="height:30px;width:30px;" alt="Loading" /></td>
								<td></td>
							</tr>
						</div>
				  </table>
			  </div>
			</div>
			</form>
			<div id="bank_acc_details" class="tabcontent">
			  <h3>Bank Account Details</h3>
			  <div class="row" ng-if="hasAcc==1">
			  	<table class="myTable table-striped">
			  		<tr>
			  			<td>Account Name:</td>
			  			<td>{{acc_name}}</td>
			  		</tr>
			  		<tr>
			  			<td>Account Number:</td>
			  			<td>{{acc_no}}</td>
			  		</tr>
			  		<tr>
			  			<td>Account Type:</td>
			  			<td>{{acc_type}}</td>
			  		</tr>
			  		<tr>
			  			<td>Balance:</td>
			  			<td ng-if="passcode==-99 || passcode.length==0">You have not geneated your passcode <small>(Click below button)</small></td>
			  			<td ng-if="passcode!=-99 && passcode.length!=0"><button class="btn btn-primary btn-sm" id="change_pass" ng-click="change_passcode">View Balance</button></td>
			  		</tr>
			  		<tr>
			  			<td>Passcode:</td>
			  			<td ng-if="passcode==-99 || passcode.length==0"><button class="btn btn-default btn-sm" id="get_pass" ng-click="get_passcode()">Get Passcode</button></td>
			  			<td ng-if="passcode!=-99 && passcode.length!=0"><button class="btn btn-primary btn-sm" id="change_pass" ng-click="change_passcode">Change Passcode</button></td>
			  		</tr>
			  	</table>
			  </div>
			  <div class="row" ng-if="hasAcc==0">
			  	<div class="alert alert-warning" style="margin: 10px;">Pending</div>
			  	<div class="row" style="margin: 10px;">(Your account is not verified yet.)</div>
			  </div>
			  <div class="row" ng-if="hasAcc==-1">
			  	<div class="alert alert-danger" style="margin: 10px;">Rejected</div>
			  	<div class="row" style="margin: 10px;">(Your account is rejected at verification process.)</div>
			  </div>
			</div>
			<form name="myForm2">
			<div id="change_password" class="tabcontent">
			  <h3>Change Password</h3>
			  <div class="row">
		  			<table class="myTable">
			  			<div class="form-group">
						<tr>
						<td><label for="old_password">Old Password:</label><br></td>
						<td><input type="password" class="form-control" name="old_password" placeholder="Enter first name" ng-model="old_password"  ng-style="old_passwordStrength" ng-change="analyze_old(old_password)" required  password-dir></td>
						<td>
						<span style="color:red" id="old_password" ng-show="myForm2.old_password.$dirty && myForm2.old_password.$invalid">
						<span ng-show="myForm2.old_password.$error.required">Old Password is required</span>
						<span ng-show="!myForm2.old_password.$error.required && myForm2.old_password.$error.passvalid">read instructions</span>
						</span>
						</td>
						</tr>
						</div>
						<div class="form-group">
						<tr>
						<td><label for="new_password">New Password:</label><br></td>
						<td><input type="password" class="form-control" name="new_password" placeholder="Enter first name" ng-model="new_password"  ng-style="new_passwordStrength" ng-change="analyze_new(new_password)" required  password-dir></td>
						<td><a class="badge my_badge" data-toggle="tooltip" data-placement="top" title="Password should contain at least one number and at least one character">?</a>
						<span style="color:red" id="new_password" ng-show="myForm2.new_password.$dirty && myForm2.new_password.$invalid">
						<span ng-show="myForm2.new_password.$error.required">New Password is required</span>
						<span ng-show="!myForm2.new_password.$error.required && myForm2.new_password.$error.passvalid">read instructions</span>
						</span>
						</td>
						</tr>
						</div>
						<div class="form-group">
						<tr>
						<td><label for="confirm_new_password">Confirm New Password:</label><br></td>
						<td><input type="password" class="form-control" name="confirm_new_password" placeholder="Enter first name" ng-model="confirm_new_password" ng-disabled="!myForm2.new_password.$valid" ng-style="cnew_passwordStrength" ng-change="analyze_cnew(new_password,confirm_new_password)" required  password-dir cpass-dir></td>
						<td>
						<span style="color:red" id="confirm_new_password" ng-show="myForm2.confirm_new_password.$dirty && myForm2.confirm_new_password.$invalid">
						<span ng-show="myForm2.confirm_new_password.$error.required">Password is required</span>
						<span ng-show="!myForm2.confirm_new_password.$error.required && myForm2.confirm_new_password.$error.passvalid">read instructions</span>
						<span ng-show="!myForm2.confirm_new_password.$error.required && myForm2.confirm_new_password.$error.cpassvalid">Passwords do not match</span>
						</span>
						</td>
						</tr>
						</div>
						<div class="form-group">
							<tr>
								<td><input type="submit" ng-click="check_part2()" id="submit_btn" value="Submit" class="btn btn-primary" ng-disabled="myForm2.old_password.$invalid || myForm2.new_password.$invalid || myForm2.confirm_new_password.$invalid" /></td>
								<td id="status_part2"><img src="images/small_loader.gif" ng-if="spinner_part2" id="spinner_part2" style="height:30px;width:30px;" alt="Loading" /></td>
								<td></td>
							</tr>
						</div>
					</table>
			  </div>
			</div>
			<div id="billing_details" class="tabcontent">
			  <form name="bill_form" novalidate>
			  	<table class="myTable">
					<div class="form-group">
					<tr>
					<td><label for="postal_add">Postal Address</label><br></td>
					<td><input type="text" class="form-control" name="postal_add" placeholder="Enter postaladd" ng-model="postal_add"  ng-style="postaladdStyle" ng-change="analyze9(postal_add)" required address-dir></td>
					<td>
					<span style="color:red" id="postal_add" ng-show="bill_form.postal_add.$dirty && bill_form.postal_add.$invalid">
					<span ng-show="bill_form.postal_add.$error.required">Postal address is required</span>
					<span ng-show="!bill_form.postal_add.$error.required && bill_form.postal_add.$error.addressvalid">Do not use unused character.</span>
					<span ng-show="!bill_form.postal_add.$error.required && bill_form.postal_add.$error.addresslengthvalid">Enter more details so we can understand</span>
					</span>
					</td>
					</tr>
					</div>
					<div class="form-group">
					<tr>
					<td><label for="perm_add">Permanent Address</label><br></td>
					<td><input type="text" class="form-control" name="perm_add" placeholder="Enter permadd" ng-model="perm_add"  ng-style="permaddStyle" ng-change="analyze10(perm_add)" required address-dir></td>
					<td><input type="checkbox" name="same_as" id="same_as" ng-model="same_as" ng-change="address_fun()" /> Same as above
					<span style="color:red" id="perm_add" ng-show="bill_form.perm_add.$dirty && bill_form.perm_add.$invalid">
					<span ng-show="bill_form.perm_add.$error.required">Permanent address is required</span>
					<span ng-show="!bill_form.perm_add.$error.required && bill_form.perm_add.$error.addressvalid">Do not use unused character.</span>
					<span ng-show="!bill_form.perm_add.$error.required && bill_form.perm_add.$error.addresslengthvalid">Enter more details so we can understand</span>
					</span>
					</td>
					</tr>
					</div>
					<div class="form-group">
					<tr>
					<td><label for="pincode">Pincode:</label><br></td>
					<td><input type="text" class="form-control" name="pincode" placeholder="Enter pincode name" ng-model="pincode"  ng-style="pincodeStyle" ng-change="analyze14(pincode)" required  pincode-dir></td>
					<td>
					<span style="color:red" id="pincode" ng-show="bill_form.pincode.$dirty && bill_form.pincode.$invalid">
							<span ng-show="bill_form.pincode.$error.required">Pincode is required</span>
							<span ng-show="!bill_form.pincode.$error.required && bill_form.pincode.$error.pincodevalid">Invalid pincode</span>
					</span>
					</td>
					</tr>
					</div>
					<div class="form-group">
					<tr>
					<td><label for="city">City:</label><br></td>
					<td><input type="text" class="form-control" name="city" placeholder="Enter city name" ng-model="city"  ng-style="cityStyle" ng-change="analyze11(city)" required  names-dir></td>
					<td>
					<span style="color:red" id="city" ng-show="bill_form.city.$dirty && bill_form.city.$invalid">
					<span ng-show="bill_form.city.$error.required">City is required</span>
					<span ng-show="!bill_form.city.$error.required && bill_form.city.$error.namesvalid">Enter only characters</span>
					</span>
					</td>
					</tr>
					</div>
					<div class="form-group">
					<tr>
					<td><label for="state">State:</label><br></td>
					<td><input type="text" class="form-control" name="state" placeholder="Enter state name" ng-model="state"  ng-style="stateStyle" ng-change="analyze12(state)" required  names-dir></td>
					<td>
					<span style="color:red" id="state" ng-show="bill_form.state.$dirty && bill_form.state.$invalid">
					<span ng-show="bill_form.state.$error.required">State is required</span>
					<span ng-show="!bill_form.state.$error.required && bill_form.state.$error.namesvalid">Enter only characters</span>
					</span>
					</td>
					</tr>
					</div>
					<div class="form-group">
					<tr>
					<td><label for="country">Country:</label><br></td>
					<td><input type="text" class="form-control" name="country" placeholder="Enter country name" ng-model="country"  ng-style="countryStyle" ng-change="analyze13(country)" required  names-dir></td>
					<td>
					<span style="color:red" id="country" ng-show="bill_form.country.$dirty && bill_form.country.$invalid">
					<span ng-show="bill_form.country.$error.required">Country is required</span>
					<span ng-show="!bill_form.country.$error.required && bill_form.country.$error.namesvalid">Enter only characters</span>
					</span>
					</td>
					</tr>
					</div>
				</table>
			  </form>
			</div>
			</form>
		</div>
	</div>
</div>
<div class="modal fade" id="success_modal" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>
        <div class="modal-body">
        <div class="alert alert-success">Information updated successfully</div>
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
        <div class="alert alert-danger">Please, try again after few minutes</div>
        </div>
      </div>
    </div>
</div>
<div class="modal fade" id="get_passcode_modal" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>
        <div class="modal-body">
        <div class="alert alert-success">You'll get your first passcode through email. (check your email)</div>
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
		$scope.spinner_part2=false;
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
		var set_val_contact=function(val){
			$scope.s_mobile= val;
		};
		$scope.get_any_value("contact",userid,set_val_contact);
		var set_val_postal_add=function(val){
			$scope.postal_add= val;
		};
		$scope.get_any_value("postal_add",userid,set_val_postal_add);
		var set_val_perm_add=function(val){
			$scope.perm_add= val;
		};
		$scope.get_any_value("perm_add",userid,set_val_perm_add);
		var set_val_city=function(val){
			$scope.city= val;
		};
		$scope.get_any_value("city",userid,set_val_city);
		var set_val_state=function(val){
			$scope.state= val;
		};
		$scope.get_any_value("state",userid,set_val_state);
		var set_val_country=function(val){
			$scope.country= val;
		};
		$scope.get_any_value("country",userid,set_val_country);
		var set_val_pincode=function(val){
			$scope.pincode= val;
		};
		$scope.get_any_value("pincode",userid,set_val_pincode);
		var set_val_gender=function(val){
			$scope.gender= val;
		};
		$scope.get_any_value("gender",userid,set_val_gender);
		var set_val_dob=function(val){
			$scope.dob= val;
		};
		$scope.get_any_value("dob",userid,set_val_dob);
		var set_val_hasAcc=function(val){
			$scope.hasAcc= val;
		};
		$scope.get_any_value("hasAcc",userid,set_val_hasAcc);
		var set_val_jon=function(val){
			$scope.jon= val;
		};
		$scope.get_any_value("jon",userid,set_val_jon);
		var set_val_created_time=function(val){
			$scope.created_time= val;
		};
		$scope.get_any_value("created_time",userid,set_val_created_time);
		$scope.get_acc_details=function(f,user,callback)
		{
			$http({
				method : "POST",
				url : "customer_interface.py",
				data: "get_acc_details="+f+"&user="+user,
				headers: {'Content-Type': 'application/x-www-form-urlencoded'}
			}).then(function mySuccess(response) {
				callback(response.data);
			}, function myError(response) {
			});
			
		};
		var set_val_acc_no=function(val){
			$scope.acc_no= val;
		};
		$scope.get_acc_details("acc_no",userid,set_val_acc_no);
		var set_val_acc_name=function(val){
			$scope.acc_name= val;
		};
		$scope.get_acc_details("acc_name",userid,set_val_acc_name);
		var set_val_acc_type=function(val){
			$scope.acc_type= val+" account";
		};
		$scope.get_acc_details("acc_type",userid,set_val_acc_type);
		var set_val_balance=function(val){
			$scope.balance= val+" $";
		};
		$scope.get_acc_details("balance",userid,set_val_balance);
		var set_val_passcode=function(val){
			$scope.passcode= val;
		};
		$scope.get_acc_details("passcode",userid,set_val_passcode);
		$scope.maxd = new Date() ;
                var strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
                var mediumRegex = new RegExp("^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})");
                $scope.old_passwordStrength = {
					"border-width":"1.45px"
                };
                $scope.analyze_old = function(value) {
                    if(strongRegex.test(value)) {
                        $scope.old_passwordStrength["border-color"] = "green";
                    } else if(mediumRegex.test(value)) {
                        $scope.old_passwordStrength["border-color"] = "orange";
                    } else {
                        $scope.old_passwordStrength["border-color"] = "red";
                    }
                };
		$scope.new_passwordStrength = {
					"border-width":"1.45px"
                };
                $scope.analyze_new = function(value) {
                    if(strongRegex.test(value)) {
                        $scope.new_passwordStrength["border-color"] = "green";
                    } else if(mediumRegex.test(value)) {
                        $scope.new_passwordStrength["border-color"] = "orange";
                    } else {
                        $scope.new_passwordStrength["border-color"] = "red";
                    }
                };
		$scope.cnew_passwordStrength = {
					"border-width":"1.45px"
                };
                $scope.analyze_cnew = function(value) {
                    if(strongRegex.test(value)) {
                        $scope.cnew_passwordStrength["border-color"] = "green";
                    } else if(mediumRegex.test(value)) {
                        $scope.cnew_passwordStrength["border-color"] = "orange";
                    } else {
                        $scope.cnew_passwordStrength["border-color"] = "red";
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
								data: "f=s_user&q="+value+"&u="+userid,
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
				$scope.perm_add=$scope.postal_add;
			else
				$scope.perm_add="";
		};
		$scope.check_part2 = function() {
			
							var old_password=$scope.old_password;
							var new_password=$scope.new_password;
							var cnew_password=$scope.confirm_new_password;
							$http({
								method : "POST",
								url : "customer_interface.py",
								data : "change_password="+old_password+"&new_password="+new_password+"&user="+userid,
								headers: {'Content-Type': 'application/x-www-form-urlencoded'}
							}).then(function mySuccess(response) {
								flag = response.data;
								if(flag==11)
									{
										$("#success_modal").modal("show");
										$("#status_part2").empty();
									}
								else if(flag==-99)
									$("#status_part2").html("<span style='color:red;'>Old password is incorrect</span>");
								else if(flag==-1)
									$("#status_part2").html("<span style='color:red;'>Enter password which is different from previous password</span>");
								else
									{
										$("#error_modal").modal("show");
										$("#status_part2").empty();
									}
							}, function myError(response) {
								$("#error_modal").modal("show");
								$("#status_part2").empty();
							});
               };
		$scope.get_passcode = function() {
							$http({
								method : "POST",
								url : "customer_interface.py",
								data : "get_passcode="+userid,
								headers: {'Content-Type': 'application/x-www-form-urlencoded'}
							}).then(function mySuccess(response) {
								var flag=response.data;
								if(flag==11)
									{
										$("#get_passcode_modal").modal("show");
										setTimeout(function(){
											$("#get_passcode_modal").modal("hidden");
										},200);
									}
								else{
									$("#error_modal").modal("show");
									$("#status_part2").empty();
								}
							}, function myError(response) {
								$("#error_modal").modal("show");
								$("#status_part2").empty();
							});
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
myApp.directive('userDir', function() {
				return {
					require: 'ngModel',
					link: function(scope, element, attr, mCtrl) {
						function myValidation(value) {
							var patt_user = new RegExp("^[0-9a-zA-Z_.]+$");
							if (patt_user.test(value)) {
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
myApp.directive('passwordDir', function() {
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
myApp.directive('cpassDir', function() {
				return {
					require: 'ngModel',
					link: function(scope, element, attr, mCtrl) {
						function myValidation(value) {
							var new_password=document.myForm2.new_password.value;
							if (value==new_password) {
								mCtrl.$setValidity('cpassvalid', true);
							} else {
								mCtrl.$setValidity('cpassvalid', false);
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
		var userid="<?php echo $_SESSION['Userid']; ?>";
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
				x.send("f="+f+"&q="+val_f+"&u="+userid);
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
function check_part1()
	{
		var mobile=myForm.s_mobile.value;
		var user=myForm.s_user.value;
		var email=myForm.s_email.value;
		var fname=myForm.s_fname.value;
		var lname=myForm.s_lname.value;
		var middlename=myForm.s_middlename.value;
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
							if(data==11)
							{
								$("#spinner").hide();
								$("#success_modal").modal("show");
								setTimeout(function(){
									$("#success_modal").modal("hide");
								},1000);
							}
							else
							{
								$("#spinner").hide();
								$("#error_modal").modal("show");
								setTimeout(function(){
									$("#error_modal").modal("hide");
								},1000);
							}
						}
				};
				x.open("POST","customer_interface.py",true);
				x.setRequestHeader("Content-type","application/x-www-form-urlencoded");
				x.send("update_account_details="+user+"&s_email="+email+"&s_mobile="+mobile+"&s_fname="+fname+"&s_lname="+lname+"&s_middlename="+middlename);
		
	}
$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip(); 
	$("#spinner_part1").hide();
});
</script>
<script src="js/vertical_tab.js"></script>
<?php include("footer.php"); ?>