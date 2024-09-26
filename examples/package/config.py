#!/usr/bin/python
# -*- coding:utf8 -*

"""
Configuration file
"""

verbose = True
user = "root"
password = ""
host = "localhost"
database = "test"

list_of_users = ["root", "user1", "user2"]
dict_of_users = {"root": "root", "user1": "user1", "user2": "user2"}

# unit tests

if __name__ == "__main__":
  print ("leap_year(2016) = ", leap_year(2016))
  print ("leap_year(1900) = ", leap_year(1900))
  assert leap_year(2016)
  assert not leap_year(2015)
  assert leap_year(2000)
