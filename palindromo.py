# -*- coding: utf-8 -*-
   
def palindromo(palabra):

        reverso = palabra[::-1]

        if reverso == palabra:
                print ('La palabra {} si es un palindromo'.format(palabra))
        else:
                print ('La palabra {} no es un palindromo'.format(palabra))  
        
if __name__== "__main__" :

    palabra = str(raw_input('Ingrese la palabra: '))

    palindromo(palabra)
