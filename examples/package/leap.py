#!/usr/bin/python
# -*- coding:utf8 -*

""" Module to compute leap year
"""

def leap_year(year):
	""" True when leap year
	"""

	if ((year % 400) == 0):
		return True
	elif ((year % 100) == 0):
		return False 
	elif ((year % 4) == 0):
		return True
	else:
		return False

# unit tests

if __name__ == "__main__":
  print "leap_year(2016) = ", leap_year(2016)
  print "leap_year(1900) = ", leap_year(1900)
  assert leap_year(2016)
  assert not leap_year(2015)
  assert leap_year(2000)
