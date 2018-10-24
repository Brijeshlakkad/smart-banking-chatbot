<?php include_once("header.php"); ?>
<?php check_session();
check_pages(); ?>

<script>  window.fbAsyncInit = function() {
    FB.init({
      appId            : '182961315923841',
      autoLogAppEvents : true,
      xfbml            : true,
      version          : 'v3.1'
    });
  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "https://connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));
</script>
<style>
.button {
    display: block;
    width: 100%;
		height: 50%;
		font-size: 21px;
}
.downArrow{
	position: relative;
	width: 20%;
}

.bounce {
	-moz-animation: bounce 3s infinite;
	-webkit-animation: bounce 3s infinite;
	animation: bounce 3s infinite;
}
@-moz-keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    -moz-transform: translateY(0);
    transform: translateY(0);
  }
  40% {
    -moz-transform: translateY(-30px);
    transform: translateY(-30px);
  }
  60% {
    -moz-transform: translateY(-15px);
    transform: translateY(-15px);
  }
}
@-webkit-keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }
  40% {
    -webkit-transform: translateY(-30px);
    transform: translateY(-30px);
  }
  60% {
    -webkit-transform: translateY(-15px);
    transform: translateY(-15px);
  }
}
@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    -moz-transform: translateY(0);
    -ms-transform: translateY(0);
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }
  40% {
    -moz-transform: translateY(-30px);
    -ms-transform: translateY(-30px);
    -webkit-transform: translateY(-30px);
    transform: translateY(-30px);
  }
  60% {
    -moz-transform: translateY(-15px);
    -ms-transform: translateY(-15px);
    -webkit-transform: translateY(-15px);
    transform: translateY(-15px);
  }
}
.customImg {
  border-radius: 50%;
}
</style>
<div class="container-fluid my_well">
	<div ng-app="myapp" ng-controller="BrijController" style="margin-top: 20px;">
	<div class="row" align="center">
		<div class="col-lg-4">
			<form name="transactionForm" novalidate>
			<div class="button btn btn-primary">
				<center>
			<div style="padding:30px;">
				<span>{{transaction_state_display}}</span>

				<table class="myTable">
			<tr><td><span><input type='text' name='acc_num' ng-change="check_acc_exists(acc_num)" ng-model="acc_num" placeholder="Enter Account Number" ng-style="acc_num_style" class="form-control" accnum-dir required/></span></td></tr>
			<tr><td><span style="color:black;font-size:15px;" ng-show="transactionForm.acc_num.$dirty && transactionForm.acc_num.$invalid">
				<span ng-show="transactionForm.acc_num.$error.required">Account number is required</span>
				<span ng-show="!transactionForm.acc_num.$error.required && transactionForm.acc_num.$error.accnumvalid">Please Enter Valid Account Number</span>
			</span>
			<span>{{show_acc_name}}</span></td></tr>
			<tr><td><span><input type='text' name='amount' ng-change="check_amount(amount)" ng-model="amount" placeholder="Enter Amount" ng-style="amount_style" class="form-control" amount-dir required /></span></td></tr>
			<tr><td><span style="color:black;font-size:15px;" ng-show="transactionForm.amount.$dirty && transactionForm.amount.$invalid">
			<span ng-show="transactionForm.amount.$error.required">Amount is required</span>
			<span ng-show="!transactionForm.amount.$error.required && transactionForm.amount.$error.amountvalid">Enter valid amount</span>
			<span ng-show="!transactionForm.amount.$error.required && transactionForm.amount.$error.amountrangevalid && !transactionForm.amount.$error.amountvalid">Enter amount less than 50,000 Rs.</span>
		</span></td></tr>
	</table>
		</div><br/><div class="downArrow bounce">
			<button type="submit" class="btn btn-default" ng-click="make_transaction()" ng-disabled="transactionForm.acc_num.$invalid || transactionForm.amount.$invalid">
  <img width="40" height="40" alt="" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/PjwhRE9DVFlQRSBzdmcgIFBVQkxJQyAnLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4nICAnaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkJz48c3ZnIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDMyIDMyIiBoZWlnaHQ9IjMycHgiIGlkPSLQodC70L7QuV8xIiB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCAzMiAzMiIgd2lkdGg9IjMycHgiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjxwYXRoIGQ9Ik0yNC4yODUsMTEuMjg0TDE2LDE5LjU3MWwtOC4yODUtOC4yODhjLTAuMzk1LTAuMzk1LTEuMDM0LTAuMzk1LTEuNDI5LDAgIGMtMC4zOTQsMC4zOTUtMC4zOTQsMS4wMzUsMCwxLjQzbDguOTk5LDkuMDAybDAsMGwwLDBjMC4zOTQsMC4zOTUsMS4wMzQsMC4zOTUsMS40MjgsMGw4Ljk5OS05LjAwMiAgYzAuMzk0LTAuMzk1LDAuMzk0LTEuMDM2LDAtMS40MzFDMjUuMzE5LDEwLjg4OSwyNC42NzksMTAuODg5LDI0LjI4NSwxMS4yODR6IiBmaWxsPSIjMTIxMzEzIiBpZD0iRXhwYW5kX01vcmUiLz48Zy8+PGcvPjxnLz48Zy8+PGcvPjxnLz48L3N2Zz4=" /></button>
</div></center></div>
</form>
</div>
<div class="col-lg-4">
<h2 class="c_header">Jon Snow is here!</h2>
<div class="row" style="margin-top: 20px;">
  <div class="row" style="margin: 50px;">
    <img src="images/jon-snow.jpg" alt="JonSnow" class="customImg" style="width:200px"><br/>
    <span style="font-size:20px;">Tell me if you need a bank assistance ;)</span>
  </div>
  <div class="fb-messengermessageus"
    messenger_app_id="182961315923841"
    page_id="354180721992855"
    size="xlarge">
  </div>
</div>

</div>
		<div class="col-lg-4">
      <div class="button btn btn-primary">
        <center>
    			<div style="padding:30px;">
    				<span>{{header_of_passbook}}</span>
            <div ng-bind-html="show_last_5_transaction" style="font-size:15px;" ng-click="show_more_transactions()"></div>
          </div>
        </center>
      </div>
</div>
</div>
<div class="modal fade" id="success_modal_scope" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>
        <div class="modal-body">
        <div class="alert alert-success"><div ng-bind-html="success_modal_val"></div></div>
        </div>
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
        <div class="alert alert-danger">{{error_modal_val}}</div>
        </div>
      </div>
    </div>
</div>
</div>
</div>
<script>
var myApp = angular.module("myapp", []);
user="<?php echo $_SESSION[Userid]; ?>";
myApp.controller("BrijController", function($scope,$http,$sce) {
	$scope.user="<?php echo $_SESSION[Userid]; ?>";
  $scope.header_of_passbook="Passbook";
	$scope.transaction_state_display="Send Money to";
	$scope.show_acc_name="";
	$scope.acc_num_style = {
		"border-width":"1.45px"
	};
  $scope.get_trans_num=2;
  $scope.get_last_transaction=function(num){
    var flag=1;
    $scope.get_trans_num=num;
    $http({
      method : "POST",
      url : "customer_interface.py",
      data: "get_last_transaction="+$scope.user+"&num_of_transactions="+$scope.get_trans_num,
      headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    }).then(function mySuccess(response) {
      flag = response.data;
      flag=flag.trim();
      if(flag.startsWith("11"))
      {
        $scope.last_trans_num=parseInt(flag.substr(2,2));
        $scope.show_last_5_transaction=$sce.trustAsHtml(flag.substr(4));
      }
      else {

      }
    }, function myError(response) {

    });
  };
  $scope.get_last_transaction($scope.get_trans_num);
  $scope.show_more_transactions=function()
  {
    if($scope.last_trans_num<$scope.get_trans_num)
    {
      $scope.success_modal_val=$sce.trustAsHtml("<b>You have reached maximum limit of transactions</b>");
      $("#success_modal_scope").modal("show");
      return;
    }
    else{
      $scope.get_trans_num+=2;
      $scope.get_last_transaction($scope.get_trans_num);
    }
  };
	$scope.check_acc_exists = function(value) {
						    var flag=1;
								$http({
									method : "POST",
									url : "customer_interface.py",
									data: "check_acc_num_exists="+value+"&user="+$scope.user,
									headers: {'Content-Type': 'application/x-www-form-urlencoded'}
								}).then(function mySuccess(response) {
									flag = response.data;
									flag=flag.trim();
									if(flag.startsWith("11"))
									{
										$scope.acc_num_style["border-color"] = "green";
										$scope.show_acc_name=flag.substr(2);
									}
									else {
											$scope.acc_num_style["border-color"] = "red";
									}
								}, function myError(response) {
									$scope.userStyle["border-color"] = "red";
								});
			};
			var patt_amount = new RegExp("^[0-9]+$");
			$scope.amount_style = {
				"border-width":"1.45px"
							};
			$scope.check_amount = function(value) {
							if(patt_amount.test(value) && value <= 50000 && value>0) {
									$scope.amount_style["border-color"] = "green";
							}else {
									$scope.amount_style["border-color"] = "red";
							}
					};
			$scope.make_transaction=function()
					{
								var flag=1;
								$http({
									method : "POST",
									url : "customer_interface.py",
									data: "make_transaction="+$scope.user+"&acc_num="+$scope.acc_num+"&amount="+$scope.amount,
									headers: {'Content-Type': 'application/x-www-form-urlencoded'}
								}).then(function mySuccess(response) {
									flag = response.data;
									flag=flag.trim();
                  if(flag==-22)
                  {
                    $scope.error_modal_val="You have inefficient balance";
                    $("#error_modal").modal("show");
                  }
									if(flag.startsWith("11"))
									{
										$scope.success_modal_val=$sce.trustAsHtml(flag.substr(2));
										$("#success_modal_scope").modal("show");
									}
									else {
                      $scope.error_modal_val="Please, try again after few minutes";
											$("#error_modal").modal("show");
									}
								}, function myError(response) {
                  $scope.error_modal_val="Please, try again after few minutes";
									$("#error_modal").modal("show");
								});
					};
});
myApp.directive('accnumDir', function($http) {
				return {
					require: 'ngModel',
					link: function(scope, element, attr, mCtrl) {
						function myValidation(value) {
							$http({
										method : "POST",
										url : "customer_interface.py",
										data: "check_acc_num_exists="+value+"&user="+user,
										headers: {'Content-Type': 'application/x-www-form-urlencoded'}
									}).then(function mySuccess(response) {
                    flag = response.data;
  									flag=flag.trim();
  									if(flag.startsWith("11"))
  									{
											mCtrl.$setValidity('accnumvalid', true);
										}
										else {
												mCtrl.$setValidity('accnumvalid', false);
										}
									}, function myError(response) {
										mCtrl.$setValidity('accnumvalid', false);
									});
							return value;
						}
						mCtrl.$parsers.push(myValidation);
					}
				};
});
myApp.directive('amountDir', function() {
				return {
					require: 'ngModel',
					link: function(scope, element, attr, mCtrl) {
						function myValidation(value) {
							var patt_amount = new RegExp("^[0-9]+$");
							if(patt_amount.test(value) && value>0) {
								mCtrl.$setValidity('amountvalid', true);
							}else {
								mCtrl.$setValidity('amountvalid', false);
							}
							if(value <= 50000 && value>0)
							{
								mCtrl.$setValidity('amountrangevalid', true);
						}else {
							mCtrl.$setValidity('amountrangevalid', false);
						}
							return value;
						}
						mCtrl.$parsers.push(myValidation);
					}
				};
});
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
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular-sanitize.js"></script>
<?php include("footer.php"); ?>
