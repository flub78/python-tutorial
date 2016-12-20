#!/usr/bin/python
# -*- coding:utf8 -*

""" Circular buffer
"""

class Ring:
	
	def __init__(self, size):
		""" Constructor """
		self._size = size
		self._buffer = []
		
	def __str__(self):
		return "Ring: " + str(self._buffer)
	
	def __len__(self):
		return len(self._buffer)
	
	def __getitem__(self, i):
		""" access to element at index i
		note that providing __getitem__ generates a default iterator
		"""
		return self._buffer[i]
	
	def __setitem__(self, i, v):
		self._buffer[i] = v
	
	def append(self, elt):
		self._buffer.append(elt)
		if len(self._buffer) > self._size:
			del self._buffer[0]
			
	def __add__(self, elt):
		self.append(elt)

			
	def __contains__(self, v):
		return v in self._buffer
	
	def __iter__(self):
		""" returns an iterator on the ring
		note that providing this method disables the default iterator 
		"""
		return RingIterator(self)
		
class RingIterator:

	def __init__(self, ring):
		""" Constructor """
		self._i = 0
		self._ring = ring
		
	def next(self):
		i = self._i
		self._i += 1
		if (self._i > len(self._ring)):
			raise StopIteration
		return self._ring[i]
	
	
# basic unit tests
if __name__ == "__main__":
	""" Some basic tests, """
	t = Ring(3)
	# assert(t)
	t.append(1)
	t.append(2)
	assert(len(t) == 2)
	t.append(3)
	t.append(4)
	assert(len(t) == 3)
	print t
	assert(t[0] == 2)
	assert(t[2] == 4)
	t[2] = 5
	assert(t[2] == 5)
	assert(3 in t)		# strange, True even if __contains__ is not redefined
	
	t + 17
	print t
	
