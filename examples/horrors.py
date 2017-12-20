#!/usr/bin/python
# -*- coding:utf8 -*

print ("Spooky Python features\n")

# Fixed in Python 3.x
# True = False 

# When method overloading is applied to basic types
# (I still do not understand why people consider that loose type checking or no type checking is considered 
# as a positive point). Either the language does the type checking or the programmer has to do it...
#
# Duck typing:
#  "If it walks like a duck and it quacks like a duck, then it must be a duck."
#
# Equivalent to Late binding, or dynamic binding
# mechanism in which the method being called upon an object or the function being called with arguments is looked up by name at runtime.
i = 3
print ("i * 3 = ", i * 3)
       
i = str(i)
print ("i * 3 = ", i * 3)

print ("bye")

