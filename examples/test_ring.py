#!/usr/bin/python
# -*- coding:utf8 -*

from ring import *

r = Ring(4)

r + 1
r + 2
r + 3
print r

# Stange no iterator defined and it works ....
for elt in r:
    print elt

print "bye"



