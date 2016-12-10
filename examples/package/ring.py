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
		
# unit tests

if __name__ == "__main__":
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
	
