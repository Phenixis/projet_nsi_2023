from random import randint
import pyxel
from Capacite import *
from Pokemon import *
from Persos import *

TYPES = {'physique': ["Acier", "Combat", "Insecte", "Normal", "Poison", "Roche", "Sol", "Spectre", "Vol"],
         'special': ["Dragon", "Eau", "Electrik", "Feu", "Glace", "Plante", "Psy", "Ténèbres"]}

STATUTS = ["eveille","brûlure", "gel", "paralysie", "empoisement", "sommeil", "confus"]

CAP = {"charge": Capacite("physique", "normal", 35, 40, 1)}
