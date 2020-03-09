from __main__ import *

def commit_query(query):
	__cursor__.execute(query)
	__rhodes__.commit()
