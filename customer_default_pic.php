<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
if(!isset($_COOKIE["Username"])) {
    header("Location:unreachable.php");
} else {
$var_temp=$_COOKIE['Username'];
$var=trim($var_temp);
$cfilename=$var.".png";
$path_to_file="customer_images/".$var."/";
copy('images/user.png', $path_to_file."".$cfilename);
$cookie_name = "To_access";
$cookie_value = $_COOKIE['Username'];
setcookie('Username', null, -1, '/');
setcookie($cookie_name, $cookie_value, time() + (10), "/");
header("Location:profile_set.php");
}
?>
