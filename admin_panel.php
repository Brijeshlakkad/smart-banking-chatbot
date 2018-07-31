<?php include("header.php"); ?>
<?php check_session_for_admin(); ?>
<div class="container" id="show_here" align="center">

</div>
<script>
$(document).ready(function(){
	$("#new_customers").click(function(){
		get_table_of_customer("new_customer");
	});
	$("#approved_customers").click(function(){
		get_table_of_customer("approved_customers");
	});
	$("#rejected_customers").click(function(){
		get_table_of_customer("rejected_customers");
	});
	var get_table_of_customer=function(flag)
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
});
</script>
<?php include("footer.php"); ?>