#!/usr/bin/python
# -*- coding:utf8 -*

s = "Hello Frédéric!\n"

print s
print s.lower()
print s.lower().capitalize().center(30)
print s.lower().capitalize().center(30).strip()

prenom = 'Johne'
nom = 'Doe'
age = 99
chaine = "My name is {0} {1} and I am {2} years old.".format(prenom, nom, age)
print nom[0]
print nom[2]
print nom[-1]
print prenom[1:-2]

print

adresse = """
{no_rue}, {nom_rue}
{code_postal} {nom_ville} ({pays})
""".format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")

print(adresse)
print "bye"

