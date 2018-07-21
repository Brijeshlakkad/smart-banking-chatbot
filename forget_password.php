<?php
include("header.php");
$fmail="";
if(isset($_GET['femail']))
{
	$fmail=$_GET['femail'];
}
$otp="";
$numbers = range('0','9');
$max = count($numbers) - 1;
for ($i = 0; $i < 6; $i++) {
	$rand = rand(0, $max);
	$otp .= $numbers[$rand];
}
?>
<div class="container well login_block" align="center">
	<div class="row">
		<div><caption><a href="index.php"><a href="index.php"><img src="images/jonsnow.png" class="img-responsive" style="margin-top:10px;width:250px;height:60px;float:center;filter:drop-shadow(0px 0px 3px #ffffff);"/></a></caption></div>
	</div>
<div class="row" ng-app="myapp" ng-controller="BrijController">
<div id="email_sender">
<form  name="myForm" novalidate  method="post">
		<table class="myTable">
			<div class="form-group">
				<tr>
					<td><label for="forget_email">Email:</label></td>
					<td><input type="email" id="forget_email" class="form-control" name="forget_email" value="<?php echo $fmail; ?>" placeholder="Enter Email" ng-model="forget_email" required /></td>
				</tr>
				<tr>
					<td></td>
					<td>
						<span style="color:red"  ng-show="myForm.forget_email.$dirty && myForm.forget_email.$invalid"><span ng-show="myForm.forget_email.$error.required">Email is required.</span><span ng-show="myForm.forget_email.$error.email">Invalid email address.</span></span>
					</td>
				</tr>
				<tr>
					<td>
						<input hidden="hidden" id="otp" name="otp" value="<?php echo $otp; ?>"/>
					</td>
					<td></td>
				</tr>
				<tr>
					<td><img src="images/small_loader.gif" id="spinner1" style="height:30px;width: 30px;" alt="Loading" /><input class="btn btn-primary" id="send" ng-disabled="myForm.forget_email.$invalid" type="submit" value="submit" /></td>
					<td id="status1"></td>
				</tr>
			</div>
		</table>
</form>
</div>
<div id="otp_handler">
	<form name="otp_form" method="post">
		<table class="myTable">
			<div class="form-group">
				<tr>
					<td><label for="otp2">Enter OTP :</label></td>
					<td><input type="text" class="form-control" name="otp2" id="otp2" placeholder="Enter OTP" /></td>
					<td><img src="images/small_loader.gif" id="spinner2" style="height:30px;width: 30px;" alt="Loading" /><button class="btn btn-link" id="resend" >Resend</button></td>
				</tr>
				<tr>
					<td></td>
					<td><input class="btn btn-primary" id="varify" type="submit" value="submit" /></td>
					<td id="status2"></td>
				</tr>
			</div>
		</table>
	</form>
	
</div>

<div id="new_password">
	<form ng-controller="BrijController" name="myForm2" method="post">
		<table class="myTable">
			
				<div class="form-group">
					<tr>
					<td><label for="s_password">New Password:</label><br></td>
					<td><input  type="password" class="form-control" name="s_password" id="npass" placeholder="Enter Password"  ng-model="s_password" ng-style="passwordStrength" ng-change="analyze(s_password)" required pass-dir></td>
					<td><a class="badge my_badge" data-toggle="tooltip" data-placement="top" title="Password should contain at least one number and at least one character">?</a>
					<span style="color:red" id="s_password" ng-show="myForm2.s_password.$dirty && myForm2.s_password.$invalid">
					<span ng-show="myForm2.s_password.$error.required">Password is required</span>
					<span ng-show="!myForm2.s_password.$error.required && myForm2.s_password.$error.passvalid">Invalid Password</span>
					</span>
					</td>
					</tr>
					</div>
					<div class="form-group">
					<tr>
					<td><label for="s_cpassword">Confirm New Password:</label><br></td>
					<td><input ng-disabled="!myForm2.s_password.$valid" type="password" class="form-control" name="s_cpassword" placeholder="Enter Confirm Password"  ng-model="s_cpassword" ng-style="cpassStyle" ng-change="analyze2(s_cpassword,s_password)" onkeyup="check_pass(this.value)" required cpass-dir></td>
					<td>
					<span style="color:red" id="s_cpassword" ng-show="myForm2.s_cpassword.$dirty">
					<span ng-show="myForm2.s_cpassword.$error.required && myForm2.s_cpassword.$invalid">Password is required.</span>
					</span>
					</td>
					</tr>
					</div>
				<div class="form-group">
				<tr>
					<td></td>
					<td><img src="images/small_loader.gif" id="spinner3" style="height:30px;width: 30px;" alt="Loading" /><input class="btn btn-primary" id="change_pass" ng-disabled=" myForm2.s_password.$invalid ||  myForm2.s_cpassword.$invalid" type="submit" value="submit" /></td>
					<td id="status3"></td>
					<td></td>
				</tr>
			</div>
		</table>
	</form>
</div>
</div>
</div>

<script>
	var otp;
	var email;
$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip(); 
	
	$("#otp_handler").hide();
	$("#new_password").hide();
	
	$("#spinner1").hide();
	$("#spinner2").hide();
	$("#spinner3").hide();
	$("#forget_email").focus();
	$('#send').click(function(e){
    e.preventDefault();
		email=document.myForm.forget_email.value;
		varify_email(email);
		
	});
	$('#resend').click(function(e){
    e.preventDefault();
		send_OTP('1');
	});
	$('#change_pass').click(function(e){
    e.preventDefault();
		get_old_pass(email);
	});
	
	$("#varify").click(function(e){
		e.preventDefault();
		var otp2=$("#otp2").val();
		if(otp == otp2)
			{
				$("#email_sender").hide();
				$("#otp_handler").hide();
				$("#new_password").show();
				$("#npass").focus();
			}
		else
			{
				$("#status2").html("<b style='color:red;'>Wrong OTP</b>");
			}
	});
	
	// this is not required
	$('#spinner').bind("ajaxSend", function() {
        $(this).show();
    }).bind("ajaxComplete", function() {
        $(this).hide();
    });
});
function varify_email(f_email)
	{
			var x=new XMLHttpRequest();
			x.onreadystatechange=function(){
				if(this.readyState==4 && this.status==200)
					{
						var data=this.responseText;
						if(data==1)
							document.getElementById("status1").innerHTML="<span style='color:red;'>Please enter registered email</span>";
						else
							send_OTP('0');
					}
			};
			x.open("POST","check_exists.php",true);
			x.setRequestHeader("Content-type","application/x-www-form-urlencoded");
			x.send("f=f_email&q="+f_email);
	}
function send_OTP(s)
	{
		email=document.myForm.forget_email.value;
		otp=document.myForm.otp.value;
		var x=new XMLHttpRequest();
		x.onreadystatechange=function(){
			if(x.readyState==1 || x.readyState==2 || x.readyState==3)
				{
					if(s==1)
						{
							$("#resend").hide();
							$("#spinner2").show();
							$("#varify").hide(); // to avoid being show two panel
						}
					if(s==0)
						{
							$("#spinner1").show();
							$("#send").hide();
							$("#status1").empty();
							$("#status1").html("<p>Sending OTP..</p>");
						}
				}
			else if(x.readyState==4 && x.status==200)
			{
				var data=this.responseText;
				if(s==1)
						{
							$("#resend").show();
							$("#spinner2").hide();
							$("#varify").show();
							if(data==1)
								{
									$("#email_sender").hide();
									$("#otp_handler").show();
									
								}
							else
								{
									$("#status2").html("<b style='color:red;'>Error: unable to send email</b>");
								}
						}
				if(s==0)
					{
						$("#send").show();
						$("#spinner1").hide();
						if(data==1)
							{
								$("#email_sender").hide();
								$("#otp_handler").show();
							}
						else
							{
								$("#status1").html("<b style='color:red;'>Error: unable to send email</b>");
							}
					}
					$("#otp2").focus();
				
			}
		};
		x.open("POST","forget.py",true);
		x.setRequestHeader("Content-type","application/x-www-form-urlencoded");
		x.send("forget_email="+email+"&otp="+otp);
	}
	/*
function check_password(field,val)
	{
		if(field=="cnpass")
			{
				var pass=pass_form.npass.value;
				if(val != pass)
					document.getElementById(field).innerHTML="Passwords do not match";
				else
					document.getElementById(field).innerHTML="";
			}
		else{
			var x=new XMLHttpRequest();
			x.onreadystatechange=function(){
				if(this.readyState==4 && this.status==200)
					{
						document.getElementById(field).innerHTML=this.responseText;
					}
			};
			x.open("POST","ajax_signp_validation.php",true);
			x.setRequestHeader("Content-type","application/x-www-form-urlencoded");
			x.send("q="+val+"&f=s_password");
		}
	}*/
function get_old_pass(f_email)
	{
		var pass=myForm2.s_password.value;
		var cpass=myForm2.s_cpassword.value;
		var x=new XMLHttpRequest();
			x.onreadystatechange=function(){
				if(this.readyState==4 && this.status==200)
					{
						$("#status3").empty();
						var data=this.responseText;
						if(data==0)
							{
							change_password(pass,cpass);
							}
						else
							{
							document.getElementById("status3").innerHTML="<span style='color:red;'>Please enter different password</span>";
							}
							
					}
			};
			x.open("POST","check_exists.php",true);
			x.setRequestHeader("Content-type","application/x-www-form-urlencoded");
			x.send("f=f_pass&q="+pass+"&f_email="+f_email);
	}
function change_password(pass,cpass)
	{
			var x=new XMLHttpRequest();
			x.onreadystatechange=function(){
				if(x.readyState==1 || x.readyState==2 || x.readyState==3)
				{
					$("#spinner3").show();
				}
				if(this.readyState==4 && this.status==200)
					{
						$("#change_pass").show();
						$("#spinner3").hide();
						var data=this.responseText;
						if(data==0)
							{
								$("#status3").html("Please, Try again !");
							}
						else if(data==1)
							{
								window.location="login.php";
							}
					}
			};
			x.open("POST","change_password.py",true);
			x.setRequestHeader("Content-type","application/x-www-form-urlencoded");
			x.send("email="+email+"&npass="+pass);
	}
	var myApp = angular.module("myapp", []);
	myApp.controller("BrijController", function($scope) {
                var strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
                var mediumRegex = new RegExp("^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})");
                $scope.passwordStrength = {
					"border-width":"1.45px"
                };
                $scope.analyze = function(value) {
                    if(strongRegex.test(value)) {
                        $scope.passwordStrength["border-color"] = "green";
                    } else if(mediumRegex.test(value)) {
                        $scope.passwordStrength["border-color"] = "orange";
                    } else {
                        $scope.passwordStrength["border-color"] = "red";
                    }
                };
				$scope.cpassStyle = {
					"border-width":"1.45px"
                };
                $scope.analyze2 = function(value1,value2) {
                    if(value1 == value2 && value2.length!=0) {
                        $scope.cpassStyle["border-color"] = "green";
                    }
					else {
                        $scope.cpassStyle["border-color"] = "red";
                    }
                };
	});
	myApp.directive('passDir', function() {
				return {
					require: 'ngModel',
					link: function(scope, element, attr, mCtrl) {
						function myValidation(value) {
							var patt=new RegExp("^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})");
							if (patt.test(value)) {
								mCtrl.$setValidity('passvalid', true);
							} else {
								mCtrl.$setValidity('passvalid', false);
							}
							return value;
						}
						mCtrl.$parsers.push(myValidation);
					}
				};
});
	function check_pass(cpass)
	{
		var pass=myForm2.s_password.value;
		
		if(pass!=cpass && cpass!="")
			$("#s_cpassword").html("Passwords do not match");
		else if(cpass=="")
			$("#s_cpassword").html("Password is required");
		else
			$("#s_cpassword").html("");
	}
</script>

</body>
</html>