#!/usr/bin/python
# -*- coding:utf8 -*

print ("Exceptions!\n")

try:
	var = 1 / 0
except Exception as e:
	print ("Division by 0 caught")
	print (e)

try:
	raise Exception('spam', 'egg')
except Exception as e:
	print ("User exception caught")
	print (e)
finally:
	print ("Everything is OK")	

try:
	raise Exception('Are you crazy?')
except Exception as e:
	print ("Another user exception caught")
	print (e)
finally:
	print ("Everything is OK")	

try:
	assert(False)
except Exception as e:
	print ("Exception raised by a failed assertion")
	print (e)

print ("bye")

