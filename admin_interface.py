#!/usr/bin/python
import cgi, cgitb
import sys
import security
import admin_show_customers
import no_found
import customer_details
import admin_control
print("Content-type:text/html;Content-type: image/jpeg\r\n\r\n")
cgitb.enable(display=0, logdir="/path/to/logdir")
form = cgi.FieldStorage()
if form.getvalue('flag'):
	flag=form.getvalue("flag")
	info=no_found.no_found("No new requests")
	if flag=="approved_customers":
		info=admin_show_customers.show_customers(1)
	elif flag=="rejected_customers":
		info=admin_show_customers.show_customers(-1)
	elif flag=="new_customers":
		info=admin_show_customers.show_customers(0)
	elif flag=="new_requests":
		info=admin_control.provides_requests()
	elif flag=="new_feedbacks":
		info=admin_control.provides_feedbacks()
	print("%s"%info)
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
if form.getvalue("verify_customer") and form.getvalue("status"):
	userid = security.protect_data(form.getvalue('verify_customer'))
	status = security.protect_data(form.getvalue('status'))
	user=customer_details.get_any_value_by_id(userid,"email")
	flag_bit=admin_control.verify_customer(userid,user,status)
	print("%s"%flag_bit)
if form.getvalue('get_acc_details') and form.getvalue('userid'):
	userid = security.protect_data(form.getvalue('userid'))
	get_acc_details=security.protect_data(form.getvalue('get_acc_details'))
	got_it=customer_details.get_account_details_by_id(userid,get_acc_details)
	print("%s"%got_it)
if form.getvalue('get_request_details') and form.getvalue('r_id'):
	r_id = security.protect_data(form.getvalue('r_id'))
	get_request_details=security.protect_data(form.getvalue('get_request_details'))
	got_it=customer_details.get_request_details(r_id,get_request_details)
	print("%s"%got_it)
if form.getvalue("verify_card_request") and form.getvalue("status"):
	r_id = security.protect_data(form.getvalue('verify_card_request'))
	status = security.protect_data(form.getvalue('status'))
	acc_id=customer_details.get_request_details(r_id,"acc_id")
	flag_bit=admin_control.verify_card_request(r_id,acc_id,status)
	print("%s"%flag_bit)
if form.getvalue('get_card_details') and form.getvalue('userid'):
	userid = security.protect_data(form.getvalue('userid'))
	get_card_details=security.protect_data(form.getvalue('get_card_details'))
	got_it=customer_details.get_card_details_by_id(userid,get_card_details)
	print("%s"%got_it)
