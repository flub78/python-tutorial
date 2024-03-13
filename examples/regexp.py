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

"""
comma separated list of integers
"""
str1 = "1,2,3,4,5"
reg = r'(\d+),?'

r = re.match(reg, str1)
print (r.group(0))
print (re.findall(reg, str1))

"""
comma separated list of strings enclosed in single and double quotes
"""
str2 = "'a','b','c','d','e'"
str3 = '"a","b","c","d","e"'
str6 = '"a", "b", "c",  "d", "e"'

str4=""

str5 = "'a, b"

reg = r'\'(.+?)\',?'
reg2 = r'\"(.+?)\",?'

# reg to match single quoted or double quoted comma separated strings or empty string
reg3 = r'\'(.+?)\'|\"(.+?)\"|^$'

print(re.findall(reg, str2))
print("str2 ",re.match(reg2, str2))
print(re.findall(reg, str3))
print("str3 ",re.match(reg2, str3))

print('str2 and reg3', re.findall(reg3, str2))
print('str3 and reg3', re.findall(reg3, str3))
print('str4 and reg3', re.findall(reg3, str4))

print('str1 and reg3', re.findall(reg3, str1))
print('str5 and reg3', re.findall(reg3, str5))
print('str6 and reg3', re.findall(reg3, str6))


