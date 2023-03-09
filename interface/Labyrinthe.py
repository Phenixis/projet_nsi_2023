import networkx as nx
from random import choice
import pygame

HEIGHT = 1450
WIDTH = 840
COLUMNS = 24  # nombre de colonnes
ROWS = 16  # nombre de lignes
SIZE = 50  # taille d'une case
WHITE = (255, 255, 255)
GREY = (20, 20, 20)
BLACK = (0, 0, 0)
PURPLE = (100, 0, 100)
RED = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()


class Joueur:

    def __init__(self):
        self.width = 30
        self.height = 42

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        self.x = 0
        self.y = 0
        self.coor = [0.0, 0.0]
        self.define_coor()

    def update(self, dir: str):
        if dir == "r":
            self.x += 1
        if dir == "l":
            self.x -= 1
        if dir == "u":
            self.y -= 1
        if dir == "d":
            self.y += 1
        self.define_coor()

    def define_coor(self):
        self.coor = [self.x * 50 + 10, self.y * 50 + 4]


def neighbors(x: int, y: int) -> list[tuple[int, int]]:
    """
    Renvoie la liste des cases 'voisines' de (x,y) par leur position, pas nécessairement connectées
    """
    dxmin = -1 if x > 0 else 0
    dxmax = 1 if x < COLUMNS - 1 else 0
    dymin = -1 if y > 0 else 0
    dymax = 1 if y < ROWS - 1 else 0
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


def draw_lab(surface):
    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(0, 0, COLUMNS * 50, ROWS * 50))

    pygame.draw.line(surface, (0, 0, 0), (0, 0), (COLUMNS * 50, 0), 5)
    pygame.draw.line(surface, (0, 0, 0), (COLUMNS * 50, 0), (COLUMNS * 50, ROWS * 50), 5)
    pygame.draw.line(surface, (0, 0, 0), (COLUMNS * 50, ROWS * 50), (0, ROWS * 50), 5)
    pygame.draw.line(surface, (0, 0, 0), (0, ROWS * 50), (0, 0), 5)

    for x in range(COLUMNS):
        for y in range(ROWS):
            if (x + 1, y) not in g.neighbors((x, y)):  # mur vertical
                pygame.draw.line(surface, (0, 0, 0), ((x + 1) * SIZE, y * SIZE), ((x + 1) * SIZE, (y + 1) * SIZE), 3)

            if (x, y + 1) not in g.neighbors((x, y)):  # mur horizontal
                pygame.draw.line(surface, (0, 0, 0), (x * SIZE, (y + 1) * SIZE), ((x + 1) * SIZE, (y + 1) * SIZE), 3)


def fill_region():
    region = {}
    i = 0

    for y in range(ROWS):
        for x in range(COLUMNS):
            region[(x, y)] = i
            i += 1

    return region


def define_graph():
    nb_cases = COLUMNS * ROWS

    g = nx.Graph()
    g.add_nodes_from(list(region.keys()))

    while nb_cases > 1:
        x1, y1 = choice(list(region.keys()))
        x2, y2 = choice(neighbors(x1, y1))
        if region[x1, y1] != region[x2, y2]:
            g.add_edge((x1, y1), (x2, y2))
            propagate(x1, y1, region[x2, y2])
            nb_cases -= 1

    positions = {(x, y): (0.5 * x, 0.5 * (ROWS - y)) for (x, y) in region.keys()}

    nx.draw_networkx_nodes(g, pos=positions, node_size=100)
    nx.draw_networkx_edges(g, pos=positions)
    return g


def main(screen):
    region = fill_region()
    g = define_graph()
    draw_lab(screen)


# joueur = Joueur()
#
# go_on = True
# while go_on:
#     pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(joueur.coor[0], joueur.coor[1], joueur.width, joueur.height))
#     for event in pygame.event.get():
#         if "key" in event.dict and event.dict['key'] == 27:
#             go_on = False
#         if "text" in event.dict.keys():
#             if event.dict['text'] == 'q' and ((joueur.x, joueur.y), (joueur.x - 1, joueur.y)) in g.edges:
#                 joueur.update("l")
#             elif event.dict['text'] == 'd' and ((joueur.x, joueur.y), (joueur.x + 1, joueur.y)) in g.edges:
#                 joueur.update("r")
#             elif event.dict['text'] == 's' and ((joueur.x, joueur.y), (joueur.x, joueur.y + 1)) in g.edges:
#                 joueur.update("d")
#             elif event.dict['text'] == 'z' and ((joueur.x, joueur.y), (joueur.x, joueur.y - 1)) in g.edges:
#                 joueur.update("u")
#
#     screen.blit(joueur.image, joueur.coor)
#     pygame.display.update()
#     clock.tick(60)
#
# pygame.quit()
