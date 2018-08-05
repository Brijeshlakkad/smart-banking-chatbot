#!/usr/bin/python
import config
import send_mail
import no_found
import customer_details
def verify_customer(userid,user,status):
	conn,cursor=config.connect_to_database()
	sql="update customers SET hasAcc='%s' where cid='%s'"%(status,userid)
	if type(status)!=int:
		status=int(status)
	sub="Verification of your Jon account"
	if status==1:
		cont="""<h1>Jon Snow</h1>,<br/><p>Your account is approved for banking and using of our services.</p>""";
	else:
		cont="""<h1>Jon Snow</h1>,<br/><p>We are sorry to hear that</p><br/></p><p>Your account is rejected.</p>""";
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
def provides_feedbacks():
	conn,cursor=config.connect_to_database()
	sql="select * from feedbacks"
	try:
		cursor.execute(sql)
		results=cursor.fetchall()
		num_row=int(cursor.rowcount)
		if num_row!=0:
			i=0
			feedbacks="""<div class="row" style="margin:20px;"><caption><h2>Feedbacks</h2></caption><table class='customerTable table-striped'><tr><td><b>Index no.</b></td><td><b>Email</b></td><td><b>Feedbacks</b></td><td><b>Time</b></td></tr>"""
			for row in results:
				f_id=row[0]
				email=row[1]
				f_text=row[2]
				time=row[3]
				i+=1
				feedbacks+="""<tr id='%s' style="cursor:pointer;"><td>%s</td><td><a class='btn btn-link' href='mailto:%s'>%s</a></td><td>%s</td><td>%s</td></tr>"""%(f_id,i,email,email,f_text,time)
			feedbacks+="</table></div>"
		else:
			feedbacks=no_found.no_found("We have not got any feedbacks, yet.")
		return feedbacks
	except:
		return "-99"
def provides_requests():
	conn,cursor=config.connect_to_database()
	sql="select * from requests"
	try:
		cursor.execute(sql)
		results=cursor.fetchall()
		num_row=int(cursor.rowcount)
		if num_row!=0:
			i=0
			requests="""<div class="row" style="margin:20px;"><caption><h2>Requests</h2></caption><table class='customerTable table-striped'><tr><td><b>Index no.</b></td><td><b>Account Number</b></td><td><b>Requesting</b></td><td><b>Time</b></td></tr>"""
			for row in results:
				r_id=row[0]
				acc_id=row[1]
				acc_no=customer_details.get_account_by_acc_id(acc_id,"acc_no")
				req=row[2]
				status=row[3]
				time=row[4]
				i+=1
				requests+="""<tr class='clickable-row' id='%s' style="cursor:pointer;"><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"""%(r_id,i,acc_no,req,time)
			requests+="</table></div>"
			requests+="""<script>$(".clickable-row").click(function() {
			var r_id=$(this).attr("id");
			alert(r_id);
			$(this).append("<form action='customer_profile.php' id='show_customer' method='post'><input type='text' name='request_id' value='"+r_id+"' /></form>");$("#show_customer").submit();
			}); 
			</script>"""
		else:
			requests=no_found.no_found("We have not got any feedbacks, yet.")
		return requests
	except:
		return "-99"