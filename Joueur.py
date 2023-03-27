import Labyrinthe
from constants import *

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

    def update(self, dir: str, region):
        """
        Permet un mouvement
        "r" correspond à "right"
        "l" correspond à "left"
        "u" correspond à "up"
        "d" correspond à "down"
        """
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
                neighbors = Labyrinthe.neighbors(self.column, self.row)
                if case in neighbors:
                    region[case][1] = True
                else:
                    region[case][1] = False
        else:
            neighbors = Labyrinthe.neighbors(self.column, self.row)

            for neighbor in neighbors:
                region[neighbor][1] = True
        return region

    def define_coor(self):
        """
        Défini les coordonnées x et y du joueur
        """
        self.coor = [self.column * 50 + 10, self.row * 50 + 4]