<?php
session_start();
function protect_anything($str)
{
	$str = addslashes($str);
	$str = stripslashes($str);
	return $str;
}
function check_session()
{
	if((!isset($_SESSION['Userid'])) && (!isset($_SESSION['Adminid'])))
	{
		header("Location:index.php");
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
function check_pages()
{
	$filename=basename($_SERVER['PHP_SELF']);
	if($filename=="index.php" || $filename=="login.php" || $filename=="signup.php")
	{
		if(isset($_SESSION['Userid']) || isset($_SESSION['Adminid']))
		{
			session_destroy();
			header("location:$filename");
		}
	}
	if(isset($_SESSION['Userid']))
	{
		if($filename=="profile.php" || $filename=="contact.php" || $filename=="profile_details.php" || $filename=="jon_snow.php")
		{

		}
		else{
			session_destroy();
			header("location:unreachable.php");
		}
	}
	if(isset($_SESSION['Adminid']))
	{
		if($filename=="admin.php" || $filename=="admin_panel.php" || $filename=="logout.php" || $filename=="customer_profile.php")
		{

		}
		else {
			session_destroy();
			header("location:unreachable.php");
		}
	}
}
?>
