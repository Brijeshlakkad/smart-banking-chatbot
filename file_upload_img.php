<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
if(!isset($_COOKIE["Username"])) {
    header("Location:unreachable.php");
} else {
$var_temp=$_COOKIE['Username'];
$var=trim($var_temp);
$allowedExts = array("jpeg", "jpg","png");
$temp = explode(".", $_FILES["image"]["name"]);
$extension = end($temp);
if ((($_FILES["image"]["type"] == "image/jpg") || ($_FILES["image"]["type"] == "image/jpeg") || ($_FILES["image"]["type"] == "image/png"))
&& in_array($extension, $allowedExts))
  {
  if ($_FILES["image"]["error"] > 0)
    {
    echo "Return Code: " . $_FILES["image"]["error"] . "<br>";
    }
  else
    {
   if (!file_exists('customer_images/'.$var)) {
    mkdir('customer_images/'.$var, 0777, true);
   }
		if($_FILES["image"]["type"] == "image/jpg")
		  {
			  $ext="jpg";
		  }
		  else if($_FILES["image"]["type"] == "image/jpeg")
		  {
			  $ext="jpeg";
		  }
		  else if($_FILES["image"]["type"] == "image/png")
		  {
			  $ext="png";
		  }
		  else
		  {
			  header("Location:unreachable.php");
		  }
		$cfilename=$var.".".$ext;
		$path_to_file="customer_images/".$var."/";
		if(file_exists($path_to_file))
		{
			if(file_exists($path_to_file."".$var.".jpeg"))
				unlink($path_to_file."".$var.".jpeg");
			if(file_exists($path_to_file."".$var.".jpg"))
				unlink($path_to_file."".$var.".jpg");
			if(file_exists($path_to_file."".$var.".png"))
				unlink($path_to_file."".$var.".png");
		}
		move_uploaded_file($_FILES["image"]["tmp_name"],$path_to_file."".$cfilename);
		$cookie_name = "To_access";
		$cookie_value = $_COOKIE['Username'];
		setcookie('Username', null, -1, '/');
		setcookie($cookie_name, $cookie_value, time() + (10), "/");
		header("Location:profile_set.php");
    }
  }
else
  {
  die("Invalid file or Bigger size");
  }
}
?>
