from constants import *


class Case:
    def __init__(self, x: int, y: int, n=True, s=True, o=True, e=True):
        self.coor = (x, y)
        self.taille = 25

        self.is_current = False

        self.n: bool = n
        self.s: bool = s
        self.e: bool = e
        self.o: bool = o

    def draw(self):
        if self.is_current:
            pg.draw.rect(screen, RED, (self.coor[0], self.coor[1], self.taille, self.taille))
        else:
            pg.draw.rect(screen, WHITE, (self.coor[0], self.coor[1], self.taille, self.taille))
        if self.n:
            pg.draw.line(screen, BLACK, self.coor, (self.coor[0] + 25, self.coor[1]), 1)
        if self.s:
            pg.draw.line(screen, BLACK, (self.coor[0], self.coor[1] + 25), (self.coor[0] + 25, self.coor[1] + 25), 1)
        if self.e:
            pg.draw.line(screen, BLACK, (self.coor[0] + 25, self.coor[1]), (self.coor[0] + 25, self.coor[1] + 25), 1)
        if self.o:
            pg.draw.line(screen, BLACK, self.coor, (self.coor[0], self.coor[1] + 25), 1)

    def __repr__(self):
        return str([self.coor, self.n, self.s, self.e, self.o])
