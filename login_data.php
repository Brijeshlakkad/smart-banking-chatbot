<?php
session_start();
include_once("functions.php");
include_once("config.php");
$email=protect_anything($_POST['l_email']);
$password=protect_anything($_POST['l_password']);
$sql="SELECT * FROM customers WHERE email='$email' AND password='$password'";
$result=mysqli_query($con,$sql);
$r=mysqli_num_rows($result);
$row=mysqli_fetch_assoc($result);
if($r==1)
{
	$_SESSION['Userid']=$row['email'];
	echo "1";
	return;
}
else
{
	echo "0";
	return;
}

?>