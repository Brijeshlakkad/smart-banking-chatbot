import cgi, cgitb 
import sys
import os
import MySQLdb
import base64
def connect_to_database():
	conn = MySQLdb.connect (host = "localhost",user = "root",passwd = "",db = "minor_project")
	cursor = conn.cursor ()
	cursor = conn.cursor(MySQLdb.cursors.DictCursor)
	return conn,cursor