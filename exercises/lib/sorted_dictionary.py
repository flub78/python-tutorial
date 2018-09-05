#!/usr/bin/python
# -*- coding:utf8 -*

""" Sorted Dictionary
"""

class SortedDictionary:
    
    def __init__(self, values = {}, **params):
        """ Constructor
            x = SortedDictionary(): generates an empty dictionary
            x = SortedDictionary(dict): initializes with another dict
            x = SortedDictionary(dict)
        """
        if type(values) not in (dict, SortedDictionary):
            raise TypeError("dictionary expected as first parameter")
            
        self._values = values 
        self._keys = list(values.keys()) # the list of keys will be kept sorted
        
        for k in params:
            self[k] = params[k]
        
    def __repr__(self):
        """ string representation of the dictionary
        """
        result = "{"
        cnt = 0
        for i in self._keys:
            if (cnt != 0):
                result += ", "
            result += "'" + str(i) + "': " + str(self[i])
            cnt += 1
        result += "}"
        return result
    
    def __len__(self):
        """ Length of the dictionary
        """
        return len(self._keys)

     
    def __getitem__(self, i):
        """ access to element at index i
        note that providing __getitem__ generates a default iterator
        """
        return self._values[i]
    
    def __setitem__(self, i, v):
        """ Set a value in the dictionary
        """
        if not i in self._keys:
            self._keys.append(i)
        self._values[i] = v
    
    def keys(self):
        return self._keys
    
    def items(self):
        return self._values.items()
        
#     def append(self, elt):
#         self._buffer.append(elt)
#         if len(self._buffer) > self._size:
#             del self._buffer[0]
#             
    def __add__(self, elt):
        """ To add two dictionaries with the + operator
        """
        for i in elt.keys():
            self[i] = elt[i]
        return self
# 
#             
#     def __contains__(self, v):
#         return v in self._buffer
    
    def sort(self):
        """ Sort the dictionary in alphabetical order"""
        self._keys.sort()
        
    def reverse(self):
        """ Sort the dictionary in reverse order"""
        self._keys.sort(reverse = True)

    def __iter__(self):
        """ returns an iterator on the dictionary
        note that providing this method disables the default iterator 
        """
        return DictIterator(self)
    
class DictIterator:
    """ An iterator for the dictionary
    """

    def __init__(self, dict):
        """ Constructor """
        self._i = 0
        self._dict = dict
        
    def __next__(self):
        """ Method to iterate, returns the next key
        """
        i = self._i
        self._i += 1
        if (self._i > len(self._dict._keys)):
            raise StopIteration
        # return self._dict._values[self._dict._keys(i)]
        return self._dict._keys[i]
    
# basic unit tests
if __name__ == "__main__":
    """ Some basic tests, """
    print ("testing")
    
