from constants import *

class Monstre:

    def __init__(self, mob_associe, path, actual_time, path_start, path_ending):
        self.mob = mob_associe
        self.path = path
        self.actual_time = actual_time
        self.path_start = path_start
        self.path_ending = path_ending

    def refresh_start(self, time, region):
        coor_mob, next_coor = list(self.path_start.keys())[:2]
        if len(self.path_start) >= 3:
            if len(self.path_start) and time >= self.path_start[coor_mob]:
                moving_in_the_graph(self.mob, def_dir(coor_mob, next_coor), region)
                region[next_coor][2] = True
                self.path_start.pop(coor_mob)
        else:
            moving_in_the_graph(mob, def_dir(coor_mob, next_coor), region)
            self.path_start.clear()

    def refresh_ending(self, time, region):
        coor_mob, next_coor = list(self.path_ending.keys())[:2]
        if len(self.path_ending) >= 3:
            if len(self.path_ending) and time >= self.path_ending[coor_mob]:
                region[next_coor][2] = False
                self.path_ending.pop(coor_mob)
        else:
            region[coor_mob][2] = False
            region[next_coor][2] = False
            self.path_ending.clear()