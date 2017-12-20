#!/usr/bin/python
#
# Minimal command line interpretor
#
# TODO: manage the cursor 

def help():
	""" Lists supported commands """

	hlp = """Small command interpretor
	command:
		help : print this
		quit : exit the interpretor
	"""
	print (hlp)

def interpretor():
	""" The interpretor event loop """
	try:
		while True:
			line = raw_input(">: ")
			print (line)
			if (line == "quit"):
				break
			elif (line == "help"):
				help()
	except:
		all
	
interpretor()
print ("bye")

