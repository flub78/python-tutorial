#!/usr/bin/python
# -*- coding:utf8 -*

import os
from package.leap import *

year = input("type a year: ")
print "year=" + str(year)
if leap_year(year):
	print ("leap year")
else:
	print ("non leap year")

print "bye"
os.system("pause")



