<?php include_once("header.php"); ?>
<?php check_session(); ?>
<div class="container-fluid my_well">
	<div class="row" align="center">
		<h2 class="c_header">Jon Snow is here.</h2>
		<div class="row" style="margin-top: 20px;">
			<div class="row" style="margin: 50px;">
				Want Help?
			</div>
			<a class="btn btn-primary" id="ask_question">Ask questions to me >></a>
		</div>
	</div>
</div>
<div class="modal fade" id="success_modal" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header"><h3>Have a great Jon day.</h3>
          <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>
        <div class="modal-body">
        <div class="alert alert-success">Jon service is started</div>
        </div>
      </div>
    </div>
</div>
<div class="modal fade" id="error_modal" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>
        <div class="modal-body">
        <div class="alert alert-danger">Please, try again after few minutes</div>
        </div>
      </div>
    </div>
</div>
<script>
$(document).ready(function(){
	var userid=$("div.userid").attr("id");
	var check_service=function(){
		$.ajax({
				type: 'POST', 
				url: 'customer_interface.py',
				data: 'check_service='+userid,
				success  : function (data)
				{
					$(document).ajaxStop(function(){
						if(data==0)
							{
								$("#ask_question").addClass("stopped").html("Start Jon service").removeAttr("href");
							}
						else if(data==1)
							{
								$("#ask_question").addClass("started").html("Ask questions to me >>").attr("href","jon_snow.php");
							}
						else
							{
								$("#ask_question").addClass("stopped").html("We are facing problem. Try again, after a few moments");
							}
						
						});
				}
				});
	};
	check_service();
	$("#ask_question").click(function(){
		var stopped=$(this).hasClass("stopped");
		var started=$(this).hasClass("started");
		if(stopped)
			{
				$.ajax({
				type: 'POST', 
				url: 'customer_interface.py',
				data: 'start_service='+userid,
				success  : function (data)
				{
					$(document).ajaxStop(function(){
						if(data==11)
							{
								$("#success_modal").modal("show");
								setTimeout(function(){
									$("#success_modal").modal("hide");
								},1000);
							}
						else
							{
								$("#error_modal").modal("show");
								setTimeout(function(){
									$("#error_modal").modal("hide");
								},1000);
							}
						});
					check_service();
				}
				});
			}
		else if(started)
			{
				
			}
	});
});
</script>
<?php include("footer.php"); ?>