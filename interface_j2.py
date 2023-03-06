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

pygame.display.set_caption("EPIC MAZE")

done = False

clock = pygame.time.Clock()

width = 25
cols = int(size[0] / width)
rows = int(size[1] / width)

stack = []




# -------- Main Program Loop -----------
go_on = True
while go_on:
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(GREY)



        pygame.display.flip()

        clock.tick(150)
        sleep(1)


    ...

pygame.quit()


