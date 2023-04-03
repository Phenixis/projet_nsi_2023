from main import *

def joue():
    # --- screen ---
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen.fill(BG)

    # --- boutons ---
    BOUTON_LEVEL_3 = pygame.Rect(WIDTH // 2.3, 300, 200, 100)

    pygame.draw.rect(screen, BG, BOUTON_LEVEL_3)

    list_boutons = [[BOUTON_LEVEL_3, WHITE]]


    # --- font ---
    font = pygame.font.Font("interface/Maze.ttf", 200)
    titre_MAZE = font.render("MAZE", False, 'white')
    font = pygame.font.Font("interface/Maze.ttf", 40)
    text_button_level_3 = font.render("LEVEL 3", False, 'white')

    list_text = [(titre_MAZE, (WIDTH//2.9, 25)), (text_button_level_3, (WIDTH // 2.15, 325))]

    go_on = True
    while go_on:
        for event in pygame.event.get():
            if "key" in event.dict and event.dict['key'] == 27:
                go_on = False

            # Fonctionnement boutons
            elif BOUTON_LEVEL_3.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return app(3)

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

    return ""

def jouer():
    if joue() == "rejouer":
        jouer()
    else:
        pygame.quit()
        return ""

jouer()