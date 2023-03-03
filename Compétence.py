from constants import *


class Comp:
    def __init__(self, joueur: str, nom: str):
        self.nom = nom

    def run(self):
        if self.nom == "Clonage":
            self.clonage()
        elif self.nom == "Bouclier":
            self.bouclier()
        elif self.nom == "Lampe torche":
            self.lampe_torche()
        elif self.nom == "Passage à travers un mur":
            self.passage_a_travers_un_mur()
        elif self.nom == "Charge":
            self.charge()
        elif self.nom == "Monstres":
            self.monstres()
        elif self.nom == "Fermer porte":
            self.fermer_porte()
        elif self.nom == "Murs invisibles":
            self.murs_invisibles()
        elif self.nom == "Rocket":
            self.rocket()

    def clonage(self):
        ...

    def bouclier(self):
        ...

    def lampe_torche(self):
        ...

    def passage_a_travers_un_mur(self):
        ...

    def charge(self):
        ...

    def monstres(self):
        ...

    def fermer_porte(self):
        ...

    def murs_invisibles(self):
        ...

    def rocket(self):
        ...
