from constants import *
from random import choice
go_on = True

width = 25
cols = int(size[0] / width)
rows = int(size[1] / width)

grid = []

for x in range(0, size[0], 25):
    for y in range(0, size[1], 25):
        grid.append(Case(x, y, choice([True, False]), choice([True, False]), choice([True, False]), choice([True, False])))

for case in grid:
    case.draw()

while go_on:
    if is_pressed("esc"):
        go_on = False
    pg.display.flip()

