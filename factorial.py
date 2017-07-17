acum = 1
factorial = int(raw_input("Ingresa un numero "))
b = factorial
while factorial > 0 :
    acum= acum * factorial
    factorial = factorial -1
print ("El factorial del numero {} es %i".format(b)%acum ) 



def fac (x):
    if x == 0:
        return 1
    else:
        return x*fac(x-1)
        
print fac(5)
       
