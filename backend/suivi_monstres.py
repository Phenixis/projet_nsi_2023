from time import sleep
from Labyrinthe_V2 import *


terrain = [[0 for _ in range(5)] for __ in range(5)]

terrain[0][0] = 2
terrain[1][4] = 7
terrain[1][0] = 7
terrain[2][0] = 7
terrain[2][1] = 7
terrain[1][0] = 7
terrain[0][2] = 7
terrain[0][3] = 7
terrain[1][3] = 7
terrain[3][3] = 7
terrain[4][3] = 7
terrain[4][1] = 7

terrain[4][4] = 4
# for ligne in terrain:
#     print(ligne)
#
# x = 0
# y = 0
# while terrain[4][4] != 2:
#     print('\b'*1000)
#     if terrain[3][4] != 2:
#         if terrain[x][y + 1] in [0, 4]:
#             terrain[x][y] = 0
#             y += 1
#             terrain[x][y] = 2
#         if terrain[x + 1][y] in [0, 4]:
#             terrain[x][y] = 0
#             x += 1
#             terrain[x][y] = 2
#         for ligne in terrain:
#             print(ligne)
#             sleep(1)
#     else:
#         terrain[x][y] = 0
#         x += 1
#         terrain[x][y] = 2
#         sleep(1)
#         print(ligne)


'''

------------------------------------------------------------------------------------------------------------------------
        Déterminer un ratio pour chaque case, plus le ratio est petit, plus il est proche de la sortie
------------------------------------------------------------------------------------------------------------------------

'''


position_monstre = x, y

neighbors(position_monstre)

n = 10

for _ in range(n)
    neighbors(x,y)