#!/usr/bin/python
import config
import os
import fnmatch
def find_customer_get_file(username,doc):
	if doc=="file":
		root="customer_files"
		try:
			listOfFiles = os.listdir(os.path.join(root,username))
		except:
			return -1
		patterns = ["pdf","jpeg","jpg"]
		filename=username
	elif doc=="profile_pic":
		root="customer_images"
		try:
			listOfFiles = os.listdir(os.path.join(root,username))
		except:
			return -1
		patterns = ["png","jpeg","jpg"]
		filename=username
	path=os.path.join(root,username)
	for entry in listOfFiles:
		for p in patterns:
			if entry.endswith(p) and entry.startswith(filename):
				path=os.path.join(path,entry)
				break
	return path
