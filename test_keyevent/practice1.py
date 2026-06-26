# importing pygame module
import pygame

# initalising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((300,300))

# creating a running loop
while True:
    # Creating a loop check events that are occuring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # checking if keydown event happened or not    
        if event.type == pygame.KEYDOWN:
            # if keydown event happened
            # than printing a string as output
            print("A key has been pressed")

            if event.key == pygame.K_UP:
                print("UP arrow key has been pressed")
            if event.key == pygame.K_UP:
                print("UP arrow key has been pressed")

            if event.key == pygame.K_UP:
                print("UP arrow key has been pressed")

            elif event.key == pygame.K_DOWN:
                print("DOWN arrow key has been pressed")

            elif event.key == pygame.K_LEFT:
                print("LEFT arrow key has been pressed")

            elif event.key == pygame.K_RIGHT:
                print("Right arrow key has been pressed")

