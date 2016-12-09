#!/usr/bin/python
# -*- coding:utf8 -*

"""
TP 1

	Le joueur mise sur un numéro compris entre 0 et 49 (50 numéros en tout). En choisissant son numéro, il y dépose la somme qu'il souhaite miser.
	La roulette est constituée de 50 cases allant naturellement de 0 à 49. Les numéros pairs sont de couleur noire, les numéros impairs 
	sont de couleur rouge. Le croupier lance la roulette, lâche la bille et quand la roulette s'arrête, relève le numéro de la case dans 
	laquelle la bille s'est arrêtée. Dans notre programme, nous ne reprendrons pas tous ces détails « matériels » mais ces explications 
	sont aussi à l'intention de ceux qui ont eu la chance d'éviter les salles de casino jusqu'ici. Le numéro sur lequel s'est arrêtée la 
	bille est, naturellement, le numéro gagnant.

	Si le numéro gagnant est celui sur lequel le joueur a misé (probabilité de 1/50, plutôt faible), le croupier lui remet 3 fois la somme misée.

	Sinon, le croupier regarde si le numéro misé par le joueur est de la même couleur que le numéro gagnant 
	(s'ils sont tous les deux pairs ou tous les deux impairs). Si c'est le cas, le croupier lui remet 50 % de la somme misée. 
	Si ce n'est pas le cas, le joueur perd sa mise.
"""

import random

# Multiplication
def mult(n):
	i = 1
	while (i <= 10):
		print str(n), " * ", str(i), " = ", str(i * n)
		i += 1


if __name__ == "__main__":
	
	balance = 10
	
	while balance >= 0:
		print "your balance = ", balance
		cell = input('expected number: ')
		actual = random.randint(0, 49)
		balance -= 2
		print "real = ", actual
		if (actual == 0):
			pass
		elif cell == actual:
			balance += 49
			print "win"
		elif ((cell % 2) == (actual % 2)): 
			balance += 3
			print "color"
		
	print "you are broke"
