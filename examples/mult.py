#!/usr/bin/python

# Multiplication
def mult(n):
	i = 1
	while (i <= 10):
		print str(n), " * ", str(i), " = ", str(i * n)
		i += 1

if __name__ == "__main__":
	nb = input("type an integer: ")
	mult(nb)

