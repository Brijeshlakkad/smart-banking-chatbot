#!/usr/bin/python
import config
import send_mail
import no_found
import customer_details
import random
import string
from datetime import datetime
def check_account_exists(userid):
	conn,cursor=config.connect_to_database()
	sql="select * from accounts where c_id='%s'"%userid
	try:
		cursor.execute(sql)
		num_row=cursor.rowcount
		if num_row==0:
			return "11"
		else:
			return "-22"
	except:
		return "-99"
def create_acc_name(userid):
	fname=customer_details.get_any_value_by_id(userid,"fname")
	lname=customer_details.get_any_value_by_id(userid,"lname")
	middlename=customer_details.get_any_value_by_id(userid,"middle_name")
	return fname+" "+middlename+" "+lname
def create_acc_no(userid):
	contact=customer_details.get_any_value_by_id(userid,"contact")
	return "00"+str(contact)
def create_bank_account_details(userid):
	conn,cursor=config.connect_to_database()
	check=check_account_exists(userid)
	if check=="-22":
		return "-22"
	elif check=="-99":
		return "-99"
	acc_name=create_acc_name(userid)
	acc_no=create_acc_no(userid)
	acc_type="saving"
	sql="insert into accounts(c_id,acc_name,acc_type,acc_no) values('%s','%s','%s','%s')"%(userid,acc_name,acc_type,acc_no)
	try:
		cursor.execute(sql)
		conn.commit()
		return "11"
	except:
		conn.rollback()
		return "-99"
def create_cvv():
	return ''.join([random.choice(string.digits) for n in xrange(3)])
def create_card_no():
	return random.randint(1111111111111111,9999999999999999)
def create_card(acc_id):
	conn,cursor=config.connect_to_database()
	c_id=customer_details.get_account_by_acc_id(acc_id,"c_id")
	holder_name=customer_details.get_account_by_acc_id(acc_id,"acc_name")
	card_type="Mastercard"
	till_month=datetime.now().strftime('%m')
	till_year=str((int(datetime.now().year+1))%100).zfill(2)
	cvv=create_cvv()
	card_no=create_card_no()
	sql="insert into cards(c_id,acc_id,holder_name,till_month,till_year,csv,card_type,card_no) values('%s','%s','%s','%s','%s','%s','%s','%s')"%(c_id,acc_id,holder_name,till_month,till_year,cvv,card_type,card_no)
	try:
		cursor.execute(sql)
		conn.commit()
		return "11"
	except:
		conn.rollback()
		return "-99"
def verify_customer(userid,user,status):
	sql="update customers SET hasAcc='%s' where cid='%s'"%(status,userid)
	if type(status)!=int:
		status=int(status)
	sub="Verification of your Jon account"
	if status==1:
		bit=create_bank_account_details(userid)
		bit=str(bit)
		if bit=="-99":
			return "-99"
		elif bit=="-22":
			return "-22"
		cont="""<h1>Jon Snow</h1>,<br/><p>Your account has approved for banking and using of our services.</p>""";
	else:
		cont="""<h1>Jon Snow</h1>,<br/><p>We are sorry to hear that</p><br/></p><p>Your account is rejected.</p>""";
	conn,cursor=config.connect_to_database()
	try:
		cursor.execute(sql)
		m=send_mail.Mail()
		st=m.send_mail(user,sub,cont)
		st=str(st)
		if st=="11":
			conn.commit()
			return "11"
		else:
			conn.rollback()
			return "-99"
	except:
		conn.rollback()
		return "-99"
def verify_card_request(r_id,acc_id,status):
	sql="update requests SET status_bit='%s' where r_id='%s'"%(status,r_id)
	user=customer_details.get_account_by_acc_id(acc_id,"email")
	if type(status)!=int:
		status=int(status)
	sub="Verification of your card request"
	if status==1:
		bit=create_card(acc_id)
		bit=str(bit)
		if bit=="-99":
			return "-99"
		elif bit=="-22":
			return "-22"
		cont="""<h1>Jon Snow</h1>,<br/><p>Your card request has approved for banking and using of our services.</p>""";
	else:
		cont="""<h1>Jon Snow</h1>,<br/><p>We are sorry to hear that</p><br/></p><p>Your account is rejected.</p>""";
	conn,cursor=config.connect_to_database()
	try:
		cursor.execute(sql)
		m=send_mail.Mail()
		st=m.send_mail(user,sub,cont)
		conn.commit()
		return "11"
	except:
		conn.rollback()
		return "-99"
	finally:
		conn.close()
def provides_feedbacks():
	conn,cursor=config.connect_to_database()
	sql="select * from feedbacks"
	try:
		cursor.execute(sql)
		results=cursor.fetchall()
		num_row=int(cursor.rowcount)
		if num_row!=0:
			i=0
			feedbacks="""<div class="row" style="margin:20px;"><caption><h2>Feedbacks <button class="btn btn-primary" id="feedback_refresh"><span class="glyphicon glyphicon-refresh"></span></button></h2></caption><table class='customerTable table-striped'><tr><td><b>Index no.</b></td><td><b>Email</b></td><td><b>Feedbacks</b></td><td><b>Time</b></td></tr>"""
			for row in results:
				f_id=row[0]
				email=row[1]
				f_text=row[2]
				time=row[3]
				i+=1
				feedbacks+="""<tr id='%s' style="cursor:pointer;"><td>%s</td><td><a class='btn btn-link' href='mailto:%s'>%s</a></td><td>%s</td><td>%s</td></tr>"""%(f_id,i,email,email,f_text,time)
			feedbacks+="""</table></div>
			<script>
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
			$("#feedback_refresh").click(function(){
				get_table_of_details("new_feedbacks");
			});
			</script>"""
		else:
			feedbacks=no_found.no_found("We have not got any feedbacks, yet.")
		return feedbacks
	except:
		return "-99"
def provides_requests():
	conn,cursor=config.connect_to_database()
	sql="select * from requests ORDER BY created_time DESC"
	try:
		cursor.execute(sql)
		results=cursor.fetchall()
		num_row=int(cursor.rowcount)
		if num_row!=0:
			i=0
			requests="""<div class="row" style="margin:20px;"><caption><h2>Requests <button class="btn btn-primary" id="request_refresh"><span class="glyphicon glyphicon-refresh"></span></button></h2></caption><table class='customerTable table-striped'><tr><td><b>Index no.</b></td><td><b>Account Number</b></td><td><b>Account Name</b></td><td><b>Requesting</b></td><td><b>Time</b></td></tr>"""
			for row in results:
				r_id=row[0]
				acc_id=row[1]
				acc_no=customer_details.get_account_by_acc_id(acc_id,"acc_no")
				acc_name=customer_details.get_account_by_acc_id(acc_id,"acc_name")
				c_id=customer_details.get_account_by_acc_id(acc_id,"c_id")
				req=row[2]
				status=row[3]
				time=row[4]
				i+=1
				profile_link="""<a class='btn btn-link' id='profile_link'>%s</a>"""%acc_name
				requests+="""<tr class='clickable-row' id='%s' style="cursor:pointer;"><td>%s</td><td id='%s' class='c_id'>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"""%(r_id,i,c_id,acc_no,profile_link,req,time)
			requests+="</table></div>"
			requests+="""<script>
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
			$("#request_refresh").click(function(){
				get_table_of_details("new_requests");
			});
			$(".clickable-row").click(function() {
			var r_id=$(this).attr("id");
			var c_id=$(this).children("td.c_id").attr("id");
			$(this).append("<form action='customer_profile.php' id='show_customer' method='post'><input type='hidden' name='request_id' value='"+r_id+"' /><input type='hidden' name='customer_id' value='"+c_id+"' /></form>");
			$("#show_customer").submit();
			});
			</script>"""
		else:
			requests=no_found.no_found("We have not got any feedbacks, yet.")
		return requests
	except:
		return "-99"
def delete_customer_card(field,value):
	conn,cursor=config.connect_to_database()
	sql="delete from cards where %s='%s'"%(field,value)
	try:
		cursor.execute(sql)
		conn.commit()
		return 11
	except:
		conn.rollback()
		return -99
	finally:
		conn.close()
def change_customer_details(field,value,user):
	column_value=['postal_add','username','contact',"passcode","password"]
	conn,cursor=config.connect_to_database()
	if field=="username" or field=="contact":
		sql="select email from customers where %s='%s'"%(field,value)
		try:
			cursor.execute(sql)
			if cursor.rowcount!=0:
				row=cursor.fetchone()
				if user!=row[0]:
					return -11
		except:
			return -99
	if field=="passcode":
		cid=customer_details.get_any_value(user,"cid")
		table_name="accounts"
		condition="c_id='%s'"%cid
	else:
		table_name="customers"
		condition="email='%s'"%user
	sql="update %s SET %s='%s' where %s"%(table_name,field,value,condition)
	try:
		cursor.execute(sql)
		conn.commit()
		return 1
	except:
		conn.rollback()
		return -99
	finally:
		conn.close()
def delete_customer_request(acc_id,card_req):
	conn,cursor=config.connect_to_database()
	sql="delete from requests where acc_id='%s' and card_loan='%s'"%(acc_id,card_req)
	try:
		cursor.execute(sql)
		conn.commit()
		return 11
	except:
		conn.rollback()
		return -99
	finally:
		conn.close()
