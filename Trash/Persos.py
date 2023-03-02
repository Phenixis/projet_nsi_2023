class Perso:

    def __init__(self, prenom, pokemon, metier):
        self.phrase = str()
        self.prenom = prenom
        self.pokemon = []
        self.metier = []

    def interaction(self):
        dis(self.phrase)
        ...

    def def_interaction(self, dialogue):
        self.phrase = dialogue
        ...


def dis(text):
    print(text)


Red = Perso("Red", ["Salamèche"], ["Dresseur"])
Pecheur = Perso("Erwan", ["Tentacool"], ["Dresseur", "Pêcheur"])


# Red.def_interaction("Je te défie !")
# Red.interaction()
#
# Red.def_interaction("Tu es encore là toi !")
# Red.interaction()



def defie(perso: Perso):
    perso.interaction()
    if perso.metier == "Dresseur":
        perso.def_interaction("Je te défie !")
        perso.interaction()

# defie(Perso)
