#!/usr/bin/python
# -*- coding:utf8 -*

# Multiplication
def mult(nb):
	i = 1
	while (i <= 10):
		print str(nb), " * ", str(i), " = ", str(i * nb)
		i += 1
		
mult(3)


chaine = "Hello"

for lettre in chaine:
    print(lettre)
    
res = ""
for lettre in chaine:
    if lettre in "AEIOUYaeiouy": # lettre est une voyelle
        res += lettre
    else: # lettre est une consonne... ou plus exactement, lettre n'est pas une voyelle
        res += '*'
print res

i = 1
while i < 20: # Tant que i est inférieure à 20
    if i % 3 == 0:
        i += 4 # On ajoute 4 à i
        print("On incrémente i de 4. i est maintenant égale à", i)
        continue # On retourne au while sans exécuter les autres lignes
    elif i > 10:
    	break
    print("La variable i =", i)
    i += 1 # Dans le cas classique on ajoute juste 1 à i