<?php include("header.php"); ?>
<?php check_session(); ?>
<?php
if((!isset($_POST['customer_id'])) && (!isset($_POST['request_id'])))
{
	header("Location:unreachable.php");
}
else{
	$is_req=0;
	$customer_id=$_POST['customer_id'];
	if(isset($_POST['request_id']))
	{
		$request_id=$_POST['request_id'];
		$is_req=1;
	}
?>
<link rel="stylesheet" type="text/css" href="css/profile.css">
<style type="text/css">
		td{
	height: 20px;
	padding: 5px;
	font-family: Verdana, Geneva, sans-serif;
}
</style>
<div ng-app="myapp" ng-controller="BrijController" style="margin-top: 20px;" id="show_here">
	<div class="main">
	<center>
		<br>
		<br>
		<br>
		<div class="insidemain">
			<div class="insidemain1" >
				<img src="{{profile_pic_path}}" class="swing"/>
			</div>
			<div class="cont">
			 	<div class="text-block">
   					<p style="font-size:50px;font-family: Arial Black, Gadget, sans-serif;color: black;">{{fname}} {{lname}}</p>
   					<div class="buttons" ng-if="request_id=='-99'">
   						<button class="button" ng-click="take_action('1')" ng-if="hasAcc==0 || hasAcc==1" ng-disabled="hasAcc==1"><span>Approve</span></button>
						<button class="button" ng-click="take_action('-1')" ng-if="hasAcc==0 || hasAcc==-1" ng-disabled="hasAcc==-1"><span>Reject</span></button>
   					 </div>
						 <div class="buttons" ng-if="request_id!='-99'">
    						<button class="button" style="height:80px" ng-click="take_card_action('1')" ng-if="card_status==0 || card_status==1" ng-disabled="card_status==1"><span>Approve card request</span></button>
 						<button class="button" style="height:80px" ng-click="take_card_action('-1')" ng-if="card_status==0 || card_status==-1" ng-disabled="card_status==-1"><span>Reject Card request</span></button>
    					 </div>
  				</div>
  			</div>
  			<div style="width: 100%;margin-top: 50px;margin-right: 300px;height: 500px;">


				<div class="container" style="margin-left: 50px">

				  <ul class="nav nav-tabs">
				    <li class="active"><a data-toggle="tab" href="#home">Pesonal Details</a></li>
				   	 <li ng-if="hasAcc==1"><a data-toggle="tab" href="#menu1">Bank Account Deails</a></li>
						 <li ng-if="card_status==1"><a data-toggle="tab" href="#menu4">Card Deails</a></li>
				    <li><a data-toggle="tab" href="#menu2">Billing Details</a></li>
				    <li><a data-toggle="tab" href="#menu3">Documents</a></li>
				  </ul>

				  <div class="tab-content">
				    <div id="home" class="tab-pane fade in active">
				    	<div class="backOfDetails">
				   	 		<table>
				  					<tr>
				  						<td>Username</td><td></td></td><td class="td3">{{username}}</td>
				  					</tr>
				  					<tr>
				  						<td>Email</td><td></td><td class="td3">{{email}}</td>
				  					</tr>
				  					<tr>
				  						<td>FirstName</td><td></td><td class="td3">{{fname}}</td>
				  					</tr>
				  					<tr>
				  						<td>LastName</td><td></td><td class="td3">{{lname}}</td>
				  					</tr>
				  					<tr>
				  						<td>MiddleName</td><td></td><td class="td3">{{middlename}}</td>
				  					</tr>
				  					<tr>
				  						<td>Contact No.</td><td></td><td class="td3">{{contact}}</td>
				  					</tr>

				  					<tr>
				  						<td>DOB</td><td></td><td class="td3">{{dob}}</td>
				  					</tr>
				  					<tr>
				  						<td>Gender</td><td></td><td class="td3">{{gender}}</td>
				  					</tr>

				  				</table>
				  			</div>
				    </div>
				    <div id="menu1" class="tab-pane fade" ng-if="hasAcc==1">
				    	<div class="backOfDetails">
				      		<table>
				      			<tr>
				  					<td>Account Name</td><td></td><td class="td3">{{acc_name}}</td>
				  					</tr>
				  					<tr>
				  						<td>Account Number</td><td></td><td class="td3">{{acc_no}}</td>
				  					</tr>
				  					<tr>
				  						<td>Account Type</td><td></td><td class="td3">{{acc_type}}</td>
				  					</tr>

				      		</table>
				     	</div>
				    </div>
						<div id="menu4" class="tab-pane fade" ng-if="card_status==1">
				    	<div class="backOfDetails">
				      		<table>
				      			<tr>
				  					<td>Holder Name</td><td></td><td class="td3">{{holder_name}}</td>
				  					</tr>
				  					<tr>
				  						<td>Card Number</td><td></td><td class="td3">{{card_no}}</td>
				  					</tr>
				  					<tr>
				  						<td>Card Type</td><td></td><td class="td3">{{card_type}}</td>
				  					</tr>

				      		</table>
				     	</div>
				    </div>
				    <div id="menu2" class="tab-pane fade">
				    	<div class="backOfDetails">
				    		<table>
				      			<tr>
				  					<td>Postal Address</td><td></td><td class="td3">{{postal_add}}</td>
				  					</tr>
				  					<tr>
				  						<td>Permenent Address</td><td></td><td class="td3">{{perm_add}}</td>
				  					</tr>
				  					<tr>
				  						<td>City</td><td></td><td class="td3">{{city}}</td>
				  					</tr>
				  					<tr>
				  						<td>State</td><td></td><td class="td3">{{state}}</td>
				  					</tr>
				  					<tr>
				  						<td>Country</td><td></td><td class="td3">{{country}}</td>
				  					</tr>
				  					<tr>
				  						<td>Pincode</td><td></td><td class="td3">{{pincode}}</td>
				  					</tr>
				      		</table>
				    	</div>
				    </div>
				    <div id="menu3" class="tab-pane fade">
				      <h3>Document Uploaded by <small>{{fname}} {{lname}}</small></h3>
				      <div ng-if="file_path!=-1">
				      <a href="{{file_path}}" download>Adhar card/Driving Licence/Pan Card</a>
					  </div>
					  <div ng-if="file_path==-1">
			     	  <br/>
				      <h2>No documents found.</h2>
					  </div>
				    </div>
				  </div>
				</div>
  			</div>
		</div>
	</center>
	</div>
<div class="modal fade" id="success_modal" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>
        <div class="modal-body">
        <div class="alert alert-success">{{success_modal_val}}</div>
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
        <div class="alert alert-danger">{{error_modal_val}}</div>
        </div>
      </div>
    </div>
</div>
</div>
<script>
var myApp = angular.module("myapp", []);
myApp.controller("BrijController", function($scope,$http) {
		var req_available="<?php echo $is_req; ?>";
		$scope.request_id="-99";
		if(req_available==1)
		{
			$scope.request_id="<?php echo $request_id; ?>";
		}
		var userid="<?php echo $customer_id; ?>";
		$scope.get_any_value=function(f,user,callback)
		{
			$http({
				method : "POST",
				url : "admin_interface.py",
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
			$scope.contact= val;
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
		$scope.get_any_doc=function(f,user,callback)
		{
			$http({
				method : "POST",
				url : "admin_interface.py",
				data: "get_document="+f+"&userid="+user,
				headers: {'Content-Type': 'application/x-www-form-urlencoded'}
			}).then(function mySuccess(response) {
				callback(response.data);
			}, function myError(response) {
			});

		};
		var set_val_file=function(val){
			$scope.file_path= val;
		};
		$scope.get_any_doc("file",userid,set_val_file);
		var set_val_profile_pic=function(val){
			$scope.profile_pic_path= val;
		};
		$scope.get_any_doc("profile_pic",userid,set_val_profile_pic);
		$scope.get_acc_details=function(f,user,callback)
		{
			$http({
				method : "POST",
				url : "admin_interface.py",
				data: "get_acc_details="+f+"&userid="+user,
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
		$scope.take_action=function(value){
			if(value=="1"){
				var status=1;
				var con=prompt("Enter 'approve' to approve this customer a account.");
				if(con=='approve')
					{
						$http({
							method : "POST",
							url : "admin_interface.py",
							data: "verify_customer="+userid+"&status="+status,
							headers: {'Content-Type': 'application/x-www-form-urlencoded'}
						}).then(function mySuccess(response) {
							var flag=response.data;
							if(flag==11)
							{
								$scope.success_modal_val="Customer approved a bank account, successfully.";
								$("#success_modal").modal("show");
								setTimeout(function(){
									$("#success_modal").modal("hidden");
								},200);
							}else if(flag==-22){
								$scope.error_modal_val="Account already exists.";
								$("#error_modal").modal("show");
								setTimeout(function(){
									$("#error_modal").modal("hidden");
								},200);
							}else{
								$scope.error_modal_val="Try again! after a few minutes.";
								$("#error_modal").modal("show");
								setTimeout(function(){
									$("#error_modal").modal("hidden");
								},200);
							}
						}, function myError(response) {
						});
					}
			}
			else{
				var status=-1;
				var con=prompt("Enter 'reject' to approve this customer a account.");
				if(con=='reject')
					{
						$http({
							method : "POST",
							url : "admin_interface.py",
							data: "verify_customer="+userid+"&status="+status,
							headers: {'Content-Type': 'application/x-www-form-urlencoded'}
						}).then(function mySuccess(response) {
							var flag=response.data;
							if(flag==11)
							{
								$scope.success_modal_val="Customer rejected.";
								$("#success_modal").modal("show");
								setTimeout(function(){
									$("#success_modal").modal("hidden");
								},200);
							}else{
								$scope.error_modal_val="Try again! after a few minutes.";
								$("#error_modal").modal("show");
								setTimeout(function(){
									$("#error_modal").modal("hidden");
								},200);
							}
						}, function myError(response) {
						});
					}
			}
		};
		$scope.get_request_details=function(f,r_id,callback)
		{
			if(r_id!="-99")
			{
			$http({
				method : "POST",
				url : "admin_interface.py",
				data: "get_request_details="+f+"&r_id="+r_id,
				headers: {'Content-Type': 'application/x-www-form-urlencoded'}
			}).then(function mySuccess(response) {
				callback(response.data);
			}, function myError(response) {
			});
		}
		else {
			return "-99";
		}
		};
		var set_val_card_status=function(val){
			$scope.card_status= val;
		};
		$scope.get_request_details("status",$scope.request_id,set_val_card_status);
		$scope.get_card_details=function(f,userid,callback)
		{
			$http({
				method : "POST",
				url : "admin_interface.py",
				data: "get_card_details="+f+"&userid="+userid,
				headers: {'Content-Type': 'application/x-www-form-urlencoded'}
			}).then(function mySuccess(response) {
				callback(response.data);
			}, function myError(response) {
			});
		};
		var set_val_card_no=function(val){
			$scope.card_no= val;
		};
		$scope.get_card_details("card_no",userid,set_val_card_no);
		var set_val_holder_name=function(val){
			$scope.holder_name= val;
		};
		$scope.get_card_details("holder_name",userid,set_val_holder_name);
		var set_val_card_type=function(val){
		  $scope.card_type= val;
		};
		$scope.get_card_details("card_type",userid,set_val_card_type);
		$scope.take_card_action=function(value){
			var r_id=$scope.request_id;
			if(value=="1"){
				var status=1;
				var con=prompt("Enter 'approve' to approve this customer a account.");
				if(con=='approve')
					{
						$http({
							method : "POST",
							url : "admin_interface.py",
							data: "verify_card_request="+r_id+"&status="+status,
							headers: {'Content-Type': 'application/x-www-form-urlencoded'}
						}).then(function mySuccess(response) {
							var flag=response.data;
							if(flag==11)
							{
								$scope.success_modal_val="Customer card request approved, successfully.";
								$("#success_modal").modal("show");
								setTimeout(function(){
									$("#success_modal").modal("hidden");
								},200);
							}else{
								$scope.error_modal_val="Try again! after a few minutes.";
								$("#error_modal").modal("show");
								setTimeout(function(){
									$("#error_modal").modal("hidden");
								},200);
							}
						}, function myError(response) {
						});
					}
			}
			else{
				var status=-1;
				var con=prompt("Enter 'reject' to approve this customer a account.");
				if(con=='reject')
					{
						$http({
							method : "POST",
							url : "admin_interface.py",
							data: "verify_card_request="+r_id+"&status="+status,
							headers: {'Content-Type': 'application/x-www-form-urlencoded'}
						}).then(function mySuccess(response) {
							var flag=response.data;
							if(flag==11)
							{
								$scope.success_modal_val="Customer card request rejected.";
								$("#success_modal").modal("show");
								setTimeout(function(){
									$("#success_modal").modal("hidden");
								},200);
							}else{
								$scope.error_modal_val="Try again! after a few minutes.";
								$("#error_modal").modal("show");
								setTimeout(function(){
									$("#error_modal").modal("hidden");
								},200);
							}
						}, function myError(response) {
						});
					}
			}
		};
	});
</script>
<?php
}
include("footer.php"); ?>
