#!/usr/bin/python 
import cgi, cgitb 
import sys
import security
import admin_show_customers
import no_found
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
	else:
		info=admin_show_customers.show_customers(0)
	print("%s"%info)