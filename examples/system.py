#!/usr/bin/python
# -*- coding:utf8 -*

"""OS Interactions"""
import os

print "cwd = ", os.getcwd()
print "$HOME = ", os.getenv('HOME')
# print "login = ", os.getlogin()
print "pid = ", os.getpid()
print "directory content = ", os.listdir('.')

ls = os.system('ls -l')
print "ls -l = ", ls
print "ls = ", os.system('ls')

cmd = os.popen('ls -l')
ls2 = cmd.read()

print "bye"

