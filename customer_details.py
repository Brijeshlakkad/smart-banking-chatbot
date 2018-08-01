#!/usr/bin/python 
import pymysql
import cgi, cgitb 
import sys
import os
import random
import config
import find_file
import string
import private_data
from smtplib import SMTP_SSL as SMTP 
from email.mime.text import MIMEText
class customer:
	global cid,username,fname,lname,middle_name,email,password,contact,postal_add,perm_add,city,state,country,pincode,dob,gender
	global created_time,jon,hasAcc
	def customer_details(self,user):
		sql="select * from customers where email='%s'"%user
		conn,cursor=config.connect_to_database()
		try:
			cursor.execute(sql)
			results=cursor.fetchall()
			for row in results:
				self.cid=row[0]
				self.username=row[1]
				self.fname=row[2]
				self.lname=row[3]
				self.email=row[4]
				self.password=row[5]
				self.contact=row[6]
				self.postal_add=row[7]
				self.perm_add=row[8]
				self.city=row[9]
				self.state=row[10]
				self.country=row[11]
				self.middle_name=row[12]
				self.pincode=row[13]
				self.dob=row[14]
				self.gender=row[15]
				self.created_time=row[17]
				self.jon=row[18]
				self.hasAcc=row[19]
		except:
			print("Error")
		conn.close()
class customer_by_id:
	global cid,username,fname,lname,middle_name,email,password,contact,postal_add,perm_add,city,state,country,pincode,dob,gender
	global created_time,jon,hasAcc
	def customer_details(self,userid):
		sql="select * from customers where cid='%s'"%userid
		conn,cursor=config.connect_to_database()
		try:
			cursor.execute(sql)
			results=cursor.fetchall()
			for row in results:
				self.cid=row[0]
				self.username=row[1]
				self.fname=row[2]
				self.lname=row[3]
				self.email=row[4]
				self.password=row[5]
				self.contact=row[6]
				self.postal_add=row[7]
				self.perm_add=row[8]
				self.city=row[9]
				self.state=row[10]
				self.country=row[11]
				self.middle_name=row[12]
				self.pincode=row[13]
				self.dob=row[14]
				self.gender=row[15]
				self.created_time=row[17]
				self.jon=row[18]
				self.hasAcc=row[19]
		except:
			print("Error")
		conn.close()
	
class customer_account:
	global acc_id,c_id,acc_no,acc_type,acc_name,balance,passcode
	def account_details(self,c_id):
		sql="select * from accounts where c_id='%s'"%c_id
		conn,cursor=config.connect_to_database()
		try:
			cursor.execute(sql)
			results=cursor.fetchall()
			for row in results:
				self.acc_id=row[0]
				self.c_id=row[1]
				self.acc_name=row[2]
				self.acc_type=row[3]
				self.balance=row[4]
				self.created_time=row[5]
				self.passcode=row[6]
				self.acc_no=row[7]
		except:
			print("Error")
		conn.close()

class Mail:
	USERNAME = private_data.admin_email
	PASSWORD = private_data.admin_password
	def send_passcode(self,user,contact,passcode):
		SMTPserver = 'smtp.gmail.com'
		sender =    private_data.admin_email
		destination = user
		text_subtype = 'html'
		content="""\
		<h2>Jon Snow (The Assistant)</h2> <br> \
		Dear customer,<br> \
		<p>Your passcode for registered contact number %s account is <h2>%s</h2> </p>
			 <br> \
		""" % (contact,passcode)
		subject="First Time Generated Passcode"
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
			return "0"
def get_any_value(user,f):
	c=customer()
	c.customer_details(user)
	if f=="cid":
		return c.cid
	elif f=="username":
		return c.username
	elif f=="fname":
		return c.fname
	elif f=="lname":
		return c.lname
	elif f=="middle_name":
		return c.middle_name
	elif f=="email":
		return c.email
	elif f=="password":
		return c.password
	elif f=="contact":
		return c.contact
	elif f=="postal_add":
		return c.postal_add
	elif f=="perm_add":
		return c.perm_add
	elif f=="city":
		return c.city
	elif f=="state":
		return c.state
	elif f=="country":
		return c.country
	elif f=="pincode":
		return c.pincode
	elif f=="dob":
		return c.dob
	elif f=="gender":
		return c.gender
	elif f=="jon":
		return c.jon
	elif f=="hasAcc":
		return c.hasAcc
	elif f=="created_time":
		return c.created_time
	else: 
		return 0
def get_any_value_by_id(userid,f):
	c=customer_by_id()
	c.customer_details(userid)
	if f=="cid":
		return c.cid
	elif f=="username":
		return c.username
	elif f=="fname":
		return c.fname
	elif f=="lname":
		return c.lname
	elif f=="middle_name":
		return c.middle_name
	elif f=="email":
		return c.email
	elif f=="password":
		return c.password
	elif f=="contact":
		return c.contact
	elif f=="postal_add":
		return c.postal_add
	elif f=="perm_add":
		return c.perm_add
	elif f=="city":
		return c.city
	elif f=="state":
		return c.state
	elif f=="country":
		return c.country
	elif f=="pincode":
		return c.pincode
	elif f=="dob":
		return c.dob
	elif f=="gender":
		return c.gender
	elif f=="jon":
		return c.jon
	elif f=="hasAcc":
		return c.hasAcc
	elif f=="created_time":
		return c.created_time
	else: 
		return 0

def get_any_document(username,doc):
	return find_file.find_customer_get_file(username,doc)

def get_account_details_by_id(userid,f):
	acc=customer_account()
	acc.account_details(userid)
	if f=="acc_id":
		return acc.acc_id
	elif f=="c_id":
		return acc.c_id
	elif f=="acc_no":
		return acc.acc_no
	elif f=="acc_type":
		return acc.acc_type
	elif f=="acc_name":
		return acc.acc_name
	elif f=="balance":
		return acc.balance
	elif f=="passcode":
		return acc.passcode
	elif f=="created_time":
		return acc.created_time
	else:
		return 0
	
def get_account_details_by_user(user,f):
	userid=get_any_value(user,"cid")
	acc=customer_account()
	acc.account_details(userid)
	if f=="acc_id":
		return acc.acc_id
	elif f=="c_id":
		return acc.c_id
	elif f=="acc_no":
		return acc.acc_no
	elif f=="acc_type":
		return acc.acc_type
	elif f=="acc_name":
		return acc.acc_name
	elif f=="balance":
		return acc.balance
	elif f=="passcode":
		return acc.passcode
	elif f=="created_time":
		return acc.created_time
	else:
		return 0

def generate_customer_passcode(user):
	userid=get_any_value(user,"cid")
	contact=get_any_value(user,"contact")
	m=Mail()
	ran_passcode = ''.join([random.choice(string.digits) for n in xrange(6)])
	sql="update accounts SET passcode='%s' where c_id='%s'"%(ran_passcode,userid)
	conn,cursor=config.connect_to_database()
	try:
		cursor.execute(sql)
		if str(m.send_passcode(user,contact,ran_passcode))=="11":
			conn.commit()
			return "11"
		else:
			conn.rollback()
			return "0n"
	except:
		conn.rollback()
		return "0"
	finally:
		conn.close()