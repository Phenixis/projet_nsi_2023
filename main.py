from constants import *

# --- screen ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
screen.fill(BG)

# --- valeurs ---
start_mob = False
go_on = True
nb_monstre = 0
region, graph = main(screen)

# --- joueurs ---
joueur = Joueur(0, 0, RED) # joueur 1
joueur.update("nowhere", region)
monstres = [0, 0, 0] # 0 : monstre inactif, 1 : monstres actif
mob1 = Joueur(COLUMNS - 1, ROWS - 1, GREY) # bas-droite -> haut-gauche
mob1_path = Monstre(mob1, graph)
mob2 = Joueur(0, ROWS - 1, GREY) # bas-gauche -> haut-gauche
mob2_path = Monstre(mob2, graph)
mob3 = Joueur(COLUMNS - 1, 0, GREY) # haut-droite -> haut-gauche
mob3_path = Monstre(mob3, graph)

# --- bouttons ---
BOUTON_1 = pygame.Rect(1245, 200, 150, 50) # J2 : Comp Monstre
pygame.draw.rect(screen, BG, BOUTON_1)
BOUTON_2 = pygame.Rect(1245, 350, 150, 50) # J2 : Comp 2
pygame.draw.rect(screen, BG, BOUTON_2)
BOUTON_3 = pygame.Rect(1245, 500, 150, 50) # J2 : Comp 3
pygame.draw.rect(screen, BG, BOUTON_3)
BOUTON_4 = pygame.Rect(1245, 650, 150, 50) # J2 : Comp 4
pygame.draw.rect(screen, BG, BOUTON_4)
BOUTON_5 = pygame.Rect(75, 825, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_5)
BOUTON_6 = pygame.Rect(375, 825, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_6)
BOUTON_7 = pygame.Rect(675, 825, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_7)
BOUTON_8 = pygame.Rect(975, 825, 150, 50)
pygame.draw.rect(screen, BG, BOUTON_8)
list_buttons = [[BOUTON_1, WHITE], [BOUTON_2, WHITE], [BOUTON_3, WHITE], [BOUTON_4, WHITE]]
list_buttons_j1 = [BOUTON_5, BOUTON_6, BOUTON_7, BOUTON_8]
# --- font ---
font = pygame.font.Font("interface/Maze.ttf", 80)
titre_MAZE = font.render("MAZE", False, 'white')
font = pygame.font.Font("interface/Maze.ttf", 35)
text_monster = font.render("MONSTER", False, 'white')
text_button1 = font.render("BUTTON", False, 'white')
text_button2 = font.render("BUTTON", False, 'white')
text_button3 = font.render("BUTTON", False, 'white')
text_button5 = font.render("SHIELD----[1]", False, 'white')
text_button6 = font.render("CROSS-----[2]", False, 'white')
text_button7 = font.render("CPT 3------[3]", False, 'white')
text_button8 = font.render("CPT 4------[4]", False, 'white')
list_text = [(titre_MAZE, (1235, 50)), (text_monster, (1257, 207)), (text_button1, (1269, 357)),
             (text_button2, (1269, 507)), (text_button3, (1269, 657)), (text_button5, (103, 830)),
             (text_button6, (403, 830)), (text_button7, (703, 830)), (text_button8, (1003, 830))]


# --- fonction ---
def init_monstre(nb_monstre, monstres, graph):
    global mob1, mob1_path, mob2, mob2_path, mob3, mob3_path
    if event.type == pygame.MOUSEBUTTONDOWN and nb_monstre < 3:
        nb_monstre += 1
        if monstres[0] == 0:
            mob1 = Joueur(COLUMNS - 1, ROWS - 1, GREY)
            mob1_path = Monstre(mob1, graph)
            monstres[0] = 1
        elif monstres[1] == 0:
            mob2 = Joueur(0, ROWS - 1, GREY)
            mob2_path = Monstre(mob2, graph)
            monstres[1] = 1
        elif monstres[2] == 0:
            mob3 = Joueur(COLUMNS - 1, 0, GREY)
            mob3_path = Monstre(mob3, graph)
            monstres[2] = 1


while go_on:
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(joueur.coor[0], joueur.coor[1], joueur.width, joueur.height))
    for event in pygame.event.get():
        if "key" in event.dict and event.dict['key'] == 27:
            go_on = False
        elif BOUTON_1.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN and nb_monstre < 3:
                init_monstre(nb_monstre, monstres, graph)

        elif BOUTON_2.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                boutons_go_on = False

        elif BOUTON_3.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                boutons_go_on = False

        elif BOUTON_4.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                boutons_go_on = False
        if "text" in event.dict.keys():
            if event.dict['text'] == '&' and joueur.bouclier_end == 0:
                joueur.start_bouclier()

            if event.dict['text'] == 'é' and joueur.cross_mur_end == 0:
                joueur.start_cross_mur()

            moving_in_the_graph(joueur, event.dict['text'], graph, region)

    if region[(joueur.column, joueur.row)][-1] == 1:
        print("case d'arrivée atteinte !")
        go_on = False

    if region[(joueur.column, joueur.row)][2] and not joueur.bouclier:
        print("Vous êtes mort")
        go_on = False

    if LEVEL == 2:
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
            mob1_path.refresh_start(time(), graph, region)
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
            mob2_path.refresh_start(time(), graph, region)
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
            mob3_path.refresh_start(time(), graph, region)
            screen.blit(mob3_path.mob.image, mob3_path.mob.coor)
        if len(mob3_path.path_ending):
            mob3_path.refresh_ending(time(), region)
        if not (len(mob3_path.path_start) or len(mob3_path.path_ending)):
            if time() > mob3_path.time + CD_MOB:
                nb_monstre -= 1
                mob3_path.time = 0
                monstres[2] = 0
    if joueur.bouclier_end != 0:
        joueur.refresh_bouclier(time())
    if joueur.cross_mur_end != 0:
        joueur.refresh_cross_mur(time())

    for button in list_buttons:
        if button[0].collidepoint(pygame.mouse.get_pos()):
            button[1] = BLACK
            break
        else:
            button[1] = WHITE

    for (button, color) in list_buttons:
        pygame.draw.rect(screen, color, button, 5)

    for element in list_text:
        screen.blit(element[0], element[1])
    pygame.draw.rect(screen, WHITE, (1220, 0, 200, 800), 10, 5)
    pygame.draw.rect(screen, WHITE, (5, 810, 1195, 80), 10, 5)
    pygame.draw.rect(screen, WHITE, (1220, 810, 200, 80), 10, 5)
    for element in list_buttons_j1:
        pygame.draw.rect(screen, WHITE, element, 5)
    pygame.display.update()

pygame.quit()
