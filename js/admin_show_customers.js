$(document).ready(function(){
	$("#new_customers").click(function(){
		$.ajax({
     		type: 'POST', 
			url: 'admin_interface.py',
           	data: 'flag=new_customers',
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