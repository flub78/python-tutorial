#!/usr/bin/python
# -*- coding:utf8 -*
print "Lists\n"

mylist = [1, 2]
mylist.append(3)
mylist = mylist + [4, 5]
mylist.remove(4)
del mylist [0]
for elt in mylist:
	print elt
print "mylist = ", mylist
	
for i, elt in enumerate(mylist):
	print "tab[", i, "] = ", elt

board = [
  ['.', 'O', 'X'],
  ['.', 'X', '.'],
  ['O', 'X', 'O'],
]

print board
for row in board:
	print row

# -------------------------------------------------------------------------------------------
s = "Good morning America"
print s
l = s.split()
print l
s2 = "-".join(l)
print s2

def multi_params(*params):
	print "multi_params"
	for elt in params:
		print elt
		
multi_params(1, 2, 3, 4)
multi_params(*l)

liste_origine = [0, 1, 2, 3, 4, 5]
squares = [nb * nb for nb in liste_origine]
print squares

liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print [nb for nb in liste_origine if nb % 2 == 0]


inventaire = [
("pommes", 22),
("melons", 4),
("poires", 18),
("fraises", 76),
("prunes", 51) ]


print "bye"

