class Case:
    def __init__(self, x: int, y: int, n=True, s=True, o=True, e=True):
        self.coor = (x, y)
        self.n: bool = n
        self.s: bool = s
        self.e: bool = e
        self.o: bool = o


    def __str__(self):
        return [self.coor, self.n, self.s, self.e, self.o]