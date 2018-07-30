#!/usr/bin/python 
import cgi, cgitb 
import sys
import security
import admin_login_data
print("Content-type:text/html;Content-type: image/jpeg\r\n\r\n")
cgitb.enable(display=0, logdir="/path/to/logdir")
form = cgi.FieldStorage()	
if form.getvalue('show_new_customers'):
	info=show_customers.show_customers(0)
	print("%s"%info)