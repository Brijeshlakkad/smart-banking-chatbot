#!/usr/bin/python
import pymysql
import cgi, cgitb
import sys
import os
import re
import private_data
import config
import customer_details
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

class Mail:
	USERNAME = private_data.admin_email
	PASSWORD = private_data.admin_password
	def send_mail(self,email_ad,mob,name):
		SMTPserver = 'smtp.gmail.com'
		sender =    private_data.admin_email
		destination = email_ad
		text_subtype = 'html'
		content="""\
		<b>Welcome to the Jon Snow (The Assistant)</b> <br> \
		dear %s ,<br> \
			You have registered your email address successfully <br> \
			Your Mobile number %s <br> \
		""" % (name,mob)
		subject="Sign up successfully"
		try:
			msg = MIMEText(content, text_subtype)
			msg['Subject']= subject
			msg['From']   = sender
			conn = SMTP(SMTPserver)
			conn.set_debuglevel(False)
			conn.login(self.USERNAME, self.PASSWORD)
			try:
				conn.sendmail(sender, destination, msg.as_string())
			finally:
				conn.quit()
		except Exception:
			print("0")

m=Mail()
form = cgi.FieldStorage()
conn,cursor=config.connect_to_database()
print("Content-type:text/html\r\n\r\n")

if form.getvalue('s_email'):
	email = form.getvalue('s_email')
if form.getvalue('s_user'):
	username = form.getvalue('s_user')
if form.getvalue('s_mobile'):
	phone = form.getvalue('s_mobile')
if form.getvalue('s_password'):
	password = form.getvalue('s_password')
if form.getvalue('s_fname'):
	fname = form.getvalue('s_fname')
if form.getvalue('s_lname'):
	lname = form.getvalue('s_lname')
if form.getvalue('s_middlename'):
	middle_name = form.getvalue('s_middlename')
if form.getvalue('s_gender'):
	gender = form.getvalue('s_gender')
if form.getvalue('s_dob'):
	dob = form.getvalue('s_dob')
if form.getvalue('s_postaladd'):
	postal_add = form.getvalue('s_postaladd')
if form.getvalue('s_permadd'):
	perm_add = form.getvalue('s_permadd')
if form.getvalue('s_pincode'):
	pincode = form.getvalue('s_pincode')
if form.getvalue('s_city'):
	city = form.getvalue('s_city')
if form.getvalue('s_state'):
	state = form.getvalue('s_state')
if form.getvalue('s_country'):
	country = form.getvalue('s_country')

sql="""INSERT INTO customers (username,fname,lname,middle_name,email,contact,password,gender,dob,postal_add,perm_add,pincode,city,state,country) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(username,fname,lname,middle_name,email,phone,password,gender,dob,postal_add,perm_add,pincode,city,state,country)
try:
	cursor.execute(sql)
	conn.commit()
	cid=customer_details.get_any_value(email,"cid")
	m.send_mail(email,phone,username)
	print("%d"%cid)
except:
	conn.rollback()
	print("-99")
conn.close()
