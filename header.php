<?php include("functions.php"); ?>
<?php check_pages(); ?>
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
	<link rel="stylesheet" type="text/css" href="css/please_wait.css" />
	<script src="js/jquery.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/messages_functions.js"></script>
	<script src="js/angular.js"></script>
	<script type="text/javascript" src="js/bootstrap-show-password.min.js"></script>
</head>
<body>
<script>
$body = $("body");
$(document).on({
    ajaxStart: function() { $body.addClass("loading");    },
     ajaxStop: function() { $body.removeClass("loading"); }
});
</script>
<div class="please_wait_modal"></div>

<?php
	if(is_admin_logged_in())
	{
		?>

	<nav class="pages-nav">
		<div class="pages-nav__item adminid" id="<?php echo $_SESSION['Adminid']; ?>"><a class="link link--page remove-text-deco" href="admin_panel.php">Home</a></div>
		<div class="pages-nav__item">
		<div class="dropdown">
		<a class="dropdown-toggle link link--page remove-text-deco" data-toggle="dropdown" href="#">View
        <span class="caret"></span></a>
        <ul class="dropdown-menu">
			<li><a class="link" href="#" id="new_customers"><span class="c-social-media">New customers</span></a></li>
			<li><a class="link" href="#" id="approved_customers"><span class="c-social-media">Approved customers</span></a></li>
			<li><a class="link" href="#" id="rejected_customers"><span class="c-social-media">Rejected Customers</span></a></li>
		</ul>
		</div>
		</div>
		<div class="pages-nav__item"><a class="link link--page remove-text-deco" id="new_requests" href="#">New requests</a></div>
		<div class="pages-nav__item"><a class="link link--page remove-text-deco" id="new_feedbacks" href="#">New feedbacks</a></div>
		<div class="pages-nav__item">
		<div class="dropdown">
		<a class="dropdown-toggle link link--page remove-text-deco" data-toggle="dropdown" href="#">Settings
        <span class="caret"></span></a>
        <ul class="dropdown-menu">
			<li><a class="link" href="#"><span class="c-social-media">Profile</span></a></li>
			<li><a class="link" href="logout.php"><span class="c-social-media">Logout</span></a></li>
		</ul>
		</div>
		</div>
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
		<div class="pages-nav__item"><a class="link link--page remove-text-deco" style="font-size:10px;" href="contact.php">Contact</a></div>
	</nav>
		<?php
	}
	else
	{
		?>
		<nav class="pages-nav">
			<div class="pages-nav__item"><a class="link link--page remove-text-deco" href="index.php">Home</a></div>
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
		</nav>
		<nav class="pages-nav">
			<div class="pages-nav__item"><a class="link link--page remove-text-deco" style="font-size:10px;" href="contact.php">Contact</a></div>
		</nav>
		<?php
	}
	?>
