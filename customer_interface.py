#!/usr/bin/python
import cgi, cgitb
import sys
import security
import customer_details
import feedback_modules
import jon_snow_brain
print("Content-type:text/html;Content-type: image/jpeg\r\n\r\n")
cgitb.enable(display=0, logdir="/path/to/logdir")
form = cgi.FieldStorage()
if form.getvalue('get_data'):
	user=security.protect_data(form.getvalue('user'))
	get_data = security.protect_data(form.getvalue('get_data'))
	got_it=customer_details.get_any_value(user,get_data)
	print("%s"%got_it)
if form.getvalue('get_data_id') and form.getvalue('userid'):
	userid = security.protect_data(form.getvalue('userid'))
	get_data_id=security.protect_data(form.getvalue('get_data_id'))
	got_it=customer_details.get_any_value_by_id(userid,get_data_id)
	print("%s"%got_it)
if form.getvalue('get_document') and form.getvalue('userid'):
	userid = security.protect_data(form.getvalue('userid'))
	username=customer_details.get_any_value_by_id(userid,"username")
	get_document=security.protect_data(form.getvalue('get_document'))
	got_it=customer_details.get_any_document(username,get_document)
	print("%s"%got_it)
if form.getvalue('get_acc_details') and form.getvalue('user'):
	user = security.protect_data(form.getvalue('user'))
	get_acc_details=security.protect_data(form.getvalue('get_acc_details'))
	got_it=customer_details.get_account_details_by_user(user,get_acc_details)
	print("%s"%got_it)
if form.getvalue('get_card_details') and form.getvalue('user'):
	user = security.protect_data(form.getvalue('user'))
	get_card_details=security.protect_data(form.getvalue('get_card_details'))
	got_it=customer_details.get_card_details_by_user(user,get_card_details)
	print("%s"%got_it)
if form.getvalue('get_passcode'):
	user = security.protect_data(form.getvalue('get_passcode'))
	flag_bit=customer_details.generate_customer_passcode(user)
	print("%s"%flag_bit)
if form.getvalue('change_passcode') and form.getvalue('user'):
	change_passcode = security.protect_data(form.getvalue('change_passcode'))
	user = security.protect_data(form.getvalue('user'))
	flag_bit=customer_details.change_customer_passcode(change_passcode,user)
	print("%s"%flag_bit)
if form.getvalue('update_account_details'):
	username=security.protect_data(form.getvalue('update_account_details'))
	email = security.protect_data(form.getvalue('s_email'))
	contact = security.protect_data(form.getvalue('s_mobile'))
	fname = security.protect_data(form.getvalue('s_fname'))
	lname = security.protect_data(form.getvalue('s_lname'))
	middle_name = security.protect_data(form.getvalue('s_middlename'))
	flag_bit=customer_details.update_account_details(username,email,contact,fname,lname,middle_name)
	print("%s"%flag_bit)
if form.getvalue('change_password'):
	user=security.protect_data(form.getvalue('user'))
	old_password=str(security.protect_data(form.getvalue('change_password')))
	new_password = str(security.protect_data(form.getvalue('new_password')))
	got_old_password=str(customer_details.get_any_value(user,"password"))
	if old_password==new_password:
		flag_bit=-1
	elif got_old_password==old_password:
		flag_bit=customer_details.update_password(user,new_password)
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
	flag_bit=customer_details.check_service(check)
	print("%s"%flag_bit)
if form.getvalue("start_service"):
	check=security.protect_data(form.getvalue("start_service"))
	jon=1
	flag_bit=customer_details.start_service(jon,check)
	print("%s"%flag_bit)
if form.getvalue("jon_service") and form.getvalue("user"):
	bit=security.protect_data(form.getvalue("jon_service"))
	user=security.protect_data(form.getvalue("user"))
	flag_bit=customer_details.jon_service(bit,user)
	print("%s"%flag_bit)
if form.getvalue("message") and form.getvalue("user"):
	text=security.protect_data(form.getvalue("message"))
	user=security.protect_data(form.getvalue("user"))
	get_id=customer_details.get_any_value(user,"cid")
	jon=0
	flag_bit=jon_snow_brain.add_chat(get_id,jon,text)
	print("%s"%flag_bit)
if form.getvalue("reload_messages"):
	user=security.protect_data(form.getvalue("reload_messages"))
	get_id=customer_details.get_any_value(user,"cid")
	flag_bit=jon_snow_brain.reload_chats(get_id,user)
	print("%s"%flag_bit)
if form.getvalue("how_many_services") and form.getvalue("user"):
	user=security.protect_data(form.getvalue("user"))
	services=security.protect_data(form.getvalue("how_many_services"))
	userid=customer_details.get_any_value(user,"cid")
	flag_bit=customer_details.how_many_services(userid,services)
	print("%s"%flag_bit)
if form.getvalue("request_services") and form.getvalue("user"):
	request_services=security.protect_data(form.getvalue("request_services"))
	user=security.protect_data(form.getvalue("user"))
	acc_id=customer_details.get_account_details_by_user(user,"acc_id")
	flag_bit=customer_details.request_services(acc_id,request_services)
	print("%s"%flag_bit)
if form.getvalue("status_request") and form.getvalue("user"):
	status_request=security.protect_data(form.getvalue("status_request"))
	user=security.protect_data(form.getvalue("user"))
	acc_id=customer_details.get_account_details_by_user(user,"acc_id")
	flag_bit=customer_details.status_request(acc_id,status_request)
	print("%s"%flag_bit)
if form.getvalue("update_bill_details") and form.getvalue("postal_add") and form.getvalue("perm_add") and form.getvalue("pincode") and form.getvalue("city") and form.getvalue("state") and form.getvalue("country"):
	user=security.protect_data(form.getvalue("update_bill_details"))
	postal_add=security.protect_data(form.getvalue("postal_add"))
	perm_add=security.protect_data(form.getvalue("perm_add"))
	city=security.protect_data(form.getvalue("city"))
	pincode=security.protect_data(form.getvalue("pincode"))
	state=security.protect_data(form.getvalue("state"))
	country=security.protect_data(form.getvalue("country"))
	flag_bit=customer_details.update_bill_details(user,postal_add,perm_add,pincode,city,state,country)
	print("%s"%flag_bit)
if form.getvalue("check_acc_num_exists") and form.getvalue("user"):
	user=security.protect_data(form.getvalue("user"))
	acc_no=security.protect_data(form.getvalue("check_acc_num_exists"))
	userid=customer_details.get_any_value(user,"cid")
	flag_bit=customer_details.check_acc_num_exists(acc_no,userid)
	flag_bit=security.protect_data(flag_bit)
	print("%s"%flag_bit)
if form.getvalue("make_transaction") and form.getvalue("acc_num") and form.getvalue("amount"):
	user=security.protect_data(form.getvalue("make_transaction"))
	amount=security.protect_data(form.getvalue("amount"))
	from_acc_no=customer_details.get_account_details_by_user(user,"acc_no")
	if from_acc_no==0:
		print("-99")
	to_acc_no=security.protect_data(form.getvalue("acc_num"))
	flag_bit=customer_details.make_transaction(from_acc_no,to_acc_no,amount)
	flag_bit=flag_bit.strip()
	print("%s"%flag_bit)
if form.getvalue("get_last_transaction") and form.getvalue("num_of_transactions"):
	user=security.protect_data(form.getvalue("get_last_transaction"))
	num=security.protect_data(form.getvalue("num_of_transactions"))
	acc_no=customer_details.get_account_details_by_user(user,"acc_no")
	flag_bit=customer_details.get_last_transaction(acc_no,num)
	flag_bit=flag_bit.strip()
	print("%s"%flag_bit)
if form.getvalue('get_card_request_num'):
	user = security.protect_data(form.getvalue("get_card_request_num"))
	userid=customer_details.get_any_value(user,"cid")
	accid=customer_details.get_account_details_by_id(userid,"acc_id")
	flag_bit=customer_details.check_request_exist(accid)
	print("%s"%flag_bit)
