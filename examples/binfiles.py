#!/usr/bin/python
# -*- coding:utf8 -*
#
# Use files to save and restore objects
import pickle
import os

print "Binary files!\n"

score = {
  "joueur 1":    5,
  "joueur 2":   35,
  "joueur 3":   20,
  "joueur 4":    2,
}

filename = '/tmp/file.data'

# write
with open(filename, 'ab') as fd:
    pic = pickle.Pickler(fd)
    pic.dump(score)

assert(os.path.isfile(filename))    
    
# read
with open(filename, 'rb') as fd:
    pic = pickle.Unpickler(fd)
    score2 = pic.load()

assert (score == score2)

os.unlink(filename)

assert(not os.path.isfile(filename))    

print "bye"

