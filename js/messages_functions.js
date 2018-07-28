$(document).ready(function () {
		var $chatOutput = $("#chatOutput");
		var $chatRefresh = $("#chatRefresh");
		var userid=$("div.userid").attr("id");
		
		var reload_messages=function(){
			$.ajax({
				type: 'POST', 
				url: 'customer_interface.py',
				data: "reload_messages="+userid,
				success  : function (data)
				{
					$(document).ajaxStop(function(){
						if(data!="error")
						{
							$("#chatOutput").html(data);
							return;
						}
						else{
							$("#error_modal").modal("toggle");
							return;
						}
					});
				}
			});
			
		};
		$("#chatRefresh").click(function(){
			reload_messages();
		});
});