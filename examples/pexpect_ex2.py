#!/usr/bin/python
# -*- coding:utf8 -*
import pexpect
import os

def print_result(str):
    print ("===== =====\n", str, "..... .....")
    
if (os.name != "nt"):   
    print ("pexpect example\n")
    child = pexpect.spawn ('ftp')
    child.expect ('ftp> ')
    child.sendline ('help')
    child.expect ('ftp> ')
    print_result(child.before)
    
    child.sendline ('ls')
    child.expect ('ftp> ')
    print_result( child.before)
    
    child.sendline ('quit')
else:
    print ("not supported on windows")

print ("bye")

