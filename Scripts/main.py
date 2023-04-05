from constants_dir.constants import *
from Scripts.rejoue import *


def app(level : int):
    # --- screen ---
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen.fill(BG)

    # --- valeurs ---
    start_mob = False
    go_on = True
    nb_monstre = 0
    region, graph = main(screen, level)
    time_0 = -1
    J2 = False

    # --- joueurs ---
    joueur = Joueur(0, 0, RED)  # joueur 1
    joueur.update("nowhere", region, level)
    monstres = [0, 0, 0]  # 0 : monstre inactif, 1 : monstres actif
    mob1 = Joueur(COLUMNS - 1, ROWS - 1, GREY)
    mob1_path = Monstre(mob1, graph, time())
    mob2 = Joueur(0, ROWS - 1, GREY)
    mob2_path = Monstre(mob2, graph, time())
    mob3 = Joueur(COLUMNS - 1, 0, GREY)
    mob3_path = Monstre(mob3, graph, time())

    # --- boutons ---
    BOUTON_1 = pygame.Rect(WIDTH - 175, 200, 150, 50)  # J2 : Comp Monstre
    BOUTON_2 = pygame.Rect(WIDTH - 175, 350, 150, 50)  # J2 : Comp Immobilisation
    BOUTON_3 = pygame.Rect(WIDTH - 175, 500, 150, 50)  # J2 : Comp 3
    BOUTON_4 = pygame.Rect(WIDTH - 175, 650, 150, 50)  # J2 : Comp 4
    BOUTON_5 = pygame.Rect(((COLUMNS * SIZE) - 5) / 4 - 195, HEIGHT - 75, 150, 50)
    BOUTON_6 = pygame.Rect(((COLUMNS * SIZE) - 5) / 4 + 105, HEIGHT - 75, 150, 50)
    BOUTON_7 = pygame.Rect(((COLUMNS * SIZE) - 5) / 4 + 405, HEIGHT - 75, 150, 50)
    BOUTON_8 = pygame.Rect(((COLUMNS * SIZE) - 5) / 4 + 705, HEIGHT - 75, 150, 50)
    pygame.draw.rect(screen, BG, BOUTON_1)
    pygame.draw.rect(screen, BG, BOUTON_2)
    pygame.draw.rect(screen, BG, BOUTON_3)
    pygame.draw.rect(screen, BG, BOUTON_4)
    pygame.draw.rect(screen, BG, BOUTON_5)
    pygame.draw.rect(screen, BG, BOUTON_6)
    pygame.draw.rect(screen, BG, BOUTON_7)
    pygame.draw.rect(screen, BG, BOUTON_8)
    list_buttons_j2 = [[BOUTON_1, WHITE], [BOUTON_2, WHITE], [BOUTON_3, WHITE], [BOUTON_4, WHITE]]
    list_buttons_j1 = [BOUTON_5, BOUTON_6, BOUTON_7, BOUTON_8]
    # --- font ---
    font = pygame.font.Font("./ressources/Font/Maze.ttf", 71)
    titre_MAZE = font.render("MAZE", False, 'white')
    font = pygame.font.Font("./ressources/Font/Maze.ttf", 35)
    text_button_monster = font.render("MONSTER", False, 'white')
    text_button1 = font.render("STUNT", False, 'white')
    text_button2 = font.render("BUTTON 3", False, 'white')
    text_button3 = font.render("BUTTON 4", False, 'white')
    text_button5 = font.render("SHIELD------[1]", False, 'white')
    text_button6 = font.render("CROSS-------[2]", False, 'white')
    text_button7 = font.render("CPT 3--------[3]", False, 'white')
    text_button8 = font.render("CPT 4--------[4]", False, 'white')
    list_text = [(titre_MAZE, (WIDTH - 177, 25)), (text_button_monster, (WIDTH - 165, 207)),
                 (text_button1, (WIDTH - 165, 357)),
                 (text_button2, (WIDTH - 165, 507)), (text_button3, (WIDTH - 165, 657)),
                 (text_button5, (((COLUMNS * SIZE) - 5) / 4 - 185, HEIGHT - 70)),
                 (text_button6, (((COLUMNS * SIZE) - 5) / 4 + 115, HEIGHT - 70)),
                 (text_button7, (((COLUMNS * SIZE) - 5) / 4 + 415, HEIGHT - 70)),
                 (text_button8, (((COLUMNS * SIZE) - 5) / 4 + 715, HEIGHT - 70))]

    # --- fonction ---
    def init_monstre(nb_monstre, monstres, graph, mob1, mob1_path, mob2, mob2_path, mob3, mob3_path):
        nb_monstre += 1
        if monstres[0] == 0:
            mob1 = Joueur(COLUMNS - 1, ROWS - 1, GREY)
            mob1_path.init(mob1, graph, time())
            monstres[0] = 1
        elif monstres[1] == 0:
            mob2 = Joueur(0, ROWS - 1, GREY)
            mob2_path.init(mob2, graph, time())
            monstres[1] = 1
        elif monstres[2] == 0:
            mob3 = Joueur(COLUMNS - 1, 0, GREY)
            mob3_path.init(mob3, graph, time())
            monstres[2] = 1
        return mob1, mob1_path, mob2, mob2_path, mob3, mob3_path

    def compteur():
        actual_time = int(time())
        time_secs = actual_time - time_0 if time_0 != -1 else 0
        sexe = str(int(time_secs % 60))
        if int(sexe) < 10:
            sexe = '0' + sexe
        min = str(int(time_secs // 60))
        if int(min) < 10:
            min = '0' + min
        text = pygame.font.Font("./ressources/Font/Maze.ttf", 60).render(min + ":" + sexe, False, 'white')
        pygame.draw.rect(screen, BLACK, (WIDTH - 180, HEIGHT - 80, 160, 60))
        screen.blit(text, (WIDTH - 164, HEIGHT - 80))

    def end_game(winner, level):
        print(str(int(time() - time_0)) + "secs")
        with open("./parties.txt", "a", encoding="utf-8") as f:
            date = dt.datetime.now()
            f.write(f"\n{date.day}:{date.month}:{date.year} - "
                    f"{date.hour}h{date.minute}min{date.second}secs = "
                    f"{str(time() - time_0)}secs, "
                    f"mod=J1{'&J2' if J2 else ''}, "
                    f"level={level}, "
                    f"winner={winner}")

    while go_on:
        pygame.draw.rect(screen, WHITE, pygame.Rect(joueur.coor[0], joueur.coor[1], joueur.width, joueur.height))
        for event in pygame.event.get():
            if "key" in event.dict and event.dict['key'] == 27:
                go_on = False

            # Fonctionnement boutons souris J2
            elif BOUTON_1.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN and nb_monstre < 3:
                    J2 = True
                    mob1, mob1_path, mob2, mob2_path, mob3, mob3_path = init_monstre(nb_monstre, monstres, graph, mob1,
                                                                                     mob1_path, mob2, mob2_path, mob3,
                                                                                     mob3_path)

            elif BOUTON_2.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN and joueur.immobile_end == 0 and not joueur.bouclier:
                    J2 = True
                    joueur.start_immobile()

            elif BOUTON_3.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    boutons_go_on = False

            elif BOUTON_4.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    boutons_go_on = False

            if "text" in event.dict.keys():
                if event.dict['text'] == '&' and joueur.bouclier_end == 0 and not joueur.immobile:
                    joueur.start_bouclier()

                if event.dict['text'] == 'é' and joueur.cross_mur_end == 0 and not joueur.immobile:
                    joueur.start_cross_mur()

                if joueur.slower:
                    sleep(0.2)

                if time_0 == -1:
                    time_0 = time()
                moving_in_the_graph(joueur, event.dict['text'], graph, region, level)

        if region[(joueur.column, joueur.row)][-1] == 1:
            print("case d'arrivée atteinte !")
            end_game("J1", level)
            # sleep(0.5)
            go_on = False

        if region[(joueur.column, joueur.row)][2] and not joueur.bouclier:
            print("Vous êtes mort")
            end_game("J2", level)
            go_on = False

        if level == 2:
            draw_case((joueur.column, joueur.row), screen, graph, region)
            draw_wall((joueur.column, joueur.row), screen, graph)
            if nb_monstre >= 1:
                draw_case((mob1.column, mob1.row), screen, graph, region)
                draw_wall((mob1.column, mob1.row), screen, graph)
            if nb_monstre >= 2:
                draw_case((mob2.column, mob2.row), screen, graph, region)
                draw_wall((mob2.column, mob2.row), screen, graph)
            if nb_monstre >= 3:
                draw_case((mob3.column, mob3.row), screen, graph, region)
                draw_wall((mob3.column, mob3.row), screen, graph)

        draw_lab(screen, graph, region)
        screen.blit(joueur.image, joueur.coor)

        if monstres[0] == 1:
            if len(mob1_path.path_start):
                mob1_path.refresh_start(time(), graph, region, level)
                screen.blit(mob1_path.mob.image, mob1_path.mob.coor)
            if len(mob1_path.path_ending):
                mob1_path.refresh_ending(time(), region)
            if not (len(mob1_path.path_start) or len(mob1_path.path_ending)):
                if time() > mob1_path.time + CD_MOB:
                    nb_monstre -= 1
                    mob1_path.time = 0
                    monstres[0] = 0

        if monstres[1] == 1:
            if len(mob2_path.path_start):
                mob2_path.refresh_start(time(), graph, region, level)
                screen.blit(mob2_path.mob.image, mob2_path.mob.coor)
            if len(mob2_path.path_ending):
                mob2_path.refresh_ending(time(), region)
            if not (len(mob2_path.path_start) or len(mob2_path.path_ending)):
                if time() > mob2_path.time + CD_MOB:
                    nb_monstre -= 1
                    mob2_path.time = 0
                    monstres[1] = 0

        if monstres[2] == 1:
            if len(mob3_path.path_start):
                mob3_path.refresh_start(time(), graph, region, level)
                screen.blit(mob3_path.mob.image, mob3_path.mob.coor)
            if len(mob3_path.path_ending):
                mob3_path.refresh_ending(time(), region)
            if not (len(mob3_path.path_start) or len(mob3_path.path_ending)):
                if time() > mob3_path.time + CD_MOB:
                    nb_monstre -= 1
                    mob3_path.time = 0
                    monstres[2] = 0

        if time_0 != -1:
            if joueur.bouclier_end != 0:
                joueur.refresh_bouclier(time())
            if joueur.cross_mur_end != 0:
                joueur.refresh_cross_mur(time())
            if joueur.immobile_end != 0:
                joueur.refresh_immobile(time())

        for button in list_buttons_j2:
            if button[0].collidepoint(pygame.mouse.get_pos()):
                button[1] = BLACK
                break
            else:
                button[1] = WHITE

        pygame.draw.rect(screen, WHITE, rect_comp_J1, 10, 5)
        pygame.draw.rect(screen, WHITE, rect_comp_J2, 10, 5)
        pygame.draw.rect(screen, WHITE, rect_chrono, 10, 5)

        for element in list_text:
            screen.blit(element[0], element[1])

        for element in list_buttons_j1:
            pygame.draw.rect(screen, WHITE, element, 5)

        for (button, color) in list_buttons_j2:
            pygame.draw.rect(screen, color, button, 5)

        compteur()
        pygame.display.update()
    return rejoue()
