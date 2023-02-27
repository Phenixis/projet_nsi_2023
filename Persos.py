class Perso:

    def __init__(self, phrase, prenom, pokemon, metier):
        self.phrase = "Je suis " + metier[1] + " et " + phrase
        self.prenom = prenom
        self.pokemon = pokemon
        self.metier = metier

    def interaction(self):
        dis(self.phrase)

    def def_interaction(self, dialogue):
        self.phrase = dialogue


def dis(text):
    print(text)


Red = Perso("test", "Red", ["Salamèche"], ["Dresseur", "Rival"])
Pecheur = Perso("Tu viens me déranger durant ma pêche ! Je te défie", "Erwan", ["Tentacool"], ["Dresseur", "un pêcheur"])

# Red.def_interaction("Je te défie !")
# Red.interaction()
#
# Red.def_interaction("Tu es encore là toi !")
# Red.interaction()



