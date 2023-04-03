from constants_dir.fonctions import neighbors, time
from constants_dir.modules import pygame
from constants_dir.values import *


class Joueur:
    """
    Crée un personnage
    """

    def __init__(self, column, row, color):
        self.width = 30
        self.height = 42

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)

        self.column = column
        self.row = row
        self.coor = [0.0, 0.0]
        self.define_coor()

        self.bouclier = False
        self.bouclier_end = 0

        self.cross_mur = False
        self.cross_mur_end = 0

        self.immobile = False
        self.immobile_end = 0

        self.slower = False

    def verify_dir(self, dir, region):
        column, row = 0, 0
        if dir == "r":
            column = self.column + 1
        if dir == "l":
            column = self.column - 1
        if dir == "u":
            row = self.row - 1
        if dir == "d":
            row = self.row + 1

        return (column, row) in region

    def update(self, dir: str, region):
        """
        Permet un mouvement
        "r" correspond à "right"
        "l" correspond à "left"
        "u" correspond à "up"
        "d" correspond à "down"
        """
        if self.verify_dir(dir, region):
            if LEVEL == 3:
                for case in region.keys():
                    nghs = neighbors(self.column, self.row)
                    if case in nghs:
                        region[case][1] = False

            if dir == "r":
                self.column += 1
            if dir == "l":
                self.column -= 1
            if dir == "u":
                self.row -= 1
            if dir == "d":
                self.row += 1
            self.define_coor()

            region[self.column, self.row][1] = True
            if LEVEL == 3:
                for case in region.keys():
                    nghs = neighbors(self.column, self.row)
                    if case in nghs:
                        region[case][1] = True
            else:
                nghs = neighbors(self.column, self.row)

                for neighbor in nghs:
                    region[neighbor][1] = True

    def define_coor(self):
        """
        Défini les coordonnées x et y du joueur
        """
        self.coor = [self.column * 50 + 10, self.row * 50 + 5]

    def start_bouclier(self):
        self.bouclier_end = time() + 3
        self.bouclier = True
        self.image.fill(BLUE)

    def stop_bouclier(self, time):
        if self.bouclier:
            self.image.fill(RED)
        self.bouclier = False
        if time > self.bouclier_end + CD_SHIELD:
            self.bouclier_end = 0
        else:
            print(f"Cooldown bouclier : {self.bouclier_end + CD_SHIELD - time}")

    def refresh_bouclier(self, time):
        if time > self.bouclier_end:
            self.stop_bouclier(time)

    def start_cross_mur(self):
        self.cross_mur_end = time() + 0.5
        self.cross_mur = True
        self.image.fill(GREEN)

    def stop_cross_mur(self, time):
        if self.cross_mur:
            self.image.fill(RED)
        self.cross_mur = False
        if time > (self.cross_mur_end + CD_CROSS_MUR):
            self.cross_mur_end = 0
        else:
            print(f"Cooldown crossing walls : {self.cross_mur_end + CD_CROSS_MUR - time}")

    def refresh_cross_mur(self, time):
        if time > self.cross_mur_end:
            self.stop_cross_mur(time)

    def start_immobile(self):
        self.immobile_end = time() + 1.5
        self.immobile = True
        self.image.fill(GREY)

    def stop_immobile(self, time):
        if self.immobile:
            self.image.fill(RED)
        self.immobile = False
        if time > (self.immobile_end + CD_IMMOBILE):
            self.immobile_end = 0
        else:
            print(f"Cooldown immobile : {self.immobile_end + CD_IMMOBILE - time}")

    def refresh_immobile(self, time):
        if time > self.immobile_end:
            self.stop_immobile(time)