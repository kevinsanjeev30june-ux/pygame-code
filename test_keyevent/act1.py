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

        # checking if keydown event happened or not    
        if event.type == pygame.KEYDOWN:
            # if keydown event happened
            # than printing a string as output
            print("A key has been pressed")