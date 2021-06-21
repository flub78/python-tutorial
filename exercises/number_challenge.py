#!/usr/bin/python
# -*- coding:utf8 -*

"""
Trouver toutes les combinaisons d'opérateurs +,-,*,/ entre les entiers de 1 à 9 pour que le résultat soit égale à 100.
En l'absence d'opérateur, les entiers adjacents sont fusionnés, ex 3 4 5 donne 345
"""

operators = " +-*/"

def gen_one(op1, op2, op3, op4, op5, op6, op7, op8):
	"""
	Génére une expression à évaluer
	"""
	res = '1' + op1 + '2' + op2 + '3' + op3 + '4' + op4 + '5' + op5 + '6' + op6 + '7' + op7 + '8' + op8 + '9'
	return res.replace(" ", "")
	
def generator():
	""" Génere et évalue totues les expressions 5 puissance 8 = 390 625	
	"""
	cnt = 0
	# pour chaque opérateur dans chaque position on boucle sur les quatre opérateurs possibles
	# l'absence d'opérateur est considérée comme un opérateur
	for op1 in operators:
		for op2 in operators:
			for op3 in operators:
				for op4 in operators:
					for op5 in operators:
						for op6 in operators:
							for op7 in operators:
								for op8 in operators:
									# On génère l'expression
									res = gen_one(op1, op2, op3, op4, op5, op6, op7, op8)
									# On l'évalue
									val = int (eval(res))
									# Et on affiche seulement si cela vaut 100
									if (val == 100):
										cnt+=1
										print(str(cnt) +": " + res + " = " + str(val))

generator()
print("bye")

