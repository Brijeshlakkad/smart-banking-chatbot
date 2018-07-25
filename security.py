#!/usr/bin/python 
import cgi, cgitb 
import sys
def protect_data(xyz):
	xyz=cgi.escape(xyz)
	xyz=xyz.strip()
	return xyz