#!/usr/bin/python
# -*- coding:utf8 -*
import re

print ("Regular expressions")

reg = r'abc'
if re.search(reg, 'abcdef'):
    print ("match abc")

reg = r'abc*'
if re.match(reg, 'abcccdef'):
    print ("match abc*")
    
reg = r'abc+'    
r = re.search(reg, 'abdef')   
print (r)
if (r):
    print ("match")    
else:
    print ("no match abc+")
print ("bye")


# find all C comments across several lines
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
text2 = '''/* this is a
    multiline comment */
    '''
print (comment.findall(text2))

# Metadata

str = "varchar(255)"
reg = r'(.+)\((.*)\)'
r = re.match(reg, str)
size = r.group(2)
print ('varchar(255) group 1', r.group(1))
print ('varchar(255) group 2', size)
print ('isDigit', size.isdigit())

str = "timestamp"
r = re.match(reg, str)      
print ('timestamp ', r)


str = "enum('light','dark')"
r = re.match(reg, str)
insideBrackets = r.group(2)
print ('enum ', insideBrackets)
print ('isDigit', size.isdigit())

str = "float(10.2)"
r = re.match(reg, str)
insideBrackets = r.group(2)

float_reg = r'(\d+)\.(\d+)'
print ('isFloat ', re.match(float_reg, insideBrackets))
print ('float ', insideBrackets)
print ('isDigit', insideBrackets.isdigit())
