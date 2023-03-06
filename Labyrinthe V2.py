import networkx as nx
from random import choice, sample
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import pygame as pg
from keyboard import is_pressed

WIDTH = 15
HEIGHT = 15


def neighbors(x: int, y: int) -> list[tuple[int, int]]:
    """
    Renvoie la liste des cases 'voisines' de (x,y) par leur position, pas nécessairement connectées
    """
    dxmin = -1 if x > 0 else 0
    dxmax = 1 if x < WIDTH - 1 else 0
    dymin = -1 if y > 0 else 0
    dymax = 1 if y < HEIGHT - 1 else 0
    return [(x + dx, y) for dx in range(dxmin, dxmax + 1) if dx != 0] + [(x, y + dy) for dy in range(dymin, dymax + 1)
                                                                         if dy != 0]


def propagate(x, y, new) -> None:
    """
    utilise un parcours en profondeur pour propager une valeur dans toutes les cellules d'une même région
    """
    stack = [(x, y)]
    old = region[x, y]
    while stack:
        x, y = stack.pop()
        region[x, y] = new
        for n in neighbors(x, y):
            if region[n] == old:
                stack.append(n)


region = {}
i = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        region[(x, y)] = i
        i += 1

colors = WIDTH * HEIGHT
g = nx.Graph()
g.add_nodes_from(list(region.keys()))

while colors > 1:
    x1, y1 = choice(list(region.keys()))
    x2, y2 = choice(neighbors(x1, y1))
    if region[x1, y1] != region[x2, y2]:
        g.add_edge((x1, y1), (x2, y2))
        propagate(x1, y1, region[x2, y2])
        colors -= 1

positions = {(x, y): (0.5 * x, 0.5 * (HEIGHT - y)) for (x, y) in region.keys()}
nx.draw_networkx_nodes(g, pos=positions, node_size=100)
nx.draw_networkx_edges(g, pos=positions)
SIZE = 50  # taille à l'écran

pg.init()
screen = pg.display.set_mode((WIDTH * 50, HEIGHT * 50))

pg.draw.rect(screen, (255, 255, 255), pg.Rect(0, 0, WIDTH * 50, HEIGHT * 50))

pg.draw.line(screen, (0, 0, 0), (0, 0), (WIDTH * 50, 0), 5)
pg.draw.line(screen, (0, 0, 0), (WIDTH * 50, 0), (WIDTH * 50, HEIGHT * 50), 5)
pg.draw.line(screen, (0, 0, 0), (WIDTH * 50, HEIGHT * 50), (0, HEIGHT * 50), 5)
pg.draw.line(screen, (0, 0, 0), (0, HEIGHT * 50), (0, 0), 5)

for x in range(WIDTH):
    for y in range(HEIGHT):
        if (x + 1, y) not in g.neighbors((x, y)):  # mur vertical
            pg.draw.line(screen, (0, 0, 0), ((x + 1) * SIZE, y * SIZE), ((x + 1) * SIZE, (y + 1) * SIZE), 5)
        if (x, y + 1) not in g.neighbors((x, y)):  # mur horizontal
            pg.draw.line(screen, (0, 0, 0), (x * SIZE, (y + 1) * SIZE), ((x + 1) * SIZE, (y + 1) * SIZE), 5)

go_on = True
while go_on:
    if is_pressed("esc"):
        go_on = False
    pg.display.update()
