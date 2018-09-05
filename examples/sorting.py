#!/usr/bin/python
# -*- coding:utf8 -*

print ("Sorting lists in Python\n")

prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
print ("la liste: ", prenoms)

print("sorted(): ", sorted(prenoms))

print("la liste non modifiée: ", prenoms)
prenoms.sort()

print ("la liste après .sort(): ", prenoms)

etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]

print (sorted(etudiants))

print (sorted(etudiants, key=lambda colonnes: colonnes[2]))

class Etudiant:

    """    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Etudiant {} (age={}, moyenne={})>".format(
                self.prenom, self.age, self.moyenne)
print ("bye")

