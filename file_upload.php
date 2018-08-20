<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
if(!isset($_COOKIE["Username"])) {
    header("Location:unreachable.php");
} else {
$var_temp=$_COOKIE['Username'];
$var=trim($var_temp);
$allowedExts = array("jpeg", "jpg", "pdf");
$temp = explode(".", $_FILES["file_tobe"]["name"]);
$extension = end($temp);
if ((($_FILES["file_tobe"]["type"] == "application/pdf") || ($_FILES["file_tobe"]["type"] == "image/jpg") || ($_FILES["file_tobe"]["type"] == "image/jpeg"))
&& ($_FILES["file_tobe"]["size"] < 512000)
&& in_array($extension, $allowedExts))
  {
  if ($_FILES["file_tobe"]["error"] > 0)
    {
    echo "Return Code: " . $_FILES["file_tobe"]["error"] . "<br>";
    }
  else
    {
   if (!file_exists('customer_files/'.$var)) {
    mkdir('customer_files/'.$var, 0777, true);
   }
    if($_FILES["file_tobe"]["type"] == "image/jpg")
		  {
			  $ext="jpg";
		  }
		  else if($_FILES["file_tobe"]["type"] == "image/jpeg")
		  {
			  $ext="jpeg";
		  }
		  else if($_FILES["file_tobe"]["type"] == "application/pdf")
		  {
			  $ext="pdf";
		  }
		  else
		  {
			  header("Location:unreachable.php");
		  }
		$cfilename=$var.".".$ext;
		$path_to_file="customer_files/".$var."/";
		if(file_exists($path_to_file))
		{
			if(file_exists($path_to_file."".$var.".jpeg"))
				unlink($path_to_file."".$var.".jpeg");
			if(file_exists($path_to_file."".$var.".jpg"))
				unlink($path_to_file."".$var.".jpg");
			if(file_exists($path_to_file."".$var.".pdf"))
				unlink($path_to_file."".$var.".pdf");
		}
		move_uploaded_file($_FILES["file_tobe"]["tmp_name"],$path_to_file."".$cfilename);
		header("Location:signup_part3.php");
    }
  }
else
  {
  die("Invalid file or Bigger size");
  }
}
?>
