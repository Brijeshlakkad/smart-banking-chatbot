#!/usr/bin/python
import cgi, os
import cgitb
import customer_details
import Cookie
print 'Content-Type: text/plain'
print 
cgitb.enable()
form = cgi.FieldStorage()
fileitem = form['file_tobe']
jon_cookies = Cookie.SimpleCookie()
userid=jon_cookies['User_cid']
username=customer_details.get_any_value(userid,"username")
customer_path="files/"+username
if not os.path.exists(customer_path):
    os.makedirs(customer_path)
if fileitem.filename:
	if fileitem.filename.endswith("pdf") or fileitem.filename.endswith("jpeg"):
		if fileitem.filename.endswith("pdf"):
			fn=username+".pdf"
		if fileitem.filename.endswith("jpeg"):
			fn=username+".jpeg"
		open(customer_path+'/' + fn, 'w+').write(fileitem.file.read())
		message = '11'
	else:
		message="-99"
else:
	message = '-1'
   
print ("%s"%message)