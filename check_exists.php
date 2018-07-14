<?php
include("config.php");
if(isset($_POST['f']) && isset($_POST['q']))
{
	$f=$_POST['f'];
	$q=$_POST['q'];
	if($f=="s_email")
	{
		$email=$q;
		if($email=="")
		{
				echo "Email is required";
				return;
		}
		else if(!filter_var($email,FILTER_VALIDATE_EMAIL))
		{
				echo "Invalid email";
				return;
		}
		else
		{
					$sql="select * from customers where Email='$email'";
					$result=mysqli_query($con,$sql);
					if(!$result)
						die("Error");
					$ro=mysqli_num_rows($result);
					if($ro>0)
					{
						echo "Email already Exists";
						return;
					}
					else
					{
						echo "0";
						return;
					}
		}
	}
	if($f=="s_user")
	{
		$user=$q;
		if($user=="")
		{
				echo "Username is required";
				return;
		}
		else if(!filter_var($email,FILTER_VALIDATE_EMAIL))
		{
				echo "Invalid email";
				return;
		}
		else
		{
					$sql="select * from customers where Email='$email'";
					$result=mysqli_query($con,$sql);
					if(!$result)
						die("Error");
					$ro=mysqli_num_rows($result);
					if($ro>0)
					{
						echo "Email already Exists";
						return;
					}
					else
					{
						echo "0";
						return;
					}
		}
	}
}
mysqli_close($con);
?>