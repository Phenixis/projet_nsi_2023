import pygame

pygame.init()

WHITE = (255, 255, 255)
GREY = (20, 20, 20)
BLACK = (0, 0, 0)
PURPLE = (100, 0, 100)
RED = (255, 0, 0)

size = (850, 850)
screen = pygame.display.set_mode(size)
screen.fill(GREY)

done = False

bouton_comp1 = pygame.Rect(1000, 255, 244, 31)
pygame.draw.rect(screen, WHITE, bouton_comp1)

lb = []
lb.append([bouton_comp1, WHITE])

# -------- Main Program Loop -----------
go_on = True
while go_on:
    for event in pygame.event.get():
        print(event.dict)
        if "key" in event.dict:
            if event.dict["key"] == 27:
                go_on = False

            if event.dict["key"] == 49:
                # fonction compétence 1

                ...
            if event.dict["key"] == 50:
                # fonction compétence 2
                ...
            if event.dict["key"] == 51:
                # fonction compétence 3
                ...
            if event.dict["key"] == 52:
                # fonction compétence 4
                ...
    # for b in lb:
    #     if b[0].collidepoint(pygame.mouse.get_pos()):

    for (button, color) in lb:
        pygame.draw.rect(screen, color, button, 5)
        pygame.display.update()
    pygame.draw.rect(screen, WHITE, (0, 0, 100, 100))
    pygame.display.flip()

pygame.quit()
