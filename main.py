from Labyrinthe import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

screen.fill(BG)
graph, region = main(screen, LEVEL)
joueur = Joueur(0, 0, RED)
mob = Joueur(COLUMNS - 1, ROWS - 1, GREY)
joueur.update("nowhere", region)
start_mob = False
go_on = True
path_arr_dep = dfs_path(graph, (COLUMNS - 1, ROWS - 1), (0, 0))
path_start = {}
path_ending = {}
actual_time = 0


def def_path(path, time, multiplicateur=0.5, base=0):
    sec = base
    for coor in path_arr_dep:
        path[coor] = time + sec
        sec += multiplicateur


def moving_in_the_graph(player: Joueur, dir: str, region):
    """
    Vérifie si la direction dans laquelle va le joueur a un mur ou non
    déplace le joueur dans la direction si possible
    """
    if dir == 'q' and ((player.column, player.row), (player.column - 1, player.row)) in graph.edges:
        player.update('l', region)
    elif dir == 'd' and (
            (player.column, player.row), (player.column + 1, player.row)) in graph.edges:
        player.update("r", region)
    elif dir == 's' and (
            (player.column, player.row), (player.column, player.row + 1)) in graph.edges:
        player.update("d", region)
    elif dir == 'z' and (
            (player.column, player.row), (player.column, player.row - 1)) in graph.edges:
        player.update("u", region)


def def_dir(coor_dep, coor_arr):
    x_dep, y_dep = coor_dep
    x_arr, y_arr = coor_arr
    if (x_dep - x_arr) == -1:
        return 'd'
    elif (x_dep - x_arr) == 1:
        return 'q'
    elif (y_dep - y_arr) == -1:
        return 's'
    elif (y_dep - y_arr) == 1:
        return 'z'
    else:
        print(f"error : {x_dep-x_arr=} et {y_dep-y_arr=}")
        return ''


def refresh_start(time, mob: Joueur):
    """
    vérifie pour la première valeur de path si son temps d'éxecution est atteint
    si oui, déplace le mob sur les coordonnées et supprime la première valeur de `path`
    """
    global path_start
    coor_mob0, next_coor0 = list(path_start.keys())[:2]
    if len(path_start) >= 3:
        if len(path_start) and time >= path_start[coor_mob0]:
            moving_in_the_graph(mob, def_dir(coor_mob0, next_coor0), region)
            region[next_coor0][2] = True
            path_start.pop(coor_mob0)
    else:
        moving_in_the_graph(mob, def_dir(coor_mob0, next_coor0), region)
        path_start.clear()


def refresh_ending(time):
    """
        vérifie pour la première valeur de path si son temps d'éxecution est atteint
        si oui, déplace le mob sur les coordonnées et supprime la première valeur de `path`
    """
    global path_ending
    coor_mob, next_coor = list(path_ending.keys())[:2]
    if len(path_ending) >= 3:
        if len(path_ending) and time >= path_ending[coor_mob]:
            region[next_coor][2] = False
            path_ending.pop(coor_mob)
    else:
        region[coor_mob][2] = False
        region[next_coor][2] = False
        path_ending.clear()


while go_on:
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(joueur.coor[0], joueur.coor[1], joueur.width, joueur.height))
    for event in pygame.event.get():
        if "key" in event.dict and event.dict['key'] == 27:
            go_on = False
        if "text" in event.dict.keys():
            if event.dict['text'] == 'e' and actual_time == 0:
                mob = Joueur(COLUMNS - 1, ROWS - 1, GREY)
                actual_time = time()
                def_path(path_start, actual_time)
                def_path(path_ending, actual_time, base=3)
                start_mob = True
            if event.dict['text'] == '&' and not joueur.bouclier:
                joueur.start_bouclier()
            moving_in_the_graph(joueur, event.dict['text'], region)
            # draw_wall([joueur.column, joueur.row], screen, graph)
            if region[(joueur.column, joueur.row)][-1] == 1:
                print("case d'arrivée atteinte !")
                go_on = False
            if region[(joueur.column, joueur.row)][2] and not joueur.bouclier:
                print("Vous êtes mort")
                go_on = False
            if LEVEL >= 2:
                for neighbor in neighbors(joueur.column, joueur.row):
                    draw_wall(neighbor, screen, graph, region)
    draw_lab(screen, graph, region)
    screen.blit(joueur.image, joueur.coor)
    if start_mob:
        if len(path_start):
            refresh_start(time(), mob)
            screen.blit(mob.image, mob.coor)
        if len(path_ending):
            refresh_ending(time())
        if not (len(path_start) or len(path_ending)):
            if time() > actual_time + 45:
                start_mob = False
                actual_time = 0
            else:
                print(f"Cooldown bave : {(actual_time + 45) - time()}")
    if joueur.bouclier_end != 0:
        joueur.refresh_bouclier(time())
    pygame.display.update()

pygame.quit()
