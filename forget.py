#!/usr/bin/python 
import sys
import os
import re
import private_data
from smtplib import SMTP_SSL as SMTP 
from email.mime.text import MIMEText
import cgi, cgitb 
form = cgi.FieldStorage() 
 
print("Content-type:text/html\r\n\r\n")
def send_forget_mail(forget_email,otp):
		SMTPserver = 'smtp.gmail.com'
		sender =   private_data.admin_email
		destination = forget_email
		USERNAME = private_data.admin_email
		PASSWORD = private_data.admin_password

		text_subtype = 'html'
		content="""\
		Forget Password OTP is : %s

		"""% (otp)
		subject="%s"% otp

		try:
			msg = MIMEText(content, text_subtype)
			msg['Subject']= subject
			msg['From']   = sender 
			conn = SMTP(SMTPserver)

			conn.set_debuglevel(False)
			conn.login(USERNAME, PASSWORD)
			try:
				conn.sendmail(sender, destination, msg.as_string())
				print("1")
			finally:
				conn.quit()
		except Exception:
			print("0")
if (form.getvalue('forget_email')):
	if form.getvalue('otp'):
		forget_email = form.getvalue('forget_email')
		otp = form.getvalue('otp')
		send_forget_mail(forget_email,otp)
else:
	print("0")