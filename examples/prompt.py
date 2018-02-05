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
	while True:
		try:
			# line = raw_input(">: ")	python 2.7 version
			line = input(">: ")
			print (line)
			if (line == "quit"):
				break
			elif (line == "help"):
				help()
		except Exception as e:
			print ("User exception caught")
			print (e)
#	except:
#		all
	
interpretor()
print ("bye")
input()

