#!/usr/bin/python
# -*- coding:utf8 -*

"""
Unit tests for sorted dictionary

execution:
    python test_sorted_dictionary.py
    or
    python -m unittest discover
"""

from lib.sorted_dictionary import *
import unittest

class SortedDictionaryTest(unittest.TestCase):
    """ Test case for game engine """

    def test_basic(self):
        sd1 = SortedDictionary()
        print(sd1)
        self.assertFalse(len(sd1), "Length of empty dict == 0")
        
        dict = {"lion" : 4, "bird" : 2, "snake" : 0}
        sd2 = SortedDictionary(dict)
        print(sd2)
        self.assertEqual(len(sd2), 3, "Length of for objects created with dictionary")
        self.assertEqual(sd2["lion"], 4, "Check one value")
        self.assertEqual(sd2["snake"], 0, "Check another value")

        sd3 = SortedDictionary(dict, ant = 6, spider = 8)
        print(sd3)
        self.assertEqual(len(sd3), 5, "Length of for objects created with implicit dictionary")
        sd3.sort()
        print(sd3)
        sd3.reverse()
        print(sd3)
        
        sd4 = SortedDictionary(fish = 6, cat = 3)
        sd = sd3 + sd4
        print(sd)
        self.assertEqual(len(sd), 7, "Length after concatenation")
        
        for key in sd:
            print("key = > " + str(key))

        for key, val in sd.items():
            print("key = > " + str(key))

if __name__ == '__main__':        
    unittest.main()


