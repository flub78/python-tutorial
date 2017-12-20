#!/usr/bin/python
# -*- coding:utf8 -*
print ("Dictionaries\n")

# playing with dictionaries
hash = {}
hash["key"] = "DEAFDBEEF"
hash["name"] = "John Doe"

print ("Hello", hash["name"])
print ('hash = ', hash)
print ("keys:")
for key in hash:
	print ("\t", key)

print ("values:")
for key, val in hash.items():
	print ("\t", key, " => ", val)

# utilisation des tuples comme clé
board = {}
board['a', 1] = "tour blanche"

placard = {"chemise" : 3, "chaussures" : 4}
print ("placard = ", placard)
del placard['chemise']
print ("placard = ", placard)

print ("bye")

