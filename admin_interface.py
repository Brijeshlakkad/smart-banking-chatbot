#!/usr/bin/python 
import cgi, cgitb 
import sys
import security
import admin_login_data
print("Content-type:text/html;Content-type: image/jpeg\r\n\r\n")
cgitb.enable(display=0, logdir="/path/to/logdir")
form = cgi.FieldStorage()	
if form.getvalue('admin_id') and form.getvalue('admin_password'):
	admin_id=security.protect_data(form.getvalue('admin_id'))
	admin_password=security.protect_data(form.getvalue('admin_password'))
	flag_bit=admin_login_data.login_module(admin_id,admin_password)
	print("%s"%flag_bit)