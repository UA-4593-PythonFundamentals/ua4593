# import sys
# from pprint import pprint
# pprint(sys.path)

import pygame
from constants import Colors
pygame.init()


window_height = 600
window_width = 800

font = pygame.font.SysFont('Calibri', 25, True, False)
font_points_line = pygame.font.SysFont('Calibri', 10, True, False)

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("First Pygame App")

POINTS = []

is_running = True

clock = pygame.time.Clock()

while is_running:

    # Event handling and logic(update state)
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print(event)
            if event.button == pygame.BUTTON_LEFT:
                POINTS.append(event.pos)
            elif event.button == pygame.BUTTON_RIGHT:
                if POINTS:
                    POINTS.pop()
    


    # Drawing code
    screen.fill(Colors.WHITE)
    if POINTS:
        points_str = "points: " +", ".join(map(str, POINTS))
        text = font_points_line.render(f"{points_str}",True,Colors.BLACK)
        screen.blit(text, (10, 10))
        # print(POINTS)
        if len(POINTS) > 2:
            pygame.draw.polygon(screen, Colors.YELLOW, POINTS)
        for point in POINTS:
            text = font.render(f"{point}",True,Colors.BLACK)
            screen.blit(text, (point[0]-50, point[1]-20))
            pygame.draw.circle(screen, Colors.RED, point, 5)
    
    pygame.display.flip()
    clock.tick(60)