from constants import *


class Joueur:

    def __init__(self, lst_comp: list[Comp], stats: dict, x_dep: int, y_dep: int):
        self.alive = True
        self.comps = lst_comp
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
        print(self.coor)

J1 = Joueur([...], {...: ...}, 0, 0)

J1.goes('up')
J1.goes('down', 5)