class Perso:

    def __init__(self, prenom, pokemon, metier):
        self.phrase = str()
        ...

    def interaction(self):
        dis(self.phrase)
        ...

    def def_interaction(self, dialogue):
        self.phrase = dialogue
        ...


def dis(text):
    print(text)


Red = Perso("Red", ["pkmn1"], "dresseur")
Red.def_interaction("Je te défie !")
Red.interaction()

Red.def_interaction("Tu es encore là toi !")
Red.interaction()
