from time import sleep

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
for ligne in terrain:
    print(ligne)

x = 0
y = 0
while terrain[4][4] != 2:
    print('\b'*1000)
    if terrain[3][4] != 2:
        if terrain[x][y + 1] in [0, 4]:
            terrain[x][y] = 0
            y += 1
            terrain[x][y] = 2
        if terrain[x + 1][y] in [0, 4]:
            terrain[x][y] = 0
            x += 1
            terrain[x][y] = 2
        for ligne in terrain:
            print(ligne)
            sleep(1)
    else:
        terrain[x][y] = 0
        x += 1
        terrain[x][y] = 2
        sleep(1)
        print(ligne)


'''

------------------------------------------------------------------------------------------------------------------------
        Déterminer un ratio pour chaque case, plus le ratio est petit, plus il est proche de la sortie
------------------------------------------------------------------------------------------------------------------------

ratio = 1000
for case in lab:
    if ratio de case == '':
        case.ratio = ratio
        ratio -= 1
          


'''
from Case import *
lab = {}

def best_chemin():
    #parcourir les chemins et garder le plus court
    ways = {}
    sortie = False



def ratio():
    ratio = 1000
    for case in way:
        if ratio == '':
            case.ratio = ratio
            ratio -= 1