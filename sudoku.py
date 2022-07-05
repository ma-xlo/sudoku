#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system
from random import randint

matrix_player = [ [ ' ' for i in range(9) ] for j in range(9) ]
x_axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
y_axis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#y_axis = ['➊', '➋', '➌', '➍', '➎', '➏', '➐', '➑', '➒']


# for i in range(9):
#     seeder = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for j in range(9):
#         seeder_length = len(seeder)
#         rand_posix = randint(0, seeder_length - 1)
#         matrix_player[i][j] = seeder[rand_posix]
#         seeder.pop(rand_posix)

while 1:
    system('clear')

    print(' ┌───────────────────────────────────────┐')
    print(' │               SUDOKU-CLI              │')
    print(' ├───┬───┬───┬───┬───┬───┬───┬───┬───┬───┤')
    print(' │ # │ A │ B │ C │ D │ E │ F │ G │ H │ I │')
    print(' ├───┼───┴───┴───┴───┴───┴───┴───┴───┴───┤')

    for i in range(9):
        print(end=' ')
        print(f'│ {y_axis[i]} │', end= ' ')
        for j in range(9):
            if not j == 8 and not j == 2 and not j == 5:
                print(f'{matrix_player[i][j]} ¦', end= ' ')
            elif j == 2 or j == 5:
                print(f'{matrix_player[i][j]} │', end= ' ')
            else:
                print(f'{matrix_player[i][j]}', end= ' ')
        if j == 8:
            print('│')
        if i == 2 or i == 5:
            print(' │ - │ ──────────┼───────────┼────────── │')
    print(' └───┴───────────────────────────────────┘')

    cmd_input = str(input('  > '))
    x = cmd_input[0]
    y = int(cmd_input[1])
    n = int(cmd_input[3])

    for i in range(len(x_axis)):
        if(x == x_axis[i]):
            if(n < 1 or n > 9):
                continue
            else:
                matrix_player[y-1][i] = n

    """
    print(f'X axis: {cmd_input[0]}')
    print(f'Y axis: {cmd_input[1]}')
    print(f'Operator: {cmd_input[2]}')
    print(f'Number: {cmd_input[3]}') 
    """

