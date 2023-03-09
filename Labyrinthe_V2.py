import networkx as nx
from random import choice
import pygame as pg
from keyboard import is_pressed
import pygame
from time import sleep

WIDTH = 15
HEIGHT = 15

pygame.init()

WHITE = (255, 255, 255)
GREY = (20, 20, 20)
BLACK = (0, 0, 0)
PURPLE = (100, 0, 100)
RED = (255, 0, 0)
clock = pygame.time.Clock()


class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)

        self.x = 0
        self.y = 0
        self.coor = [self.x * 50 + 25, self.y * 50 + 25]

    def update(self, dir: str):
        if dir == "r":
            self.x += 1
        if dir == "l":
            self.x -= 1
        if dir == "u":
            self.y -= 1
        if dir == "d":
            self.y += 1
        self.coor = [self.x * 50 + 25, self.y * 50 + 25]


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
            pg.draw.line(screen, (0, 0, 0), ((x + 1) * SIZE, y * SIZE), ((x + 1) * SIZE, (y + 1) * SIZE), 3)

        if (x, y + 1) not in g.neighbors((x, y)):  # mur horizontal
            pg.draw.line(screen, (0, 0, 0), (x * SIZE, (y + 1) * SIZE), ((x + 1) * SIZE, (y + 1) * SIZE), 3)

lst = []

for edge in g.edges:
    lst.append(edge)

joueur = Joueur()

go_on = True
while go_on:
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(joueur.coor[0], joueur.coor[1], 10, 10))
    for event in pygame.event.get():
        if "text" in event.dict.keys():
            if event.dict['text'] == 'escape':
                go_on = False
            if event.dict['text'] == 'q':
                if ((joueur.x, joueur.y), (joueur.x - 1, joueur.y)) in g.edges:
                    joueur.update("l")
            elif event.dict['text'] == 'd':
                if ((joueur.x, joueur.y), (joueur.x + 1, joueur.y)) in g.edges:
                    joueur.update("r")
            elif event.dict['text'] == 's':
                if ((joueur.x, joueur.y), (joueur.x, joueur.y + 1)) in g.edges:
                    joueur.update("d")
            elif event.dict['text'] == 'z':
                if ((joueur.x, joueur.y), (joueur.x, joueur.y - 1)) in g.edges:
                    joueur.update("u")

    screen.blit(joueur.image, joueur.coor)
    pg.display.update()
    clock.tick(60)

pygame.quit()
