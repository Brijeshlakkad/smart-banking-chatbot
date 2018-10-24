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
	global acc_id,c_id,acc_no,acc_type,acc_name,balance,passcode,status
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
				self.status=row[8]
		except:
			print("Error")
		conn.close()
class customer_account_by_acc_id:
	global acc_id,c_id,acc_no,acc_type,acc_name,balance,passcode,status
	def account_details(self,acc_id):
		sql="select * from accounts where acc_id='%s'"%acc_id
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
				self.status=row[8]
		except:
			print("Error")
		conn.close()
class customer_account_by_acc_no:
	global acc_id,c_id,acc_no,acc_type,acc_name,balance,passcode,status
	def account_details(self,acc_no):
		sql="select * from accounts where acc_no='%s'"%acc_no
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
				self.status=row[8]
		except:
			print("Error")
		conn.close()

class customer_card:
	global card_id,c_id,acc_id,holder_name,till_month,till_year,cvv,card_type,card_no,status
	def card_details(self,acc_id):
		sql="select * from cards where acc_id='%s'"%acc_id
		conn,cursor=config.connect_to_database()
		try:
			cursor.execute(sql)
			results=cursor.fetchall()
			for row in results:
				self.card_id=row[0]
				self.c_id=row[1]
				self.acc_id=row[2]
				self.holder_name=row[3]
				self.till_month=row[4]
				self.till_year=row[5]
				self.cvv=row[6]
				self.card_type=row[7]
				self.card_no=row[8]
				self.status=row[9]
		except:
			print("Error")
		conn.close()

class Mail:
	USERNAME = private_data.admin_email
	PASSWORD = private_data.admin_password
	def send_passcode(self,user,contact,passcode,sub):
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
	elif f=="status":
		return acc.status
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
	elif f=="status":
		return acc.status
	else:
		return 0
def get_account_by_acc_id(acc_id,f):
	acc=customer_account_by_acc_id()
	acc.account_details(acc_id)
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
	elif f=="status":
		return acc.status
	else:
		return get_any_value_by_id(acc.c_id,f)
def get_account_by_acc_no(acc_no,f):
	acc=customer_account_by_acc_no()
	acc.account_details(acc_no)
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
	elif f=="status":
		return acc.status
	else:
		return -99

def get_card_details_by_user(user,f):
	acc_id=get_account_details_by_user(user,"acc_id")
	c=customer_card()
	c.card_details(acc_id)
	if f=="card_id":
		return c.card_id
	elif f=="c_id":
		return c.c_id
	elif f=="card_no":
		return c.card_no
	elif f=="acc_id":
		return c.acc_id
	elif f=="holder_name":
		return c.holder_name
	elif f=="till_month":
		return c.till_month
	elif f=="till_year":
		return c.till_year
	elif f=="csv":
		return c.cvv
	elif f=="card_type":
		return c.card_type
	elif f=="status":
		return c.status
	else:
		return 0
def get_card_details_by_id(userid,f):
	acc_id=get_account_details_by_id(userid,"acc_id")
	c=customer_card()
	c.card_details(acc_id)
	if f=="card_id":
		return c.card_id
	elif f=="c_id":
		return c.c_id
	elif f=="card_no":
		return c.card_no
	elif f=="acc_id":
		return c.acc_id
	elif f=="holder_name":
		return c.holder_name
	elif f=="till_month":
		return c.till_month
	elif f=="till_year":
		return c.till_year
	elif f=="csv":
		return c.cvv
	elif f=="card_type":
		return c.card_type
	elif f=="status":
		return c.status
	else:
		return 0
def get_card_details_by_acc_id(acc_id,f):
	c=customer_card()
	c.card_details(acc_id)
	if f=="card_id":
		return c.card_id
	elif f=="c_id":
		return c.c_id
	elif f=="card_no":
		return c.card_no
	elif f=="acc_id":
		return c.acc_id
	elif f=="holder_name":
		return c.holder_name
	elif f=="till_month":
		return c.till_month
	elif f=="till_year":
		return c.till_year
	elif f=="csv":
		return c.cvv
	elif f=="card_type":
		return c.card_type
	elif f=="status":
		return c.status
	else:
		return 0
def generate_customer_passcode(user):
	userid=get_any_value(user,"cid")
	contact=get_any_value(user,"contact")
	m=Mail()
	ran_passcode = ''.join([random.choice(string.digits) for n in xrange(6)])
	sub="First Time Generated Passcode"
	sql="update accounts SET passcode='%s' where c_id='%s'"%(ran_passcode,userid)
	conn,cursor=config.connect_to_database()
	try:
		cursor.execute(sql)
		if str(m.send_passcode(user,contact,ran_passcode,sub))=="11":
			conn.commit()
			return "11"
		else:
			conn.rollback()
			return "0"
	except:
		conn.rollback()
		return "0"
	finally:
		conn.close()

def change_customer_passcode(change_passcode,user):
	conn,cursor=config.connect_to_database()
	userid=get_any_value(user,"cid")
	sql="update accounts SET passcode='%s' where c_id='%s'"%(change_passcode,userid)
	conn,cursor=config.connect_to_database()
	try:
		cursor.execute(sql)
		conn.commit()
		return "11"
	except:
		conn.rollback()
		return "0"
	finally:
		conn.close()
def update_account_details(username,email,contact,fname,lname,middle_name):
	conn,cursor=config.connect_to_database()
	sql="Update customers SET username='%s',fname='%s',lname='%s',middle_name='%s',contact='%s' where email='%s'"%(username,fname,lname,middle_name,contact,email)
	try:
		cursor.execute(sql)
		conn.commit()
		return "11"
	except:
		conn.rollback()
		return "-99"

def update_bill_details(user,postal_add,perm_add,pincode,city,state,country):
	conn,cursor=config.connect_to_database()
	sql="Update customers SET postal_add='%s',perm_add='%s',pincode='%s',city='%s',state='%s',country='%s' where email='%s'"%(postal_add,perm_add,pincode,city,state,country,user)
	try:
		cursor.execute(sql)
		conn.commit()
		return "11"
	except:
		conn.rollback()
		return "-99"

def update_password(user,new_password):
	conn,cursor=config.connect_to_database()
	sql="Update customers SET password='%s' where email='%s'"%(new_password,user)
	try:
		cursor.execute(sql)
		conn.commit()
		return "11"
	except:
		conn.rollback()
		return "0"
def check_service(user):
	conn,cursor=config.connect_to_database()
	sql="select jon from customers where email='%s'"%(user)
	try:
		cursor.execute(sql)
		row=cursor.fetchone()
		return int(row[0])
	except:
		return "-99"
def start_service(jon,user):
	conn,cursor=config.connect_to_database()
	sql="update customers SET jon='%s' where email='%s'"%(jon,user)
	try:
		cursor.execute(sql)
		conn.commit()
		return "11"
	except:
		conn.rollback()
		return "0"
def jon_service(bit,user):
	conn,cursor=config.connect_to_database()
	sql="update customers SET jon='%s' where email='%s'"%(bit,user)
	try:
		cursor.execute(sql)
		conn.commit()
		return "11"
	except:
		conn.rollback()
		return "0"
def how_many_services(userid,services):
	conn,cursor=config.connect_to_database()
	if services:
		sql="select card_id from cards where c_id='%s'"%userid
	else:
		sql="select loan_id from cards where c_id='%s'"%userid
	try:
		cursor.execute(sql)
		num=cursor.rowcount
		return num
	except:
		return "-99"

def request_services(acc_id,request):
	conn,cursor=config.connect_to_database()
	status=0
	sql="insert into requests(acc_id,card_loan,status_bit) values('%s','%s','%s')"%(acc_id,request,status)
	try:
		cursor.execute(sql)
		conn.commit()
		return "11"
	except:
		conn.rollback()
		return "-99"
def status_request(acc_id,status_request):
	conn,cursor=config.connect_to_database()
	sql="select status_bit from requests where acc_id='%s' AND card_loan='%s'"%(acc_id,status_request)
	try:
		cursor.execute(sql)
		row=cursor.fetchone()
		if row==None:
			return "-1"
		return row[0]
	except:
		return "-99"

class request:
	global acc_id,status
	def request_details(self,r_id):
		conn,cursor=config.connect_to_database()
		sql="select * from requests where r_id='%s'"%r_id
		try:
			cursor.execute(sql)
			row=cursor.fetchone()
			self.r_id=row[0]
			self.acc_id=row[1]
			self.req=row[2]
			self.status=row[3]
			self.time=row[4]
		except:
			return "-99"
		finally:
			conn.close()
class request_by_acc_id:
	global acc_id,status
	def request_details(self,acc_id):
		conn,cursor=config.connect_to_database()
		sql="select * from requests where acc_id='%s'"%acc_id
		try:
			cursor.execute(sql)
			row=cursor.fetchone()
			self.r_id=row[0]
			self.acc_id=row[1]
			self.req=row[2]
			self.status=row[3]
			self.time=row[4]
		except:
			return -99
		finally:
			conn.close()
def get_request_details(r_id,f):
	c=request()
	c.request_details(r_id)
	if f=="r_id":
		return c.r_id
	elif f=="acc_id":
		return c.acc_id
	elif f=="req":
		return c.req
	elif f=="status":
		return c.status
	elif f=="time":
		return c.time
	else:
		return get_account_by_acc_id(c.acc_id,f)

def get_request_details_by_acc_id(acc_id,f):
	c=request_by_acc_id()
	c.request_details(acc_id)
	if f=="r_id":
		return c.r_id
	elif f=="acc_id":
		return c.acc_id
	elif f=="req":
		return c.req
	elif f=="status":
		return c.status
	elif f=="time":
		return c.time
	else:
		return -99

def change_customer_card_status(user,status):
	userid=get_any_value(user,"cid")
	conn,cursor=config.connect_to_database()
	sql="update cards SET status='%s' where c_id='%s'"%(status,userid)
	try:
		cursor.execute(sql)
		conn.commit()
		return 1
	except:
		conn.rollback()
		return -99
	finally:
		conn.close()
def check_acc_num_exists(acc_no,userid):
	conn,cursor=config.connect_to_database()
	sql="select c_id,acc_name from accounts where acc_no='%s'"%(acc_no)
	try:
		cursor.execute(sql)
		if cursor.rowcount==1:
			row=cursor.fetchone()
			c_id="%s"%row[0]
			userid="%s"%userid
			if c_id==userid:
				return -22
			return "11%s"%row[1]
		return -33
	except:
		return -99
	finally:
		conn.close()
def transaction_happened(cursor,from_acc_no,to_acc_no,amount):
	amount=int(amount)
	accs=[from_acc_no,to_acc_no]
	dict={}
	for i in range(len(accs)):
		sql="select balance from accounts where acc_no='%s'"%(accs[i])
		try:
			cursor.execute(sql)
			row=cursor.fetchone()
			balance=int(row[0])
			dict.update(dict.fromkeys([accs[i]],balance))
			if (accs[i]==from_acc_no and balance<amount):
				return -22
		except:
			return -99
	for acc,balance in dict.items():
		if acc==from_acc_no:
			balance-=amount
		elif acc==to_acc_no:
			balance+=amount
		sql="update accounts SET balance='%s' where acc_no='%s'"%(balance,acc)
		try:
			cursor.execute(sql)
			return 11
		except:
			conn.rollback()
			return -99
def make_transaction(from_acc_no,to_acc_no,amount):
	conn,cursor=config.connect_to_database()
	trans_id=2179516709
	sql="insert into transactions(from_acc,to_acc,amount) values('%s','%s','%s')"%(from_acc_no,to_acc_no,amount)
	try:
		cursor.execute(sql)
		flag=transaction_happened(cursor,from_acc_no,to_acc_no,amount)
		if flag!=11:
			return flag
		conn.commit()
		sql="SELECT t_id FROM transactions ORDER BY t_id DESC LIMIT 1;"
		try:
			cursor.execute(sql)
			row=cursor.fetchone()
			t_id=row[0]
			t_id=int(t_id)
			trans_id+=t_id
			return "11<table class='myTable'><tr><td><span style='color:rgba(32,78,148,1);'>Transactions id</span></td><td>#%s</td></tr><tr><td>From Account Number</td><td>%s</td></tr><tr><td>To Account Number</td><td>%s</td></tr><tr><td>Amount</td><td>Rs. %s</td></tr></table>"%(trans_id,from_acc_no,to_acc_no,amount)
		except:
			return -99
	except:
		conn.rollback()
		return -999
	finally:
		conn.close()
def get_last_transaction(acc_no,n):
	conn,cursor=config.connect_to_database()
	trans_id=2179516709
	sql="SELECT t_id,from_acc,to_acc,amount FROM transactions where from_acc='%s' or to_acc='%s' ORDER BY t_id DESC LIMIT %s;"%(acc_no,acc_no,n)
	try:
		cursor.execute(sql)
		results=cursor.fetchall()
		num=cursor.rowcount
		num_str=str(num).zfill(2)
		response="""11%s<br/><div class="row"><b>Last %s Transactions</b></div>"""%(num_str,num_str)
		for row in results:
			t_id=row[0]
			t_id=int(t_id)
			from_acc_no=row[1]
			to_acc_no=row[2]
			trans_id+=t_id
			amount=row[3]
			response+="""<hr/><div class="row"><div class="col-sm-6" style='color:rgba(254,254,254,1);'>Transactions id</div><div class="col-sm-6">#%s</div></div><div class="row"><div class="col-sm-6" >From Account Number</div><div class="col-sm-6" >%s</div></div><div class="row"><div class="col-sm-6" >To Account Number</div><div class="col-sm-6">%s</div></div><div class="row"><div class="col-sm-6" >Amount</div><div class="col-sm-6">Rs. %s</div></div>"""%(trans_id,from_acc_no,to_acc_no,amount)
		return response
	except:
		return -99
def get_last_transaction_without_html_tags(acc_no,n):
	conn,cursor=config.connect_to_database()
	trans_id=2179516709
	sql="SELECT t_id,from_acc,to_acc,amount FROM transactions where from_acc='%s' or to_acc='%s' ORDER BY t_id DESC LIMIT %s;"%(acc_no,acc_no,n)
	try:
		cursor.execute(sql)
		results=cursor.fetchall()
		num=cursor.rowcount
		num_str=str(num).zfill(2)
		response="""Last %s Transactions"""%(num_str)
		i=int(n)+1
		for row in results:
			t_id=row[0]
			t_id=int(t_id)
			from_acc_no=row[1]
			to_acc_no=row[2]
			trans_id+=t_id
			amount=row[3]
			i-=1
			response+="""\n-----%s----\nTransactions id: #%s\nFrom Account Number: %s\nTo Account Number: %s\nAmount: Rs. %s"""%(i,trans_id,from_acc_no,to_acc_no,amount)
		return response
	except:
		return -99
	finally:
		conn.close()
def customer_card_exists(userid,card_no):
	conn,cursor=config.connect_to_database()
	sql="select card_id from cards where card_no='%s' and c_id='%s'"%(card_no,userid)
	try:
		cursor.execute(sql)
		return cursor.rowcount
	except:
		return -99
	finally:
		conn.close()

def customer_card_has(userid):
	conn,cursor=config.connect_to_database()
	sql="select card_no from cards where c_id='%s'"%(userid)
	try:
		cursor.execute(sql)
		if cursor.rowcount==1:
			row=cursor.fetchone()
			return row[0]
		return -22
	except:
		return -99
	finally:
		conn.close()
def check_request_exist(acc_id):
	conn,cursor=config.connect_to_database()
	sql="select r_id from requests where acc_id='%s'"%(acc_id)
	try:
		cursor.execute(sql)
		return cursor.rowcount
	except:
		return -99
	finally:
		conn.close()
