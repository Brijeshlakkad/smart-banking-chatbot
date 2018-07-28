#!/usr/bin/python 
import pymysql
import cgi, cgitb 
import sys
import os
import config
def update_account_details(username,email,contact,fname,lname,middle_name):
	conn,cursor=config.connect_to_database()
	sql="Update customers SET username='%s',fname='%s',lname='%s',middle_name='%s',contact='%s' where email='%s'"%(username,fname,lname,middle_name,contact,email)
	try:
		cursor.execute(sql)
		conn.commit()
		return "11"
	except:
		conn.rollback()
		return "0"

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
