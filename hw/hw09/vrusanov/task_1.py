import random
import pygame

pygame.init()

WIDTH, HEIGHT = 480, 320
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вгадай число (1–100)")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
GREEN = (50, 180, 80)
RED = (200, 60, 60)
BLUE = (60, 100, 200)

font_large = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 28)

secret = random.randint(1, 100)
attempts_left = 10
guessed = False
game_over = False
input_text = ""
message = "Введіть число та натисніть Enter"
message_color = BLACK

input_rect = pygame.Rect(140, 120, 200, 40)
button_rect = pygame.Rect(170, 180, 140, 44)


def check_guess():
    global message, message_color, guessed, game_over, attempts_left, input_text
    try:
        guess = int(input_text)
        if 1 <= guess <= 100:
            attempts_left -= 1
            if guess == secret:
                guessed = True
                game_over = True
                message = f"Вітаємо! Ви вгадали: {secret}"
                message_color = GREEN
            elif guess < secret:
                message = f"Більше. Залишилось спроб: {attempts_left}"
                message_color = BLUE
            else:
                message = f"Менше. Залишилось спроб: {attempts_left}"
                message_color = BLUE
            if attempts_left <= 0 and not guessed:
                game_over = True
                message = f"Спроб вичерпано. Загадане число: {secret}"
                message_color = RED
        else:
            message = "Число має бути від 1 до 100"
            message_color = RED
    except ValueError:
        message = "Введіть ціле число"
        message_color = RED
    input_text = ""


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if not game_over:
                if event.key == pygame.K_RETURN:
                    check_guess()
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.unicode.isdigit() and len(input_text) < 3:
                    input_text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if button_rect.collidepoint(event.pos):
                check_guess()

    screen.fill(WHITE)

    title = font_large.render("Вгадай число (1–100)", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

    pygame.draw.rect(screen, GRAY, input_rect, 2)
    text_surf = font_large.render(input_text or "?", True, BLACK)
    screen.blit(text_surf, (input_rect.x + 10, input_rect.y + 8))

    if not game_over:
        pygame.draw.rect(screen, BLUE, button_rect)
        pygame.draw.rect(screen, BLACK, button_rect, 2)
        btn_text = font_small.render("Перевірити", True, WHITE)
        screen.blit(btn_text, (button_rect.x + 28, button_rect.y + 12))

    msg_surf = font_small.render(message, True, message_color)
    screen.blit(msg_surf, (WIDTH // 2 - msg_surf.get_width() // 2, 250))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
