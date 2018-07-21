#!/usr/bin/python 
import cgi, cgitb 
import pymysql
def connect_to_database():
	conn=pymysql.connect("localhost",'root','root','minor_project',8889)
	cursor = conn.cursor()
	return conn,cursor