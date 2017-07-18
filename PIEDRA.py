# -*- coding: utf-8 -*-
import time
from time import sleep
import random

def perdiste(jugador , pc ):
    sleep (1)
    if pc == "Tijera" and jugador == "Papel":
        sleep (1)
        print ("Perdiste, Tijeras cortan Papel")   
    elif pc == "Papel" and jugador == "Piedra":
        sleep (1)
        print ("Perdiste, Papel tapa Piedra")
    elif pc == "Piedra" and jugador == "Lagarto":
        sleep (1)
        print ("Perdiste, Piedra aplasta Lagarto")
    elif pc == "Lagarto" and jugador == "Spock":
        sleep (1)
        print ("Perdiste, Lagarto envenena Spock")
    elif pc == "Spock" and jugador == "Tijeras":
        sleep (1)
        print ("Perdiste, Spock Rompe Tijeras")
    elif pc == "Tijera" and jugador == "Lagarto":
        sleep (1)
        print ("Perdiste, Tijeras decapitan Lagarto")
    elif pc == "Lagarto" and jugador == "Papel":
        sleep (1)
        print ("Perdiste, Lagarto devora Papel")
    elif pc == "Papel" and jugador == "Spock":
        sleep (1)
        print ("Perdiste, Papel desautoriza Spock")
    elif pc == "Spock" and jugador == "Piedra":
        sleep (1)
        print ("Perdiste, Spock vaporiza Piedra")
    else:
        sleep (1)
        print ("Perdiste, Piedra aplasta Tijeras")
    

def play (jugador) :
    lista = ["Piedra" ,"Papel" ,"Tijera" ,"Lagarto" ,"Spock" ]
    pc = random.choice(lista)
    sleep(1)
    print (("La computadora elijió: {}.".format(pc)))
    if jugador == pc:
        print ("E M P A T E ")
    elif jugador == "Tijera" and pc == "Papel":
        sleep (1)
        print ("Ganaste, Tijeras cortan Papel")   
    elif jugador == "Papel" and pc == "Piedra":
        sleep (1)
        print ("Ganaste, Papel tapa Piedra")
    elif jugador == "Piedra" and pc == "Lagarto":
        sleep (1)
        print ("Ganaste, Piedra aplasta Lagarto")
    elif jugador == "Lagarto" and pc == "Spock":
        sleep (1)
        print ("Ganaste, Lagarto envenena Spock")
    elif jugador == "Spock" and pc == "Tijeras":
        sleep (1)
        print ("Ganaste, Spock Rompe Tijeras")
    elif jugador == "Tijera" and pc == "Lagarto":
        sleep (1)
        print ("Ganaste, Tijeras decapitan Lagarto")
    elif jugador == "Lagarto" and pc == "Papel":
        sleep (1)
        print ("Ganaste, Lagarto devora Papel")
    elif jugador == "Papel" and pc == "Spock":
        sleep (1)
        print ("Ganaste, Papel desautoriza Spock")
    elif jugador == "Spock" and pc == "Piedra":
        sleep (1)
        print ("Ganaste, Spock vaporiza Piedra")
    elif jugador == "Piedra" and pc == "Tijera":
        sleep (1)
        print ("Ganaste, Piedra aplasta Tijeras")
    else:
        perdiste(jugador , pc ) 
        
def run():

    while True:

        command = str(raw_input('''---  ---  ---  ---  ---  ---  ---  ---

            Bienvenido a Piedra Papel Tijera Lagarto Spock. ¿Qué deseas hacer?

            [R]eglas del juego
            [J]ugar
            [S]alir
        '''))
        command = command.upper()
        if command == 'R': 
            print ('''
                  Tijeras cortan Papel
                  Papel tapa Piedra
                  Piedra apasta Lagarto
                  Lagarto envenena Spock
                  Spock rompe tijeras
                  Tijeras decapitan Lagarto
                  Lagarto devora Papel
                  Papel desautoriza Spock
                  Spock vaporiza Piedra
                  Piera aplasta Tijeras ''')
            
            
        elif command == 'J':
            lista2 = ["Piedra" ,"Papel" ,"Tijera" ,"Lagarto" ,"Spock" ]
            jugador = str(raw_input('¿Qué opción elijes? Piedra Papel Tijera Lagarto Spock: '))
            jugador = jugador.capitalize()
            if jugador  not in lista2:        
                print "No hagas trampa!"
            else:        
                play(jugador)
            
        elif command == 'S':
            break
            
        else:
            print('¡Comando no reconocido!' )
            

if __name__ == '__main__':
    print('Piedra Papel Tijera Lagarto Spock')
    run()
