from constants import *


class Pokemon:
    def __init__(self, nom: str, type: str, caps: list, statut: str, stats: dict):
        self.nom = nom
        self.type = type
        self.caps = caps
        self.statut = statut
        self.stats = stats

    def utilise_sur(self, nb: int, other):
        nb_rand = randint(0, 100)
        precision = int((100 * self.stats['precision'] * self.caps[nb].precision)*(1-other.stats["esquive"]))
        list_nb = range(precision)
        print(f"{nb_rand=}")
        print(f"{precision=}%")
        print(f"{list_nb=}")
        if nb_rand in list_nb:
            print("attaqué")
        else:
            print("non-attaqué")
