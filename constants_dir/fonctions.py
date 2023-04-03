from constants_dir.values import *

from Labyrinthe import *
from time import time


def moving_in_the_graph(player, dir, graph, region):
    """
    Vérifie si la direction dans laquelle va le joueur a un mur ou non
    déplace le joueur dans la direction si possible
    """
    if dir == 'q' and ((
    (player.column, player.row), (player.column - 1, player.row)) in graph.edges or player.cross_mur) and not player.immobile:
        player.update('l', region)
    elif dir == 'd' and ((
            (player.column, player.row), (player.column + 1, player.row)) in graph.edges or player.cross_mur) and not player.immobile:
        player.update("r", region)
    elif dir == 's' and ((
            (player.column, player.row), (player.column, player.row + 1)) in graph.edges or player.cross_mur) and not player.immobile:
        player.update("d", region)
    elif dir == 'z' and ((
            (player.column, player.row), (player.column, player.row - 1)) in graph.edges or player.cross_mur) and not player.immobile:
        player.update("u", region)


def def_dir(coor_dep, coor_arr):
    x_dep, y_dep = coor_dep
    x_arr, y_arr = coor_arr
    if (x_dep - x_arr) == -1:
        return 'd'
    elif (x_dep - x_arr) == 1:
        return 'q'
    elif (y_dep - y_arr) == -1:
        return 's'
    elif (y_dep - y_arr) == 1:
        return 'z'
    else:
        print(f"error : x_dep-x_arr={x_dep-x_arr} et y_dep-y_arr={y_dep-y_arr}")
        return ''


def dfs_path(g, start, end) -> list:
    result = []
    pred = dict()
    pred[start] = None
    stack = []
    remaining = list(g.nodes)
    stack.append(start)
    remaining.remove(start)
    found = False
    current = None
    while stack and not found:
        current = stack.pop()
        if current == end:
            found = True
        for n in g.neighbors(current):
            if n in remaining:
                stack.append(n)
                if n not in pred:
                    pred[n] = current
                remaining.remove(n)
    if found:
        while current:
            result = [current] + result
            current = pred[current]
        return result
    return []

# def blit(screen):
#     pygame.draw.rect(screen, WHITE, (0, 0, 1200, 800))
#     pygame.draw.rect(screen, WHITE, (1220, 0, 200, 800), 10, 5)
#     screen.blit(titre_MAZE, (1235, 50))
#     screen.blit(text_monster, (1257, 207))
#     screen.blit(text_button1, (1269, 357))
#     screen.blit(text_button2, (1269, 507))
#     screen.blit(text_button2, (1269, 657))