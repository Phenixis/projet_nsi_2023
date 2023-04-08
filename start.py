from Scripts.main import *


def joue():
    # --- screen ---
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen.fill(BG)

    # ---boutons musique---
    BOUTON_MUSIQUE_1 = pygame.Rect(WIDTH - 1350, HEIGHT - 200, 90, 50)
    pygame.draw.rect(screen, BG, BOUTON_MUSIQUE_1)
    BOUTON_MUSIQUE_2 = pygame.Rect(WIDTH - 1250, HEIGHT - 200, 90, 50)
    pygame.draw.rect(screen, BG, BOUTON_MUSIQUE_2)
    BOUTON_MUSIQUE_3 = pygame.Rect(WIDTH - 1150, HEIGHT - 200, 90, 50)
    pygame.draw.rect(screen, BG, BOUTON_MUSIQUE_3)
    BOUTON_LOUDER = pygame.Rect(WIDTH - 670, HEIGHT - 200, 150, 50)
    pygame.draw.rect(screen, BG, BOUTON_LOUDER)
    BOUTON_QUIETER = pygame.Rect(WIDTH - 850, HEIGHT - 200, 150, 50)
    pygame.draw.rect(screen, BG, BOUTON_QUIETER)
    BOUTON_MUTE = pygame.Rect(WIDTH - 1000, HEIGHT - 200, 120, 50)
    pygame.draw.rect(screen, BG, BOUTON_MUTE)

    # ---music params---
    music = None
    volume = 0.5
    mute = False

    # --- boutons ---
    BOUTON_LEVEL_1 = pygame.Rect(WIDTH // 10, 300, 200, 100)
    pygame.draw.rect(screen, BG, BOUTON_LEVEL_1)
    BOUTON_LEVEL_2 = pygame.Rect(WIDTH // 2.3, 300, 200, 100)
    pygame.draw.rect(screen, BG, BOUTON_LEVEL_2)
    BOUTON_LEVEL_3 = pygame.Rect(WIDTH // 1.3, 300, 200, 100)
    pygame.draw.rect(screen, BG, BOUTON_LEVEL_3)
    list_boutons = [[BOUTON_LEVEL_1, WHITE], [BOUTON_LEVEL_2, WHITE], [BOUTON_LEVEL_3, WHITE],
                    [BOUTON_MUSIQUE_1, WHITE], [BOUTON_MUSIQUE_2, WHITE], [BOUTON_MUSIQUE_3, WHITE],
                    [BOUTON_LOUDER, WHITE], [BOUTON_QUIETER, WHITE], [BOUTON_MUTE, WHITE]]

    # --- font ---
    font = pygame.font.Font("./ressources/Font/Maze.ttf", 200)
    titre_MAZE = font.render("MAZE", False, 'white')

    font = pygame.font.Font("./ressources/Font/Maze.ttf", 40)
    text_button_level_1 = font.render("LEVEL 1", False, 'white')
    text_button_level_2 = font.render("LEVEL 2", False, 'white')
    text_button_level_3 = font.render("LEVEL 3", False, 'white')

    font = pygame.font.Font("./ressources/Font/Maze.ttf", 40)
    text_choose_music = font.render("SELECT YOUR MUSIC", False, 'white')
    text_music_1 = font.render("1", False, 'white')
    text_music_2 = font.render("2", False, 'white')
    text_music_3 = font.render("3", False, 'white')

    text_volume = font.render("VOLUME", False, 'white')
    text_mute = font.render("MUTE", False, 'white')
    font = pygame.font.Font("./ressources/Font/Maze.ttf", 40)
    text_louder = font.render("LOUDER", False, 'white')
    text_quieter = font.render("QUIETER", False, 'white')

    list_text = [(titre_MAZE, (WIDTH // 2.9, 25)),
                 (text_button_level_3, (WIDTH // 1.3 + 35, 325)),
                 (text_button_level_2, (WIDTH // 2.3 + 35, 325)),
                 (text_button_level_1, (WIDTH // 10 + 35, 325)),
                 (text_choose_music, (WIDTH - 1360, HEIGHT - 250)),
                 (text_music_1, (WIDTH - 1315, HEIGHT - 195)),
                 (text_music_2, (WIDTH - 1215, HEIGHT - 195)),
                 (text_music_3, (WIDTH - 1115, HEIGHT - 195)),
                 (text_volume, (WIDTH - 850, HEIGHT - 250)),
                 (text_mute, (WIDTH - 990, HEIGHT - 195)),
                 (text_quieter, (WIDTH - 840, HEIGHT - 195)),
                 (text_louder, (WIDTH - 660, HEIGHT - 195))]

    # -- fastest games --
    highscores = {}
    for mod in ("J1", "J1&J2"):
        for level in range(1, 4):
            for winner in ("J1", "J2"):
                score = fastest_game(mod, level, winner)
                highscores[(mod, level, winner)] = str(
                    round(score, 3)) + "secs" if score != -1 else "No score saved for these params"

    for score in highscores.keys():
        print(score)

    go_on = True

    while go_on:
        for event in pygame.event.get():

            if "key" in event.dict and event.dict['key'] == 27:
                go_on = False

            # Fonctionnement boutons
            elif BOUTON_LEVEL_1.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return app(1)

            elif BOUTON_LEVEL_2.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return app(2)

            elif BOUTON_LEVEL_3.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return app(3)

            elif BOUTON_MUSIQUE_1.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if music:
                        music.stop()
                    music = pygame.mixer.Sound("./ressources/Musique/no.wav")
                    music.play(-1)
                    music.set_volume(0.5)

            elif BOUTON_MUSIQUE_2.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if music:
                        music.stop()
                    music = pygame.mixer.Sound("./ressources/Musique/no.wav")
                    music.play(-1)
                    music.set_volume(0.5)

            elif BOUTON_MUSIQUE_3.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if music:
                        music.stop()
                    music = pygame.mixer.Sound("./ressources/Musique/no.wav")
                    music.play(-1)
                    music.set_volume(0.5)

            elif BOUTON_LOUDER.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if volume != 1:
                        volume += 0.1
                        music.set_volume(volume)

            elif BOUTON_QUIETER.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if volume != 0:
                        volume -= 0.1
                        music.set_volume(volume)

            elif BOUTON_MUTE.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not mute:
                        mute = True
                        music.set_volume(0)
                    else:
                        mute = False
                        music.set_volume(volume)

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
