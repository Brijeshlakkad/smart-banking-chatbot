<?php
if(!isset($_COOKIE["User_cid"])) {
    header("Location:unreachable.php");
} else {
$var_temp=$_COOKIE['User_cid'];
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
   if (!file_exists('Files/'.$var)) {
    mkdir('Files/'.$var, 0777, true);
   }
    if (file_exists("Files/".$var."/" . $_FILES["file_tobe"]["name"]))
      {
      echo $_FILES["file_tobe"]["name"] . " already exists. ";
      }
    else
      {
      move_uploaded_file($_FILES["file_tobe"]["tmp_name"],"Files/$var"."/" . $_FILES["file_tobe"]["name"]);
      header("Location:signup_part3.php");
      }
    }
  }
else
  {
  die("Invalid file or Bigger size");
  }
}
?>