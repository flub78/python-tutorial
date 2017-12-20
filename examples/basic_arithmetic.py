#!/usr/bin/python
# -*- coding:utf8 -*

import math

print ("Python basic arithmetic\n")

a = 3
b = 6

pi = 3.1415926

sumab = a + b
subst = a - b
mult = a * b
div = a / b
mod = a % b
fact = math.factorial(b)
powab = math.pow(a, b)
cosinus = math.cos(pi / 2)

print (a, " + ", b, " = ", sumab)
print (a, " - ", b, " = ", subst)
print (a, " * ", b, " = ", mult)
print (a, " / ", b, " = ", div)
print (a, " % ", b, " = ", mod)
print ("fact(", b, ") = ", fact)
print (a, " powab ", b, " = ", powab)

print ("cos(pi / 2) = ", cosinus)
print ("sin(pi / 2) = ", math.sin(pi / 2))
print ("sqrt(2) = ", math.sqrt(2))

print ("bye")

