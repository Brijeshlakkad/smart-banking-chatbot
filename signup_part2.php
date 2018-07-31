<?php include("header.php"); ?>
<?php 
if(isset($_POST['Username']))
{
$cookie_name = "Username";
$cookie_value = $_POST['Username'];
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); 
	?>
<div class="container well login_block" align="center">
	<div class="row center-block ">
		<div><caption><a href="index.php"><img src="images/jonsnow.png" class="img-responsive" style="margin-top:10px;width:250px;height:60px;float:center;filter:drop-shadow(0px 0px 3px #ffffff);"/></a></caption></div>
	</div>
	<div class="row" id="brij">
		<form ng-app="myapp" ng-controller="BrijController" name="signup2" method="post" enctype="multipart/form-data" action="file_upload.php"  novalidate>
		<div class="row">
			<span class="jon_header">Upload Documents</span>
			<hr style='background-color:#878787;width: 100px;height: 3px;'/>
		</div>
		<table class="myTable">
			<div class="form-group">
			<tr>
			<td><label for="file_tobe">Adhar Card/Pan Card/Driving Licience:</label><br></td>
			<td><input type="file" class="form-control" name="file_tobe" ng-model="file_tobe" required></td>
			<td>
			<span style="color:red" id="file_tobe" ng-show="signup2.file_tobe.$dirty && signup2.file_tobe.$invalid">
			<span ng-show="signup2.file_tobe.$error.required">File is required</span>
			</span>
			</td>
			</tr>
			</div>
			<tr>
			<td><input type="submit" id="submit_btn" value="Submit" class="btn btn-primary" ng-disabled="" /></td>
			<td id="status"><img src="images/small_loader.gif" id="spinner" style="height:30px;width:30px;" alt="Loading" /></td>
			<td></td>
			</tr>
		</table>
		</form>
	</div>
</div>
</div>

<script>
	var myApp = angular.module("myapp", []);
	myApp.controller("BrijController", function($scope,$http) {
	});
	
$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip(); 
	$("#spinner").hide();
});
</script>
	<?php
}
else
{
	header("location:unreachable.php");
}
?>

<?php include("footer.php"); ?>