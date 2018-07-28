#!/usr/bin/python 
import cgi, cgitb 
import sys
import security
import customer_details
import update_customer_details
import feedback_modules
print("Content-type:text/html;Content-type: image/jpeg\r\n\r\n")
cgitb.enable(display=0, logdir="/path/to/logdir")
form = cgi.FieldStorage()	
if form.getvalue('get_data'):
	user=security.protect_data(form.getvalue('user'))
	get_data = security.protect_data(form.getvalue('get_data'))
	got_it=customer_details.get_any_value(user,get_data)
	print("%s"%got_it)
if form.getvalue('update_account_details'):
	username=security.protect_data(form.getvalue('update_account_details'))
	email = security.protect_data(form.getvalue('s_email'))
	contact = security.protect_data(form.getvalue('s_mobile'))
	fname = security.protect_data(form.getvalue('s_fname'))
	lname = security.protect_data(form.getvalue('s_lname'))
	middle_name = security.protect_data(form.getvalue('s_middlename'))
	flag_bit=update_customer_details.update_account_details(username,email,contact,fname,lname,middle_name)
	print("%s"%flag_bit)
if form.getvalue('change_password'):
	user=security.protect_data(form.getvalue('user'))
	old_password=str(security.protect_data(form.getvalue('change_password')))
	new_password = str(security.protect_data(form.getvalue('new_password')))
	got_old_password=str(customer_details.get_any_value(user,"password"))
	if old_password==new_password:
		flag_bit=-1
	elif got_old_password==old_password:
		flag_bit=update_customer_details.update_password(user,new_password)
	else:
		flag_bit=-99
	print("%s"%flag_bit)
if form.getvalue('feedback') and form.getvalue('email'):
	f_text=security.protect_data(form.getvalue('feedback'))
	email=security.protect_data(form.getvalue('email'))
	if str(feedback_modules.check_same_feedback(email,f_text))=="11":
		flag_bit=feedback_modules.add_feedback(email,f_text)
	else:
		flag_bit="111"
	print("%s"%flag_bit)
if form.getvalue("check_service"):
	check=security.protect_data(form.getvalue("check_service"))
	flag_bit=update_customer_details.check_service(check)
	print("%s"%flag_bit)
if form.getvalue("start_service"):
	check=security.protect_data(form.getvalue("start_service"))
	jon=1
	flag_bit=update_customer_details.start_service(jon,check)
	print("%s"%flag_bit)
	