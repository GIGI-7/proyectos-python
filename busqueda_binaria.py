
def binary(numeros, number_to_find, low, high):
        if low > high:
                return False
        mid = (low + high ) / 2 
        
        if numeros[mid] == number_to_find:
                return True
        elif numeros[mid] > number_to_find:
                return binary(numeros,number_to_find, low, mid-1)
        else: 
                return  binary(numeros,number_to_find, mid + 1, high)

if __name__ == '__main__':

        numeros = [1,3,4,5,6,9,10,11,25,27,28,34,36,49,51]
        number_to_find = int (raw_input('Ingresa un numero: '))
        
        result =  binary(numeros, number_to_find, 0, len(numeros) -1)
        if result == True:
                print ('El numero si esta en la lista')
        else:
                print ('El numero NO esta en la lista')
            
