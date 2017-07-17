# -*- coding: utf-8 -*-
def final (numero):

	if numero < 2:
		return False
	elif numero == 2:
		return True
	elif numero > 2 and numero%2 == 0:
		return False
	else:
		for i in range(3,numero-1):
			if numero % i == 0:
				return False		
	return True 

def primos ():
	numero = int (raw_input('Ingresa el numero a valorar: '))
	resultado = final(numero)


	if resultado is True:
		print ("El número es primo")
	else:
		print ("El número NO es primo")


if __name__== "__main__" :
  primos ()  
