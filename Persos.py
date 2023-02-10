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
