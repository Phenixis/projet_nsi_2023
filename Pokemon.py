from constants import *

class Pokemon:
    def __init__(self, nom: str, type: str, caps : list, statut: str, stats: dict):
        self.nom = nom
        self.type = type
        self.caps = caps
        self.statut = statut
        self.stats = stats

    def utilise_sur(self, nb: int, other: Pokemon):
        if randint(0, 100) in range(100*(self.stats['precision']*cap.precision)):
            print("attaqué")
        else:
            print("non-attaqué")
