#!/usr/bin/python
# -*- coding:utf8 -*

print ("Basic conditional instructions\n")

def even(a):
    if ((a % 2) == 0):
        print (a, "is even")
        if (a == 0):
            print (a, " == 0")
        return True
    else:
        print (a, "is odd")
        return False

even(5)
even(6)
even(0)

bln = even(6) 

if bln:
    print ("6 is even")
    
print ("bye")

