<?php include("functions.php"); ?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Jon Assistant</title>
	<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
	<link href="css/custom.css" rel="stylesheet" media="screen">
	<link rel="stylesheet" href="css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="css/component.css" />
	<link rel="stylesheet" type="text/css" href="css/please_wait2.css" />
	<script src="js/jquery.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/angular.js"></script>
	<script type="text/javascript" src="js/bootstrap-show-password.min.js"></script>
</head>
<body>
<div class="please_wait_modal"></div>
<script>
$body = $("body");
$(document).on({
    ajaxStart: function() { $body.addClass("loading");    },
     ajaxStop: function() { $body.removeClass("loading"); }    
});
</script>
<style>
	.custom_nav{
		position: fixed;
		top: 0px;
		left: 0px;
		right: 0px;
		width: 100%;
	}
</style>
<?php 
	if(!is_logged_in())
	{
	?>
	<nav class="pages-nav custom_nav">
	<div class="pages-nav__item"></div>
		<div class="pages-nav__item"><a class="link link--page remove-text-deco" href="index.php" >Home</a></div>
		<div class="pages-nav__item">
		<div class="dropdown">
		<a class="dropdown-toggle link link--page remove-text-deco" data-toggle="dropdown" href="#">Social links
        <span class="caret"></span></a>
        <ul class="dropdown-menu">
			<li><a class="link" href="#"><span class="c-social-media">Twitter</span></a></li>
			<li><a class="link" href="#"><span class="c-social-media">LinkedIn</span></a></li>
			<li><a class="link" href="#"><span class="c-social-media">Facebook</span></a></li>
			<li><a class="link" href="#"><span class="c-social-media">YouTube</span></a></li>
		</ul>
		</div>
		</div>
		<div class="pages-nav__item"><a class="link link--page remove-text-deco" href="login.php">Login/Signup</a></div>
		<div class="pages-nav__item pages-nav__item--small"></div>
		<div class="pages-nav__item pages-nav__item--small"></div>
		<div class="pages-nav__item pages-nav__item--small"><a class="link link--page link--faded remove-text-deco" href="contact.php">Contact</a></div>
		<div class="pages-nav__item pages-nav__item--small"></div>
	</nav>
	
	<?php 
	}
	else if(is_logged_in())
	{
		?>
	<nav class="pages-nav">
		<div class="pages-nav__item userid" id="<?php echo $_SESSION['Userid']; ?>"><a class="link link--page remove-text-deco" href="profile.php">Home</a></div>
		<div class="pages-nav__item">
		<div class="dropdown">
		<a class="dropdown-toggle link link--page remove-text-deco" data-toggle="dropdown" href="#">Social links
        <span class="caret"></span></a>
        <ul class="dropdown-menu">
			<li><a class="link" href="#"><span class="c-social-media">Twitter</span></a></li>
			<li><a class="link" href="#"><span class="c-social-media">LinkedIn</span></a></li>
			<li><a class="link" href="#"><span class="c-social-media">Facebook</span></a></li>
			<li><a class="link" href="#"><span class="c-social-media">YouTube</span></a></li>
		</ul>
		</div>
		</div>
		<div class="pages-nav__item">
		<div class="dropdown">
		<a class="dropdown-toggle link link--page remove-text-deco" data-toggle="dropdown" href="#">Settings
        <span class="caret"></span></a>
        <ul class="dropdown-menu">
			<li><a class="link" href="profile_details.php"><span class="c-social-media">Profile</span></a></li>
			<li><a class="link" href="logout.php"><span class="c-social-media">Logout</span></a></li>
		</ul>
		</div>
		</div>
	</nav>
	<nav class="pages-nav">
		<div class="pages-nav__item pages-nav__item--small"><a class="link link--page link--faded remove-text-deco" href="contact.php">Contact</a></div>
	</nav>
		<?php
	}
	?>
	
