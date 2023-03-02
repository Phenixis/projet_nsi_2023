terrain = [['' for _ in range(10)] for __ in range(10)]


terrain[0][0] = 'x'
terrain[1][0] = '0'
terrain[9][9] = '@'
for ligne in terrain:
    print(ligne)
