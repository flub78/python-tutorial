#!/usr/bin/python
# -*- coding:utf8 -*
print "Sets\n"

# playing with sets
autoreferenced = {"elt1", "elt2"}
set2 = {"elt1", "elt3"}
set2.add("elt4")
set2 |= {"elt5", "elt6"}

print "autoreferenced = ", autoreferenced
# forbidden
# autoreferenced.add(autoreferenced) 

set3 = autoreferenced.union(set2)
set3.remove("elt5")
print "set3 =", set3

intersection = autoreferenced.intersection(set2)
print "intersection = ", intersection

print "bye"

