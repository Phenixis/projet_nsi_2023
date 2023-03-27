from Labyrinthe import *

level = 2  # int(input("À quel niveau voulez-vous jouer ? "))
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

screen.fill(BG)
graph, region = main(screen, level)
joueur = Joueur()
joueur.update("nowhere", region)
go_on = True


def moving_in_the_graph(player: Joueur, dir: str, region):
    """
    Vérifie si la direction dans laquelle va le joueur a un mur ou non
    déplace le joueur dans la direction si possible
    """
    if dir == 'q' and ((player.column, player.row), (player.column - 1, player.row)) in graph.edges:
        player.update('l', region)
    elif event.dict['text'] == 'd' and (
            (player.column, player.row), (player.column + 1, player.row)) in graph.edges:
        player.update("r", region)
    elif event.dict['text'] == 's' and (
            (player.column, player.row), (player.column, player.row + 1)) in graph.edges:
        player.update("d", region)
    elif event.dict['text'] == 'z' and (
            (player.column, player.row), (player.column, player.row - 1)) in graph.edges:
        player.update("u", region)


while go_on:
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(joueur.coor[0], joueur.coor[1], joueur.width, joueur.height))
    for event in pygame.event.get():
        if "key" in event.dict and event.dict['key'] == 27:
            go_on = False
        if "text" in event.dict.keys():
            moving_in_the_graph(joueur, event.dict['text'], region)
            # draw_wall([joueur.column, joueur.row], screen, graph)
            if region[(joueur.column, joueur.row)][-1] == 1:
                print("case d'arrivée atteinte !")
                go_on = False
            if level == 2:
                for neighbor in neighbors(joueur.column, joueur.row):
                    draw_wall(neighbor, screen, graph, region)
    draw_lab(screen, graph, region)
    screen.blit(joueur.image, joueur.coor)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
