<?php include("header.php"); ?>
<?php check_session_for_admin(); ?>
<?php 
if(!isset($_POST['customer_id']))
{
	header("Location:unreachable.php");
}
else{
?>
<div class="container" id="show_here" align="center">

</div>
<script>

</script>
<?php
	}
include("footer.php"); ?>