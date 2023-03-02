from constants import *


class Joueur:

    def __init__(self, lst_comp: list[Comp], stats: dict, x_dep: int, y_dep: int):
        self.alive = True
        self.comp1, self.comp2, self.comp3, self.comp4 = lst_comp
        self.stats = stats
        self.coor = [x_dep, y_dep]

    def goes(self, dir: str, val: int = 1):
        if dir == 'up':
            self.coor[1] -= val
        elif dir == 'down':
            self.coor[1] += val
        elif dir == 'left':
            self.coor[0] -= val
        elif dir == 'right':
            self.coor[0] += val
        print("Coordonées du joueur :\n\tx =", self.coor[0], "\n\ty =", self.coor[1])