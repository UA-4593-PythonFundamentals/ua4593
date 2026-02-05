import pygame
import random

pygame.init()
screen_height = 720
screen_width =  1280
center_x = screen_width // 2
center_y = screen_height // 2
screen = pygame.display.set_mode((screen_width, screen_height))
large_font = pygame.font.Font(None, 100)
small_font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
running = True
text = ""
instruction_text = "Guess a number between 1 and 100. Use a keyboard to write the number"
rand_number = random.randint(1, 100)
line_color = (255,255,255)
game_state = False


while running:
    input_surface = large_font.render(text, True, (255,255,255))
    instruction_surface = small_font.render(instruction_text, True, (255,255,255))
    input_rect = input_surface.get_rect(center=screen.get_rect().center)
    instruction_rect = instruction_surface.get_rect(center=(center_x, center_y + 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    guess = int(text)
                    if  rand_number - guess == 0:
                        line_color = (255,0,0)
                        game_state = True
                        text = ""
                    elif 1 <= abs(rand_number - guess) <= 5:
                        line_color = (255,165,0)
                        instruction_text = "Warm! You are close"
                        text = ""
                    elif 6 <= abs(rand_number - guess) <= 25:
                        line_color = (0, 0, 255)
                        instruction_text = "Cold!"
                        text = ""
                    elif 26 <= abs(rand_number - guess) <= 99:
                        line_color = "aqua"
                        instruction_text = "Very cold!"
                        text = "" 
                    else:
                        text = ""
                except ValueError:
                    instruction_text = "That's not a number"
            elif event.key == pygame.K_BACKSPACE:
               text = text[:-1]
            else: 
                text += event.unicode
            if game_state:
                instruction_text = "It's correct! Press R to restart the game"
                if event.key == pygame.K_r:
                    instruction_text = "Hey! Guess a number from 1 to 100"
                    rand_number = random.randint(1, 100)
                    line_color = (255,255,255)
                    text = ""
                    game_state = False
                    
    screen.fill((30, 30, 30))
    screen.blit(input_surface, input_rect)
    screen.blit(instruction_surface, instruction_rect)
    pygame.draw.line(screen, line_color, (1, input_rect.bottom + 10), (1280, input_rect.bottom + 10), 2)
    pygame.display.flip()

    clock.tick(25)  # limits FPS to 60

pygame.quit()