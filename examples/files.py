#!/usr/bin/python
# -*- coding:utf8 -*

print ("Files!\n")

fd = open('files.py', 'r')

print (fd)
print (type(fd))

txt = fd.read()

fd.close()

# print txt

# or better
with open('files.py', 'r') as fd:
    txt2 = fd.read()
    
assert (txt == txt2)

print ("bye")

