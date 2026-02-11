import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)

clock = pygame.time.Clock()
done = False
while not done:
# --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
# --- Game logic should go here
# --- Drawing code should go here
# First, clear the screen to white. Don't put other drawing commands
# above this, or they will be erased with this command.
    gameDisplay.fill(WHITE)
# --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
# --- Limit to 60 frames per second
    clock.tick(60)