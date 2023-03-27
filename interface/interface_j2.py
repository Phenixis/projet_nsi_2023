import pygame
from constants import *

pygame.init()

SCREEN_WIDTH, SCREEN_WEIGHT = 1450, 840

NOIR = (0)
BLANC = pygame.Color("#ffffff")
VERT = pygame.Color("#0e6f46")
BLEU = pygame.Color("#213035")
MARRON = pygame.Color("#774633")
PURPLE = (100, 0, 100)

font = pygame.font.Font("MAZE.ttf",80)

text_surf = font.render("MAZE", False, 'white')



screen = pygame.display.set_mode((1450, 840), pygame.FULLSCREEN)
screen.fill(BG)
go_on = True

BOUTON_1 = pygame.Rect(1245, 200, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_1)

BOUTON_2 = pygame.Rect(1245, 350, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_2)

BOUTON_3 = pygame.Rect(1245, 500, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_3)

BOUTON_4 = pygame.Rect(1245, 650, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_4)

lb = []
lb.append([BOUTON_1, BLANC])
lb.append([BOUTON_2, BLANC])
lb.append([BOUTON_4, BLANC])
lb.append([BOUTON_3, BLANC])

boutons_go_on = True
while boutons_go_on == True:
    for event in pygame.event.get():
        if "key" in event.dict and event.dict['key'] == 27:
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

    for b in lb:
        if b[0].collidepoint(pygame.mouse.get_pos()):
            b[1] = NOIR
            break
        else:
            b[1] = BLANC

    for (button, color) in lb:
        pygame.draw.rect(screen, color, button, 5)

    pygame.draw.rect(screen, BLANC, (0, 0, 1200, 800))
    pygame.draw.rect(screen, BLANC, (1220, 0, 200, 800), 10, 5)
    screen.blit(text_surf,(1235,50))
    pygame.display.flip()
