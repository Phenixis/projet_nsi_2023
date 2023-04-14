from win32api import GetSystemMetrics
from constants_dir.modules import *

# Taille utiles
WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1)
# print(WIDTH, HEIGHT)
SIZE = 50  # taille d'une case
COLUMNS = (WIDTH // SIZE) - 4  # nombre de colonnes
ROWS = (HEIGHT // SIZE) - 2  # nombre de lignes
NB_CASES = COLUMNS * ROWS

# Couleur
WHITE = (255, 255, 255)
GREY = (20, 20, 20)  # stunt
BLACK = (0, 0, 0)
PURPLE = (100, 0, 100)  # slow_motion
RED = (255, 0, 0)  # état normal
GREEN = (0, 200, 0)  # cross
DARK_GREEN = (0, 102, 0)  # case qui tue
YELLOW = (255, 204, 0)
BLUE = (0, 0, 255)  # shield
DARK_BLUE = (33, 48, 53)
GREEN_BJ = (14, 111, 70)  # couleur background blackjack
BROWN = (119, 70, 51)
WALL_COLOR = PURPLE
BG = BLACK

# Valeur constante
# LEVEL = 1  # int(input("À quel niveau voulez-vous jouer ? "))
CD_MOB = 17
CD_SHIELD = 5
CD_CROSS_MUR = CD_STUNT = 22

# Espaces d'affichage
rect_comp_J1 = pygame.Rect(5, HEIGHT - 90, (COLUMNS * SIZE) - 5, 80)
rect_comp_J2 = pygame.Rect(WIDTH - 190, 0, 180, HEIGHT - 100)
rect_chrono = pygame.Rect(WIDTH - 190, HEIGHT - 90, 180, 80)
