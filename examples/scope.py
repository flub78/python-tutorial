#!/usr/bin/python
# -*- coding:utf8 -*

print ("Variable scope")

try:
    b += 2
    assert (False, "Exception not raise when a variable is referenced before to be used")
except Exception as e:
    print ("Expected exception raised when a variable is referenced before to be used")


a = 5

def print_a():
    a = 3
    print ("a = ", a)
    a += 1
    print ("a = ", a)
    
    def print_b():
        global a
        a +=1
        print ("global a = ", a)
    print_b()
    
print_a()

print ("a = ", a)

print ("bye")

