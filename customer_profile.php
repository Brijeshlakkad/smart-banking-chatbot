<?php include("header.php"); ?>
<?php check_session_for_admin(); ?>
<?php 
if(!isset($_POST['customer_id']))
{
	header("Location:unreachable.php");
}
else{
	$customer_id=$_POST['customer_id'];
?>
<div class="container" id="show_here" align="center">
	<div class="row"  ng-app="myapp" ng-controller="BrijController" style="margin-top: 20px;">
	{{username}}
	</div>
</div>
<script>
var myApp = angular.module("myapp", []);
	
	myApp.controller("BrijController", function($scope,$http) {
		$scope.genderOptions = [
				"Male","Female","Other"
			];
		var userid="<?php echo $customer_id; ?>";
		$scope.get_any_value=function(f,user,callback)
		{
			$http({
				method : "POST",
				url : "customer_interface.py",
				data: "get_data_id="+f+"&userid="+user,
				headers: {'Content-Type': 'application/x-www-form-urlencoded'}
			}).then(function mySuccess(response) {
				callback(response.data);
			}, function myError(response) {
			});
			
		};
		var set_val_username=function(val){
			$scope.username= val;
		};
		$scope.get_any_value("username",userid,set_val_username);
		var set_val_fname=function(val){
			$scope.fname= val;
		};
		$scope.get_any_value("fname",userid,set_val_fname);
		var set_val_lname=function(val){
			$scope.lname= val;
		};
		$scope.get_any_value("lname",userid,set_val_lname);
		var set_val_middle_name=function(val){
			$scope.middlename= val;
		};
		$scope.get_any_value("middle_name",userid,set_val_middle_name);
		var set_val_email=function(val){
			$scope.email= val;
		};
		$scope.get_any_value("email",userid,set_val_email);
		var set_val_contact=function(val){
			$scope.mobile= val;
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
	});
</script>
<?php
	}
include("footer.php"); ?>