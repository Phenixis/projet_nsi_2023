import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_WEIGHT = 1450, 840

NOIR = (0)
BLANC = pygame.Color("#ffffff")
VERT = pygame.Color("#0e6f46")
BLEU = pygame.Color("#213035")
MARRON = pygame.Color("#774633")

screen = pygame.display.set_mode((1450, 840), pygame.FULLSCREEN)
screen.fill(BLEU)
go_on = True

bouton_mise_500 = pygame.Rect(1200, 200, 150, 50)
pygame.draw.rect(screen, BLANC, bouton_mise_500)

bouton_mise_1000 = pygame.Rect(1200, 350, 150, 50)
pygame.draw.rect(screen, BLANC, bouton_mise_1000)

bouton_mise_2000 = pygame.Rect(1200, 500, 150, 50)
pygame.draw.rect(screen, BLANC, bouton_mise_2000)

bouton_mise_5000 = pygame.Rect(1200, 650, 150, 50)
pygame.draw.rect(screen, BLANC, bouton_mise_5000)

lb = []
lb.append([bouton_mise_500, BLANC])
lb.append([bouton_mise_1000, BLANC])
lb.append([bouton_mise_5000, BLANC])
lb.append([bouton_mise_2000, BLANC])

boutons_go_on = True
while boutons_go_on == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boutons_go_on = False

        elif bouton_mise_500.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                boutons_go_on = False

        elif bouton_mise_1000.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                valeur_mise = 1000
                boutons_go_on = False

        elif bouton_mise_2000.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                valeur_mise = 2000
                boutons_go_on = False

        elif bouton_mise_5000.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                valeur_mise = 5000
                boutons_go_on = False

    for b in lb:
        if b[0].collidepoint(pygame.mouse.get_pos()):
            b[1] = NOIR
            break
        else:
            b[1] = BLANC

    for (button, color) in lb:
        pygame.draw.rect(screen, color, button, 5)
        pygame.display.update()
    pygame.draw.rect(screen, VERT, (0, 0, 1200, 800))
    pygame.draw.rect(screen, BLANC, (1240, 15, 200, 805), 10, 5)
    pygame.display.flip()

