from random import randint
import numpy as np

matrix_player = [ [ ' ' for i in range(9) ] for j in range(9) ]
seeder = [1, 2, 3, 4, 5, 6, 7, 8, 9]

y_axis = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(len(matrix_player))

for i in range(9):
    for j in range(9):
            randNum = seeder[randint(0, 8)]
            if randNum in matrix_player[i]:
                j -= 1
            else:
                matrix_player[i][j] = randNum