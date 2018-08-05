#!/usr/bin/python
import private_data
from smtplib import SMTP_SSL as SMTP 
from email.mime.text import MIMEText
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