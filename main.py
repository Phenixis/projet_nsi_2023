from Labyrinthe import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

graph = main(screen)
joueur = Joueur()

go_on = True
while go_on:
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(joueur.coor[0], joueur.coor[1], joueur.width, joueur.height))
    for event in pygame.event.get():
        if "key" in event.dict and event.dict['key'] == 27:
            go_on = False
        if "text" in event.dict.keys():
            if event.dict['text'] == 'q' and ((joueur.column, joueur.row), (joueur.column - 1, joueur.row)) in graph.edges:
                joueur.update("l")
            elif event.dict['text'] == 'd' and ((joueur.column, joueur.row), (joueur.column + 1, joueur.row)) in graph.edges:
                joueur.update("r")
            elif event.dict['text'] == 's' and ((joueur.column, joueur.row), (joueur.column, joueur.row + 1)) in graph.edges:
                joueur.update("d")
            elif event.dict['text'] == 'z' and ((joueur.column, joueur.row), (joueur.column, joueur.row - 1)) in graph.edges:
                joueur.update("u")
    screen.blit(joueur.image, joueur.coor)
    pygame.display.update()
    clock.tick(60)


pygame.quit()