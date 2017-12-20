#!/usr/bin/python

# Factoriel
def fact(n):
	""" Compute a factoriel
	
	type 'q' to exit
	"""
	if (n <= 1):
		return n
	else:
		return n * fact(n - 1)

nb = int(input("type an integer: "))
print ("fact(" + str(nb) + ") = " + str((fact(nb))))

help(fact)


