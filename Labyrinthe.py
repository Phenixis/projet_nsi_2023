from constants import *
import networkx as nx
from random import choice
from Joueur import *

def neighbors(x: int, y: int) -> list:
    """
    Renvoie la liste des cases 'voisines' de (x,y) par leur position, pas nécessairement connectées
    """
    dxmin = -1 if x > 0 else 0
    dxmax = 1 if x < COLUMNS - 1 else 0
    dymin = -1 if y > 0 else 0
    dymax = 1 if y < ROWS - 1 else 0
    return [(x + dx, y) for dx in range(dxmin, dxmax + 1) if dx != 0] + [(x, y + dy) for dy in range(dymin, dymax + 1)
                                                                         if dy != 0]


def propagate(region, x, y, new) -> None:
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


def draw_lab(surface, g):
    """
    Dessine le labyrinthe
    """
    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(0, 0, COLUMNS * 50, ROWS * 50)) # background
    pygame.draw.line(surface, (0, 0, 0), (0, 0), (COLUMNS * 50, 0), 5) # ligne du haut
    pygame.draw.line(surface, (0, 0, 0), (COLUMNS * 50, 0), (COLUMNS * 50, ROWS * 50), 5) # ligne de droite
    pygame.draw.line(surface, (0, 0, 0), (COLUMNS * 50, ROWS * 50), (0, ROWS * 50), 5) # ligne du bas
    pygame.draw.line(surface, (0, 0, 0), (0, ROWS * 50), (0, 0), 5) # ligne de gauche

    for x in range(COLUMNS):
        for y in range(ROWS):
            if (x + 1, y) not in g.neighbors((x, y)):  # mur vertical
                pygame.draw.line(surface, (0, 0, 0), ((x + 1) * SIZE, y * SIZE), ((x + 1) * SIZE, (y + 1) * SIZE), 3)
            if (x, y + 1) not in g.neighbors((x, y)):  # mur horizontal
                pygame.draw.line(surface, (0, 0, 0), (x * SIZE, (y + 1) * SIZE), ((x + 1) * SIZE, (y + 1) * SIZE), 3)


def fill_region():
    """
    Rempli un dictionnaire nommé "region" des cases du labyrinthe avec une valeur de plus en plus grande
    Utile pour créer le graphe plus tard
    """
    region = {}
    i = 0
    for y in range(ROWS):
        for x in range(COLUMNS):
            region[(x, y)] = i
            i += 1

    return region


def define_graph(region):
    """
    Défini le graphe du labyrinthe permettant de dessigner les murs ensuite
    """
    nb_cases = COLUMNS * ROWS

    g = nx.Graph()
    g.add_nodes_from(list(region.keys()))

    while nb_cases > 1:
        x1, y1 = choice(list(region.keys()))
        x2, y2 = choice(neighbors(x1, y1))
        if region[x1, y1] != region[x2, y2]:
            g.add_edge((x1, y1), (x2, y2))
            propagate(region, x1, y1, region[x2, y2])
            nb_cases -= 1

    positions = {(x, y): (0.5 * x, 0.5 * (ROWS - y)) for (x, y) in region.keys()}

    nx.draw_networkx_nodes(g, pos=positions, node_size=100)
    nx.draw_networkx_edges(g, pos=positions)
    return g


def main(surface):
    """
    Rempli region, defini le graphe selon region
    Dessine le labyrinthe
    Renvoie le graphe
    """
    graphe = define_graph(fill_region())
    draw_lab(surface, graphe)
    return graphe