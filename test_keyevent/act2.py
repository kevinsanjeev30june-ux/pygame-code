# importing pygame module
import pygame

# initalising pygame
pygame.init()

# Create the display surface of object of specific dimension
window = pygame.display.set_mode((700,700))

# Fill the screen with white color
BACKGROUND_COLOR =(80,50,40)
window.fill(BACKGROUND_COLOR)

# Define colors
BLUE =(0,0,255)

# Draw solid circle
pygame.draw.circle(window,BLUE,(300,300),50)

# Draw outllined circle
pygame.draw.circle(window,BLUE,(100,100),50,3)

# Draw the surface object to the screen
pygame.display.update()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Quit pygame
pygame.quit()           