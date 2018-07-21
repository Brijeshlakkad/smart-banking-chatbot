#!/usr/bin/python
import pymysql
import cgi, cgitb 
import sys
import os
import re
import private_data
import config
from smtplib import SMTP_SSL as SMTP 
from email.mime.text import MIMEText

class Mail:
	USERNAME = private_data.admin_email
	PASSWORD = private_data.admin_password
	def send_mail(self,email_ad):
		SMTPserver = 'smtp.gmail.com'
		sender =     private_data.admin_email
		destination = email_ad
		text_subtype = 'html'
		content="""\
		<b>Your Password has changed successfully.</b> <br>
		"""
		subject="Password Changed"
		try:
			msg = MIMEText(content, text_subtype)
			msg['Subject']= subject
			msg['From']   = sender 
			conn = SMTP(SMTPserver)
			conn.set_debuglevel(False)
			conn.login(self.USERNAME, self.PASSWORD)
			try:
				conn.sendmail(sender, destination, msg.as_string())
				print("1")
			finally:
				conn.quit()
		except Exception:
			print("0")

m=Mail()
form = cgi.FieldStorage()
print("Content-type:text/html\r\n\r\n")
conn,cursor=config.connect_to_database()
if form.getvalue('email'):
	email = form.getvalue('email')
if form.getvalue('npass'):
	npass = form.getvalue('npass')
sql="Update customers SET Password='%s' where Email='%s'" % (npass,email)
try:
	cursor.execute(sql)
	conn.commit()
	m.send_mail(email)
except:
	conn.rollback()
	print("0")
	
conn.close()