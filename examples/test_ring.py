#!/usr/bin/python
# -*- coding:utf8 -*

"""
Unit tests for the Ring module

execution:
    python test_ring.py
    or
    python -m unittest discover
"""


from package.ring import *
import unittest

# Stange no iterator defined and it works ....
# for elt in r:
#    print elt

class RingTest(unittest.TestCase):
    """ Test case for ring """

    def test_basic(self):
        r = Ring(4)
        self.assertTrue(len(r) == 0, "Correct length after creation")
        r + 1
        r + 2
        r + 3
        self.assertTrue(len(r) == 3, "Correct length")
        r + 4
        r + 5
        r + 6
        self.assertTrue(len(r) == 4, "Length has an upper limit")
        self.assertTrue(r[0] == 3, "First ring value")
        self.assertTrue(r[3] == 6, "First ring value")
        
        # cannot compare a ring and a list
        # self.assertTrue(r == [3, 4, 5, 6], "correct ring values")

        print (r)
        
    def test_iter(self):
        self.assertTrue(True, "check iteration")
        r = Ring(4)
        self.assertTrue(len(r) == 0, "Correct length after creation")
        r + 1
        r + 2
        r + 3
        r + 4
        r + 5
        i = 0
        for elt in r:
            print ('r[', i, '] =', elt)
            i += 1
        
        

if __name__ == '__main__':        
    unittest.main()


