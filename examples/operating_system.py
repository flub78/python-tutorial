#!/usr/bin/python
# -*- coding:utf8 -*

import os

print ("os\n")

dir_path = os.path.dirname(os.path.realpath(__file__))
print (dir_path)

cwd = os.getcwd()
print (cwd) 

print (os.system('ftp -h'))

print ("bye")

