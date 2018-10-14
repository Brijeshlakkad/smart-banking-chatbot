#!/usr/bin/python
import private_data
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
import random
from config import connect_to_database
class Mail:
	USERNAME = private_data.admin_email
	PASSWORD = private_data.admin_password
	def send_mail(self,user,sub,cont):
		SMTPserver = 'smtp.gmail.com'
		sender =    private_data.admin_email
		destination = user
		text_subtype = 'html'
		content=cont
		subject=sub
		try:
			msg = MIMEText(content, text_subtype)
			msg['Subject']= subject
			msg['From']   = sender
			conn = SMTP(SMTPserver)
			conn.set_debuglevel(False)
			conn.login(self.USERNAME, self.PASSWORD)
			try:
				conn.sendmail(sender, destination, msg.as_string())
				return "11"
			finally:
				conn.quit()
		except Exception:
			return "-99"
	def send_otp_mail(self,user):
		otp=""
		for i in range(0,6):
			otp+="%s"%(random.randint(0,9))
		sub="OTP"
		cont="Your OTP is: <b>%s</b>"%otp
		conn,cursor=connect_to_database()
		sql="update customers SET last_otp='%s' where email='%s'"%(otp,user)
		try:
			cursor.execute(sql)
			conn.commit()
			if self.send_mail(user,sub,cont)=="11":
				return otp
			return -99
		except:
			conn.rollback()
			return -99
		finally:
			conn.close()
