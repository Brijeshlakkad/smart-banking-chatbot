#!/usr/bin/python 
import pymysql
import config
def add_feedback(email,f_text):
	conn,cursor=config.connect_to_database()
	sql="insert into feedbacks(email,f_text) values('%s','%s')"%(email,f_text);
	try:
		cursor.execute(sql)
		conn.commit()
		return "11"
	except:
		conn.rollback()
		return "0"
def check_same_feedback(email,f_text):
	conn,cursor=config.connect_to_database()
	sql="select * from feedbacks where email='%s'"%email
	try:
		cursor.execute(sql)
		results=cursor.fetchall()
		for row in results:
			got_f_text=str(row[2]).lower()
			f_text=str(f_text).lower()
			if (f_text==got_f_text):
				return '1'
		return "11"
	except:
		conn.rollback()
		return "0"