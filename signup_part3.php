<?php include("header.php");
error_reporting(E_ALL);
ini_set('display_errors', 1);
if(!isset($_COOKIE["Username"])) {
    header("Location:unreachable.php");
} else {
$username=trim($_COOKIE["Username"]);
	?>
<center>
<div class="container well login_block" align="center">
	<div class="row center-block ">
		<div><caption><a href="#"><img src="images/jonsnow.png" class="img-responsive" style="margin-top:10px;width:250px;height:60px;float:center;filter:drop-shadow(0px 0px 3px #ffffff);"/></a></caption></div>
	</div>
	<div class="row">
<form name="i_form" method="post" enctype="multipart/form-data" action="file_upload_img.php">
<table class="myTable">
	<tr>
	<div class="form-group">
		<td><label for="a_image" class="control-label">Profile picture</label></td>
		<td><input class="form-control" type="file" id="file" name="image" /></td>
		<td><p id="a_img"></p></td>
	</tr>
	<tr>
	<div class="form-group">
		<td></td><td><button class="btn btn-default form-control" type="button" id="uploadimage" onclick="check()">Upload Pic</button></td>
	</div>
	</tr>
	<tr>
		<td></td>
		<td><a class="btn btn-default form-control" type="button" href="customer_default_pic.php">Skip</a>

				</td>
	</tr>
</table>
</form>

<div id="image_preview">
	<img id="previewing" src="Images/noimage.png" alt="no image" />
</div>
</div>
</div>
</div>
</center>

<script>
	var myApp = angular.module("myapp", []);
	myApp.controller("BrijController", function($scope,$http) {
	});

$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
	$("#spinner").hide();
});
</script>
<script>
	function check()
	{
		var a = document.getElementById("a_img").innerHTML;
		var b = $("#file").val();
		if(b=="")
			{
				$("#a_img").html("<p style='color:red;'>Please select a valid Image File <br> Only jpeg, jpg and png images type allowed </p>");
			}
		else if(a=="" && b!="")
			document.i_form.submit();
	}
$(document).ready(function (e) {
$(function() {
$("#file").change(function() {
$("#a_img").empty();
var file = this.files[0];
var match= ["image/jpeg","image/png","image/jpg"];
if(!((file.type==match[0]) || (file.type==match[1]) || (file.type==match[2])))
{
$('#previewing').attr('src','../images/noimage.png');
$("#a_img").html("<p style='color:red;'>Please select a valid Image File <br> Only jpeg, jpg and png images type allowed </p>");
return false;
}
else
{
var reader = new FileReader();
reader.onload = imageIsLoaded;
reader.readAsDataURL(this.files[0]);
}
});
});
function imageIsLoaded(e) {
$("#file").css("color","green");
$('#image_preview').css("display", "block");
$('#previewing').attr('src', e.target.result);
$('#previewing').attr('width', '200px');
$('#previewing').attr('height', '180px');
};
});
</script>
	<?php
}
?>

<?php include("footer.php"); ?>
