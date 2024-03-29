from time import time

from ressources.classes.Labyrinthe import *


def moving_in_the_graph(player, dir, graph, region, level):
    """
    Vérifie si la direction dans laquelle va le joueur a un mur ou non
    déplace le joueur dans la direction si possible
    """
    if dir in ['q', 'Q'] and ((
                               (player.column, player.row), (player.column - 1,
                                                             player.row)) in graph.edges or player.cross_mur) and not player.immobile:
        player.update('l', region, level)
    elif dir in ['d', 'D'] and ((
                                 (player.column, player.row), (player.column + 1,
                                                               player.row)) in graph.edges or player.cross_mur) and not player.immobile:
        player.update("r", region, level)
    elif dir in ['s', 'S'] and ((
                                 (player.column, player.row), (player.column,
                                                               player.row + 1)) in graph.edges or player.cross_mur) and not player.immobile:
        player.update("d", region, level)
    elif dir in ['z', 'Z'] and ((
                                 (player.column, player.row), (player.column,
                                                               player.row - 1)) in graph.edges or player.cross_mur) and not player.immobile:
        player.update("u", region, level)


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
        print(f"error : x_dep-x_arr={x_dep - x_arr} et y_dep-y_arr={y_dep - y_arr}")
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


def fastest_game(mod: str, level: int, winner: str):
    file = []
    with open("./parties.txt", "r", encoding="utf-8") as f:
        for row in f:
            row = row.split(" = ")[1].split(", ")
            row[0] = float(row[0][:-4]) # le temps
            row[1] = row[1][4:] # mod
            row[2] = int(row[2][-1]) # level
            row[3] = row[3][7:-1] if '\n' in row[3][7:] else row[3][7:] # winner
            file.append(row)

    result = [row[0] for row in file if row[1:] == [mod, level, winner]]

    return min(result) if result != [] else -1

