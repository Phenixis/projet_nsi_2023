import pygame
from constants import *

pygame.init()

font = pygame.font.Font("Maze.ttf", 80)
titre_MAZE = font.render("MAZE", False, 'white')
font = pygame.font.Font("Maze.ttf", 35)
text_monster = font.render("MONSTER", False, 'white')
font = pygame.font.Font("Maze.ttf", 35)
text_button1 = font.render("BUTTON", False, 'white')
font = pygame.font.Font("Maze.ttf", 35)
text_button2 = font.render("BUTTON", False, 'white')
text_button5 = font.render("SHIELD", False, 'white')
text_button6 = font.render("CROSS", False, 'white')
text_button7 = font.render("CPT 3", False, 'white')
text_button8 = font.render("CPT 4", False, 'white')



def blit(screen):
    pygame.draw.rect(screen, WHITE, (0, 0, 1200, 800))
    pygame.draw.rect(screen, WHITE, (1220, 0, 200, 800), 10, 5)
    screen.blit(titre_MAZE, (1235, 50))
    screen.blit(text_monster, (1257, 207))
    screen.blit(text_button1, (1269, 357))
    screen.blit(text_button2, (1269, 507))
    screen.blit(text_button2, (1269, 657))




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

BOUTON_5 = pygame.Rect(75, 825, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_5)

BOUTON_6 = pygame.Rect(375, 825, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_6)

BOUTON_7 = pygame.Rect(675, 825, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_7)

BOUTON_8 = pygame.Rect(975, 825, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_8)

list_buttons_j2 = [[BOUTON_1, WHITE], [BOUTON_2, WHITE], [BOUTON_3, WHITE], [BOUTON_4, WHITE]]
list_buttons_j1 = [[BOUTON_5, WHITE], [BOUTON_6, WHITE], [BOUTON_7, WHITE], [BOUTON_8, WHITE]]
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

    for button in list_buttons_j2:
        if button[0].collidepoint(pygame.mouse.get_pos()):
            button[1] = BLACK
            break
        else:
            button[1] = WHITE

    for (button, color) in list_buttons_j2:
        pygame.draw.rect(screen, color, button, 5)

    for (button, color) in list_buttons_j1:
        pygame.draw.rect(screen, color, button, 5)
        pygame.display.update()

    pygame.draw.rect(screen, WHITE, (0, 0, 1200, 800))
    pygame.draw.rect(screen, WHITE, (1220, 0, 200, 800), 10, 5)
    pygame.draw.rect(screen, WHITE, (5, 810, 1195, 80), 10, 5)
    pygame.draw.rect(screen, WHITE, (1220, 810, 200, 80), 10, 5)
    screen.blit(titre_MAZE, (1235, 50))
    screen.blit(text_monster,(1257,207))
    screen.blit(text_button1, (1269, 357))
    screen.blit(text_button2, (1269, 507))
    screen.blit(text_button2, (1269, 657))
    screen.blit(text_button5, (103, 830))
    screen.blit(text_button6, (403, 830))
    screen.blit(text_button7, (703, 830))
    screen.blit(text_button8, (1003, 830))
    pygame.display.flip()
