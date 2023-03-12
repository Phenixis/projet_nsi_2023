from Labyrinthe import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

graph, region = main(screen, 2)
joueur = Joueur()


def moving_in_the_graph(player: Joueur, dir: str, region):
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

go_on = True
while go_on:
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(joueur.coor[0], joueur.coor[1], joueur.width, joueur.height))
    for event in pygame.event.get():
        if "key" in event.dict and event.dict['key'] == 27:
            go_on = False
        if "text" in event.dict.keys():
            moving_in_the_graph(joueur, event.dict['text'], region)
            draw_wall([joueur.column, joueur.row], screen, graph, region)

    screen.blit(joueur.image, joueur.coor)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
