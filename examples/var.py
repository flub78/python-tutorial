#!/usr/bin/python
# -*- coding:utf8 -*

a = 10
print type(a)

b = 'hello' + " world" + """!"""
print b, " is a ", type(b)

c = 3.1415928
c += 1
print c, " is a ", type(c)

f = lambda x: x + 1
c,f = f,c           # swap
print type(c)

nbr_complex= 1j
 
print 2 + nbr_complex * 3
print nbr_complex.real # Afficher la Partie réelle
print nbr_complex.imag # Afficher la Partie imaginaire

print 1j * 1j

print "bye"

