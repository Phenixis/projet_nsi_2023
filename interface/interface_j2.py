import random
import pygame
from time import sleep

pygame.init()

WHITE = (255, 255, 255)
GREY = (20, 20, 20)
BLACK = (0, 0, 0)
PURPLE = (100, 0, 100)
RED = (255, 0, 0)

size = (850, 850)
screen = pygame.display.set_mode(size)
screen.fill(GREY)


done = False

# -------- Main Program Loop -----------
go_on = True
while go_on:
    for event in pygame.event.get():
        print(event.dict)
        if "key" in event.dict:
            if event.dict["key"] == 27:
                go_on = False


    pygame.display.flip()

pygame.quit()
