#!/usr/bin/python
# -*- coding:utf8 -*

"""
Unit tests for the Ring module

execution:
    python test_ring.py
    or
    python -m unittest discover
"""


from ring import *
import unittest

r = Ring(4)

r + 1
r + 2
r + 3
print r

# Stange no iterator defined and it works ....
for elt in r:
    print elt


if __name__ == '__main__':        
    unittest.main()


