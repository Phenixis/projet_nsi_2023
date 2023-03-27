import Labyrinthe
from constants import *

class Joueur:
    """
    Crée un personnage
    """
    def __init__(self):
        self.width = 30
        self.height = 42

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        self.column = 0
        self.row = 0
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

        for case in region.keys():
            neighbors = Labyrinthe.neighbors(self.column, self.row)
            if case in neighbors:
                region[case][1] = True
            else:
                region[case][1] = False

        return region

    def define_coor(self):
        """
        Défini les coordonnées x et y du joueur
        """
        self.coor = [self.column * 50 + 10, self.row * 50 + 4]