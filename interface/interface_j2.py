import pygame
from constants import *

pygame.init()

font = pygame.font.Font("Maze.ttf", 80)
titre_MAZE = font.render("MAZE", False, 'white')


screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
screen.fill(BG)

BOUTON_1 = pygame.Rect(1245, 200, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_1)

BOUTON_2 = pygame.Rect(1245, 350, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_2)

BOUTON_3 = pygame.Rect(1245, 500, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_3)

BOUTON_4 = pygame.Rect(1245, 650, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_4)

list_buttons = [[BOUTON_1, WHITE], [BOUTON_2, WHITE], [BOUTON_3, WHITE], [BOUTON_4, WHITE]]

boutons_go_on = True
while boutons_go_on:
    for event in pygame.event.get():
        if "key" in event.dict and event.dict['key'] == 27: # le numéro 27 renvoie à esc
            boutons_go_on = False

        elif BOUTON_1.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                boutons_go_on = False

        elif BOUTON_2.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                boutons_go_on = False

        elif BOUTON_3.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                boutons_go_on = False

        elif BOUTON_4.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                boutons_go_on = False

    for button in list_buttons:
        if button[0].collidepoint(pygame.mouse.get_pos()):
            button[1] = BLACK
            break
        else:
            button[1] = WHITE

    for (button, color) in list_buttons:
        pygame.draw.rect(screen, color, button, 5)

    pygame.draw.rect(screen, WHITE, (0, 0, 1200, 800))
    pygame.draw.rect(screen, WHITE, (1220, 0, 200, 800), 10, 5)
    screen.blit(titre_MAZE, (1235, 50))
    pygame.display.flip()
