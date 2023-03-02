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
    if terrain[x][y + 1] == 0:
        y+=1
        terrain[x][y] = 2
    if terrain[x + 1][y] == 0:
        x+=1
        terrain[x][y] = 2
    for ligne in terrain:
        print(ligne)
    sleep(2)