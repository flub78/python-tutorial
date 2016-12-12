#!/usr/bin/python
# -*- coding:utf8 -*

"""
How to use unittest

execution:
    python test_random.py
    or
    python -m unittest discover
"""

import random
import unittest
from posix import lstat

class RandomTest(unittest.TestCase):
    """ Test case for random """
    
    def test_choice(self):
        """ given: a list
            when: selecting a random elt
            then: it belongs ot the list
        """
        lst = list(range(10))
        print lst
        elt = random.choice(lst)
        print "random elt = ", elt
        self.assertIn(elt, lst)
        self.assertFalse(elt % 4 == 0, "True quite often")
        
    def test_shuffle(self):
        """
        given: a list
        when: shuffled
        then: it still contains the same elements
              likely in different order
        """
        lst = list(range(10))
        shuffled = list(lst) # deep copy
        random.shuffle(shuffled)
        print "lst =", lst
        print "shuffled= ", shuffled
        sorted = list(shuffled)
        sorted.sort()
        print "sorted = ", sorted
        same_order = True
        i = 0
        while i < 10:
            same_order = same_order and (lst[i] == shuffled[i])
            i += 1
        self.assertEqual(sorted, lst)
        self.assertFalse(same_order, "list are not in the same order after shuffling")

if __name__ == '__main__':        
    unittest.main()
