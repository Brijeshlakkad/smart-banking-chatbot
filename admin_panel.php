<?php include("header.php"); ?>
<?php check_session(); ?>
<div class="container" id="show_here" align="center">

</div>
<script>
$(document).ready(function(){
	var get_table_of_details=function(flag)
	{
		$.ajax({
     		type: 'POST',
			url: 'admin_interface.py',
           	data: 'flag='+flag,
         	success  : function (data)
         	{
				$("#show_here").empty();
				$("#show_here").html(data);
         	}
			});
	};
	$("#new_customers").click(function(){
		get_table_of_details("new_customers");
	});
	$("#approved_customers").click(function(){
		get_table_of_details("approved_customers");
	});
	$("#rejected_customers").click(function(){
		get_table_of_details("rejected_customers");
	});
	$("#new_requests").click(function(){
		get_table_of_details("new_requests");
	});
	$("#new_feedbacks").click(function(){
		get_table_of_details("new_feedbacks");
	});
});
</script>
<?php include("footer.php"); ?>
