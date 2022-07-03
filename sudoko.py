from os import system
from random import seed
from random import randint
import numpy as np

matrizJogador = [ [ ' ' for i in range(9) ] for j in range(9) ]
seeder = [1, 2, 3, 4, 5, 6, 7, 8, 9]

coordenadaX = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'}
coordenadaY = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(9):
    for j in range(9):
        randNum = seeder[randint(0, 8)]
        if randNum in matrizJogador[i]:
            j -= 1
        else:
            matrizJogador[i][j] = randNum


system('clear')

print(' ┌───────────────────────────────────────┐')
print(' │               SUDOKU-CLI              │')
print(' ├───┬───┬───┬───┬───┬───┬───┬───┬───┬───┤')
print(' │ # │ A │ B │ C │ D │ E │ F │ G │ H │ I │')
print(' ├───┼───┴───┴───┴───┴───┴───┴───┴───┴───┤')

for i in range(9):
    print(end=' ')
    print(f'│ {coordenadaY[i]} │', end= ' ')
    for j in range(9):
        if not j == 8 and not j == 2 and not j == 5:
            print(f'{matrizJogador[i][j]} ¦', end= ' ')
        elif j == 2 or j == 5:
            print(f'{matrizJogador[i][j]} │', end= ' ')
        else:
            print(f'{matrizJogador[i][j]}', end= ' ')
    if j == 8:
        print('│')
    if i == 2 or i == 5:
        print(' │ - ├───────────────────────────────────┤')
print(' └───┴───────────────────────────────────┘')
print('                  Command: ')


