# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    
    |   |
        |
        |
        |
        |
        =''', '''

    
    |   |
    O   |
        |
        |
        |
        =''', '''

    
    |   |
    O   |
    |   |
        |
        |
        =''', '''

    
    |   |
    O   |
   /|   |
        |
        |
        =''', '''

    
    |   |
    O   |
   /|\  |
        |
        |
        =''', '''

   
    |   |
    O   |
   /|\  |
    |   |
        |
        =''', '''

    
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =''', '''

    
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =''', '''
''']

WORDS = [
   'efimero',
   'superfluo',
   'inefable',
   'inconmesurable'
   'etereo',
   'ojala',
   'luminiscencia',
   'compasion',
   'infinito',
   'ademan',
   'epoca',
   'bonhomia',
   'soledad',
   'resiliencia',
   'melancolia',
   'elocuencia',
   'efervescencia',
   'olvido',
   'sonambulo',
   'alba',
   'epifania',
   'incandescencia',
   'nostalgia',
   'aurora',
   'desenlace',
   
]


def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print(' ')
    print(hidden_word)
    print('---   ---   ---   ---   ---   --- ')

def run():
    word = random_word()
    hidden_word = ['--'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(raw_input('Escoge una letra: '))
        
        letter = []
        for i in range(len(word)):
                if word[i] == current_letter:
                        letter.append(i)
              
        if len(letter) == 0 :
                tries +=1
                if tries == 7 :
                        display_board(hidden_word, tries)
                        print (' ')
                        print ('Perdiste :( La palabra correcta era  {} ' .format(word))
                        break 
        else:
               for i in letter:
                        hidden_word[i] = current_letter     
        
        letter = []
        
        try:
                hidden_word.index('--')
        except ValueError:
                
                print (' ')
                print (' Felicidades encontraste la palabra')      
                break
                
if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()
