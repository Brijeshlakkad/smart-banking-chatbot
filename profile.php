<?php include_once("header.php"); ?>
<?php check_session(); ?>
<div class="container-fluid my_well">
	<div class="row" align="center">
		<h2 class="c_header">Jon Snow is here.</h2>
		<div class="row" style="margin-top: 20px;">
			<div class="row" style="margin: 50px;">
				Want Help?
			</div>
			<button class="btn btn-primary" >Ask questions to me >></button>
		</div>
	</div>
</div>
<div class="please_wait_modal"></div>
<script>
$body = $("body");
$(document).on({
    ajaxStart: function() { $body.addClass("loading");    },
     ajaxStop: function() { $body.removeClass("loading"); }    
});
</script>
<?php include("footer.php"); ?>