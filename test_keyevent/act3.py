import pygame

pygame.init()
screen = pygame.display.set_mode((700,600))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen,(0,135,255), pygame.Rect(100,100,140,140))
    pygame.display.flip()        