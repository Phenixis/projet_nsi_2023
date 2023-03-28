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
joueur = Joueur(0, 0, RED)
joueur.update("nowhere", region)
monstres = [0, 0, 0]
mob1 = Joueur(COLUMNS - 1, ROWS - 1, GREY)
mob1_path = Monstre(mob1, graph)
mob2 = Joueur(0, ROWS - 1, GREY)
mob2_path = Monstre(mob2, graph)
mob3 = Joueur(COLUMNS - 1, 0, GREY)
mob3_path = Monstre(mob3, graph)


while go_on:
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(joueur.coor[0], joueur.coor[1], joueur.width, joueur.height))
    for event in pygame.event.get():
        if "key" in event.dict and event.dict['key'] == 27:
            go_on = False
        if "text" in event.dict.keys():
            if event.dict['text'] == 'm' and nb_monstre < 3:
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
    pygame.display.update()

pygame.quit()
