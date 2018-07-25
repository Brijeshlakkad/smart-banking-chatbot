<?php
include("config.php");
if(isset($_POST['u']) && isset($_POST['f']) && isset($_POST['q']))
{
	$f=$_POST['f'];
	$q=$_POST['q'];
	$u=$_POST['u'];
	if($f=="s_user")
	{
		$user=strtolower($q);
		$email=$u;
		if($user=="")
		{
				echo "Username is required";
				return;
		}
		else if(strlen($user)<=3)
		{
			echo "Username should contain more than 3 characters";
		}
		else
		{
					$sql="select * from customers where username='$user'";
					$result=mysqli_query($con,$sql);
					if(!$result)
						die("Error");
					$row=mysqli_fetch_assoc($result);
					$ro=mysqli_num_rows($result);
					if($ro>0 && $row['email']!=$email)
					{
						echo "Username already Exists";
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
else if(!isset($_POST['u']) && isset($_POST['f']) && isset($_POST['q']))
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
					$sql="select * from customers where email='$email'";
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
	else if($f=="s_user")
	{
		$user=$q;
		if($user=="")
		{
				echo "Username is required";
				return;
		}
		else if(strlen($user)<=3)
		{
			echo "Username should contain more than 3 characters";
		}
		else
		{
					$sql="select * from customers where username='$user'";
					$result=mysqli_query($con,$sql);
					if(!$result)
						die("Error");
					$ro=mysqli_num_rows($result);
					if($ro>0)
					{
						echo "Username already Exists";
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