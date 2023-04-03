from constants import *

def rejoue():
    # --- screen ---
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen.fill(BG)

    # --- boutons ---
    BOUTON_REJOUER = pygame.Rect(WIDTH // 2.3, 300, 200, 100)
    BOUTON_QUITTER = pygame.Rect(WIDTH // 2.3, 500, 200, 100)

    pygame.draw.rect(screen, BG, BOUTON_REJOUER)
    pygame.draw.rect(screen, BG, BOUTON_QUITTER)
    list_boutons = [[BOUTON_REJOUER, WHITE], [BOUTON_QUITTER, WHITE]]


    # --- font ---
    font = pygame.font.Font("interface/Maze.ttf", 200)
    titre_MAZE = font.render("MAZE", False, 'white')
    font = pygame.font.Font("interface/Maze.ttf", 40)
    text_button_rejouer = font.render("REJOUER", False, 'white')
    text_button_quitter = font.render("QUITTER", False, 'white')
    list_text = [(titre_MAZE, (WIDTH//2.9, 25)), (text_button_rejouer, (WIDTH // 2.2, 325)),
                 (text_button_quitter, (WIDTH // 2.2, 525))]

    go_on = True
    while go_on:
        for event in pygame.event.get():
            if "key" in event.dict and event.dict['key'] == 27:
                go_on = False

            # Fonctionnement boutons
            elif BOUTON_REJOUER.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "rejouer"


            elif BOUTON_QUITTER.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "quitter"

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