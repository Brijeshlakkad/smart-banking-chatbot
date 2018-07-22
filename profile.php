<?php include("header.php"); ?>
<div class="container-fluid my_well">
	<div class="row">
		<h2><b>Hello</b></h2>
		<br>
		This is brijesh.
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