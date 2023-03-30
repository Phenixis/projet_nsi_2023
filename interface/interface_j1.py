import pygame

from constants_dir.values import BG
from constants_dir.values import *

pygame.init()



size = (1450, 840)
screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
screen.fill(GREY)

done = False

font = pygame.font.Font("MAZE.ttf",45)
text_bt1 = font.render("SHIELD", False, 'white')
text_bt2 = font.render("CROSS", False, 'white')
text_bt3 = font.render("CPT 3", False, 'white')
text_bt4 = font.render("CPT 4", False, 'white')

BOUTON_5 = pygame.Rect(20, 825, 150, 50)

pygame.draw.rect(screen, BG, BOUTON_5)

BOUTON_6 = pygame.Rect(320, 825, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_6)

BOUTON_7 = pygame.Rect(620, 825, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_7)

BOUTON_8 = pygame.Rect(920, 825, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_8)
lb = []
lb.append([BOUTON_1, WHITE])
lb.append([BOUTON_2, WHITE])
lb.append([BOUTON_3, WHITE])
lb.append([BOUTON_4, WHITE])


# -------- Main Program Loop -----------
go_on = True
while go_on:
    for event in pygame.event.get():
        print(event.dict)
        if "key" in event.dict:
            if event.dict["key"] == 27:
                go_on = False

            if event.dict["key"] == 49:
                # fonction compétence 1

                ...
            if event.dict["key"] == 50:
                # fonction compétence 2
                ...
            if event.dict["key"] == 51:
                # fonction compétence 3
                ...
            if event.dict["key"] == 52:
                # fonction compétence 4
                ...
    # for b in lb:
    #     if b[0].collidepoint(pygame.mouse.get_pos()):

    for (button, color) in lb:
        pygame.draw.rect(screen, color, button, 5)
        pygame.display.update()
    pygame.draw.rect(screen, WHITE, (0, 0, 1200, 800))
    pygame.draw.rect(screen, WHITE, (1220, 0, 200, 800), 10, 5)
    screen.blit(text_bt1, (37, 825))
    screen.blit(text_bt2, (337, 825))
    screen.blit(text_bt3, (637, 825))
    screen.blit(text_bt4, (937, 825))
    pygame.display.flip()

pygame.quit()
