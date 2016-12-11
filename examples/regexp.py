#!/usr/bin/python
# -*- coding:utf8 -*
import re

print "Regular expressions"

if re.search(r'abc', 'abcdef'):
    print "match"

if re.match(r'abc*', 'abcccdef'):
    print "match"
    print r'\1'
    
r = re.search(r'abc+', 'abdef')   
print r
if (r):
    print "match"    
else:
    print "no match"
print "bye"


# find all C comments across several lines
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
text2 = '''/* this is a
    multiline comment */
    '''
print comment.findall(text2)

