#!/usr/bin/python 
import pymysql
import cgi, cgitb 
import sys
import os
import config
import customer_details
def add_chat(from_id,to_id,text):
	conn,cursor=config.connect_to_database()
	sql="insert into chats(from_id,to_id,text) values('%s','%s','%s')"%(from_id,to_id,text)
	try:
		cursor.execute(sql)
		conn.commit()
		return "11"
	except:
		conn.rollback()
		return "0"

def reload_chats(user_id,email_id):
	conn,cursor=config.connect_to_database()
	sql="select * from chats where from_id='%s' or to_id='%s' ORDER BY created_time ASC"%(user_id,user_id)
	reload_mess=""
	try:
		cursor.execute(sql)
		results=cursor.fetchall()
		for row in results:
			chat_id="chat_%s"%row[0]
			from_id=row[1]
			to_id=row[2]
			text=row[3]
			datetime=row[4]
			time=datetime.strftime('%H : %M')
			name=customer_details.get_any_value(email_id,"username")
			profile_pic=customer_details.get_any_document(name,"profile_pic")
			if int(to_id)!=0 or from_id==0:
				reload_mess+="""<li id='%s' class="mess"><div><img src="images/jon-cart.jpg" alt="You" style="width:100%%;"><p class="text-left">%s</p><br/><span class="time-right">%s</span></div></li><br/>"""%(chat_id,text,time)
			else:
				reload_mess+="""<li id='%s' class='mess'><div><img src="%s" alt="Jon" class="right" style="height:50px;"><p class="text-right">%s</p><br/><span class="time-left">%s</span></div></li><br/>"""%(chat_id,profile_pic,text,time)
		return reload_mess
	except:
		return "error"
