#!/usr/bin/python
# -*- coding:utf8 -*
import json

print ("Hello json!\n")

print (json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))

array = [1, 2, 3, 4, 5]
print (json.dumps(array))

print (json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': ')))

str_array = ['a', 'b', 'c']
print (json.dumps(str_array))

print ("bye")

