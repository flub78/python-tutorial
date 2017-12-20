#!/usr/bin/python
# -*- coding:utf8 -*
import os
import pexpect

print (os.name)

if (os.name != "nt"):
    print ("pexpect example\n")
    child = pexpect.spawn ('ftp ftp.openbsd.org')
    child.expect ('Name .*: ')
    child.sendline ('anonymous')
    child.expect ('Password:')
    child.sendline ('noah@example.com')
    child.expect ('ftp> ')
    child.sendline ('cd pub')
    child.expect('ftp> ')
    child.sendline ('get ls-lR.gz')
    child.expect('ftp> ')
    child.sendline ('bye')
else:
    print ("not supported on windows")
print ("bye")

