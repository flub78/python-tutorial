#!/usr/bin/python
# -*- coding:utf8 -*

""" The math module"""
import math
from fractions import Fraction
import random

print "5 ** 3 = ", 5 ** 3
print "math.pow(5, 3) = ", math.pow(5, 3)
print "math.sqrt(25) = ", math.sqrt(25)
print "math.radians(360) / 2 = ", math.radians(360) / 2
print "math.pi = ", math.pi
print "cos(pi / 2)", math.cos(math.pi / 2)
print "cos(0)", math.cos(0)

print Fraction(1, 2)
print Fraction(2, 4)
print Fraction(1, 2) + Fraction(1, 2)

print "random() = ", random.random()

print "bye"

