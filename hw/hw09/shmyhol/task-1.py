import pygame
import sys
import pygame_gui
pygame.init()

WIEDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIEDTH, HEIGHT))
pygame.display.set_caption("Task1 game")


CLOCK = pygame.time.Clock()
MANAGRER = pygame_gui.UIManager((WIEDTH, HEIGHT))

TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((325, 300), (150, 50)), manager=MANAGRER, object_id="#text_input")

done = False

while not done:
    UI_REFRESH_RATE = CLOCK.tick(60)/1000
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        MANAGRER.process_events(event)

    MANAGRER.update(UI_REFRESH_RATE)
    
    SCREEN.fill("white")
    MANAGRER.draw_ui(SCREEN)
    pygame.display.update()
    CLOCK.tick(60)