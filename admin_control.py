#!/usr/bin/python
import config
import send_mail
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
