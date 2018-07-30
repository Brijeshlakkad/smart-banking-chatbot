$(document).ready(function(){
	$("#new_customers").click(function(){
		$.ajax({
     		type: 'POST', 
			url: 'show_new_customers.php',
           	data: 'flag=updated',
         	success  : function (data)
         	{
				$("#show_here").empty();
				$("#show_here").html(data);
         	}
			});
	});
	$("#approved_customers").click(function(){
		
	});
	$("#rejected_customers").click(function(){
		
	});
});