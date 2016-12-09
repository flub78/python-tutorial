#!/usr/bin/python

def help():
	hlp = """Small command interpretor
	command:
		help : print this
		quit : exit the interpretor
	"""
	print hlp
	
try:
	while True:
		line = raw_input(">: ")
		print line
		if (line == "quit"):
			break
		elif (line == "help"):
			help()
except:
	all
	
print "bye"

