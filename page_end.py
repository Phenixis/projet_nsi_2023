from main import *

# --- screen ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
screen.fill(BG)

# --- boutons ---
BOUTON_REJOUER = pygame.Rect(600, 300, 200, 100)
BOUTON_QUITTER = pygame.Rect(600, 500, 200, 100)

pygame.draw.rect(screen, BG, BOUTON_REJOUER)
pygame.draw.rect(screen, BG, BOUTON_QUITTER)
list_boutons = [[BOUTON_REJOUER, WHITE], [BOUTON_QUITTER, WHITE]]


# --- font ---
font = pygame.font.Font("interface/Maze.ttf", 71)
titre_MAZE = font.render("MAZE", False, 'white')
font = pygame.font.Font("interface/Maze.ttf", 35)
text_button_rejouer = font.render("REJOUER", False, 'white')
text_button_quitter = font.render("QUITTER", False, 'white')
list_text = [(titre_MAZE, (200, 25)), (text_button_rejouer, (600, 300)),
             (text_button_quitter, (600, 500))]

go_on = True
while go_on:
    for event in pygame.event.get():
        if "key" in event.dict and event.dict['key'] == 27:
            go_on = False

        # Fonctionnement boutons
        elif BOUTON_REJOUER.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                app()

        elif BOUTON_QUITTER.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                go_on = False

    for button in list_boutons:
        if button[0].collidepoint(pygame.mouse.get_pos()):
            button[1] = BLACK
            break
        else:
            button[1] = WHITE

    for element in list_text:
        screen.blit(element[0], element[1])

    for elt in list_boutons:
        pygame.draw.rect(screen, elt[1], elt[0], 5)


    pygame.display.update()

pygame.quit()