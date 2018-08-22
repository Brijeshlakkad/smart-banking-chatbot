<?php
check_pages();
ini_set('error_reporting', -1);
ini_set('display_errors', 1);
ini_set('html_errors', 1);
include_once("config.php");
function get_customer_details($user)
{
	global $con;
	$sql="SELECT * FROM customers WHERE email='$user'";
	$result=mysqli_query($con,$sql);
	$row=mysqli_fetch_assoc($result);
	$login_username=$row['username'];
	$login_contact=$row['contact'];
	$login_fname=$row['fname'];
	$login_lname=$row['lname'];
	$login_middle_name=$row['middle_name'];
	$login_postal_add=$row['postal_add'];
	$login_perm_add=$row['perm_add'];
	$login_city=$row['city'];
	$login_state=$row['state'];
	$login_pincode=$row['pincode'];
	$login_gender=$row['gender'];
	$login_dob=$row['dob'];
}
mysqli_close($con);
?>
