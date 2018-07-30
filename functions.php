<?php
session_start();
function protect_anything($str)
{
	$str = addslashes($str);
	$str = stripslashes($str);
	return $str;
}
function check_signup_part2()
{
	
}
function check_session()
{
	if(!isset($_SESSION['Userid']))
	{
		header("Location:index.php");
	}
}
function check_session_for_admin()
{
	if(!isset($_SESSION['Adminid']))
	{
		header("location:admin.php");
	}
}
function is_logged_in()
{
	if(isset($_SESSION['Userid']))
	{
		return true;
	}
	else
	{
		return false;
	}
}
function is_admin_logged_in()
{
	if(isset($_SESSION['Adminid']))
	{
		return true;
	}
	else
	{
		return false;
	}
}
?>