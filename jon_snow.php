<?php include_once("header.php"); ?>

<link rel="stylesheet" type="text/css" href="css/chat.css" />
<div class="container">
	<div class="row well">
		<div class="chat_header_div row"><div class="col-lg-4"><span class="chat_header_text">Jon Snow <small style="font-size: 15px;">(The Bank Assistant)</small></span></div><div class="col-lg-1 pull-right"><button class="btn btn-primary"  id="chatRefresh"><span class="glyphicon glyphicon-refresh"></span></button></div></div>

		<div>
			<ul id="chatOutput" class="chat_container" style="list-style-type: none;">
			
			</ul>
		</div>
		<div class="row" ng-app="myapp" ng-controller="BrijController">
		<form name="chat_form" novalidate>
		<div class="col-lg-11">
			<input type="text" name="message" autocomplete="off" id="message" class="form-control" ng-model="message" placeholder="type here" required/></div>
		<div class="col-lg-1 pull-right">
			<button type="submit" id="send_message" class="btn" ng-disabled="chat_form.message.$invalid"><img src="images/send2.png" height="25" alt="send"/></button>
		</div>
		</form>
		</div>
	</div>
</div>

<script>
var myApp = angular.module("myapp", []);
myApp.controller("BrijController", function($scope,$http) {
	
	});
$(document).ready(function(){
	$("#chatRefresh").click();
	$("#send_message").click(function(){
		var message=$("#message").val();
		var userid=$("div.userid").attr("id");
		$.ajax({
				type: 'POST', 
				url: 'customer_interface.py',
				data: 'message='+message+"&user="+userid,
				success  : function (data)
				{
					$(document).ajaxStop(function(){
						if(data==11)
						{
							location.reload();
						}
					});
				}
			});
	});
	
});
</script>

<?php include_once("footer.php"); ?>