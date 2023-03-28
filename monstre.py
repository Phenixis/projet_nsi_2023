from constants_dir.fonctions import *
from constants_dir.values import *


class Monstre:

    def __init__(self, mob_associe, graph):
        self.mob = mob_associe
        self.time = time()
        self.path = dfs_path(graph, (self.mob.column, self.mob.row), (0, 0))
        self.path_start = self.def_path()
        self.path_ending = self.def_path(base=1)

    def def_path(self, mult_tps=0.1, base=0):
        res = {}
        sec = base
        for coor in self.path:
            res[coor] = self.time + sec
            sec += mult_tps
        return res

    def refresh_start(self, time, graph, region):
        coor_mob, next_coor = list(self.path_start.keys())[:2]
        if len(self.path_start) >= 3:
            if len(self.path_start) and time >= self.path_start[coor_mob]:
                moving_in_the_graph(self.mob, def_dir(coor_mob, next_coor), graph, region)
                region[next_coor][2] = True
                self.path_start.pop(coor_mob)
        else:
            moving_in_the_graph(self.mob, def_dir(coor_mob, next_coor), graph, region)
            region[next_coor][2] = True
            self.path_start.clear()

    def refresh_ending(self, time, region):
        coor_mob, next_coor = list(self.path_ending.keys())[:2]
        if len(self.path_ending) >= 3:
            if len(self.path_ending):
                if time >= self.path_ending[coor_mob]:
                    region[next_coor][2] = False
                    self.path_ending.pop(coor_mob)
        else:
            region[coor_mob][2] = False
            region[next_coor][2] = False
            self.path_ending.clear()
