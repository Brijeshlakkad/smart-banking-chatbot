#!/usr/bin/python
import config
import os
import fnmatch
def find_customer_files(username):
	root="customer_files"
	listOfFiles = os.listdir(os.path.join(root,username))
	patterns = ["pdf","jpeg","jpg"]  
	for entry in listOfFiles:  
		for p in patterns:
			if entry.endswith(p):
				print(entry)
def find_customer_files(username):
	root="customer_images"
	listOfFiles = os.listdir(os.path.join(root,username))
	patterns = ["png","jpeg","jpg"]  
	for entry in listOfFiles:  
		for p in patterns:
			if entry.endswith(p):
				print(entry)