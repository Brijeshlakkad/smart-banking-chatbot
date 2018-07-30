#!/usr/bin/python
import config
def show_customers(bit):
	conn,cursor=config.connect_to_database()
	bit=int(bit)
	sql="select * from customers where hasAcc='%s'"%bit
	try:
		cursor.execute(sql)
		results=cursor.fetchall()
		for row in results:
			
	except:
		return "-1"