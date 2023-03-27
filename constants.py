from win32api import GetSystemMetrics
import pygame
from time import time

# Taille utiles
WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1)
SIZE = 50  # taille d'une case
COLUMNS = (WIDTH//SIZE)-4 # nombre de colonnes
ROWS = (HEIGHT//SIZE)-2 # nombre de lignes

# Couleur
WHITE = (255, 255, 255)
GREY = (20, 20, 20)
BLACK = (0, 0, 0)
PURPLE = (100, 0, 100)
RED = (255, 0, 0)
GREEN = (0, 102, 0)
YELLOW = (255, 204, 0)
WALL_COLOR = PURPLE
BG = BLACK

# Valeur constante
LEVEL = 1  # int(input("À quel niveau voulez-vous jouer ? "))