#!/usr/bin/python
# -*- coding:utf8 -*
import pexpect

def print_result(str):
    print "===== =====\n", str, "..... ....."
    
print "pexpect example\n"
child = pexpect.spawn ('ftp')
child.expect ('ftp> ')
child.sendline ('help')
child.expect ('ftp> ')
print_result(child.before)

child.sendline ('ls')
child.expect ('ftp> ')
print_result( child.before)

child.sendline ('quit')

print "bye"

