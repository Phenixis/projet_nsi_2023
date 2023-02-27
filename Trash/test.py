from Pokemon import *
from Capacite import *

pkmn1 = Pokemon("P1", "feu", [Capacite("normale", "physique", 35, 10, 100)], "normal", {"precision": 0.5, "esquive": 1})
pkmn2 = Pokemon("P2", "feu", [Capacite("normale", "physique", 35, 10, 100)], "normal", {"precision": 0.5, "esquive": 1})

pkmn1.utilise_sur(0, pkmn2)