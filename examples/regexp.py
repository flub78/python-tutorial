#!/usr/bin/python
# -*- coding:utf8 -*
import re

print "Regular expressions"

reg = r'abc'
if re.search(reg, 'abcdef'):
    print "match abc"

reg = r'abc*'
if re.match(reg, 'abcccdef'):
    print "match abc*"
    print r"\1"
    
reg = r'abc+'    
r = re.search(reg, 'abdef')   
print r
if (r):
    print "match"    
else:
    print "no match abc+"
print "bye"


# find all C comments across several lines
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
text2 = '''/* this is a
    multiline comment */
    '''
print comment.findall(text2)

