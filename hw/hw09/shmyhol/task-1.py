import pygame
import random
import sys


# --- Game Setup ---
def init_game():
    number = random.randint(1, 100)
    tries = 10
    message = "Guess a number from 1 to 100"
    game_over = False
    return number, tries, message, game_over


# --- Check Guess ---
def check_guess(guess, number, tries):
    tries -= 1

    if guess == number:
        return tries, "🎉 You win!", True

    if tries == 0:
        return tries, f"Game Over! Number was {number}", True

    if guess < number:
        return tries, "The number is GREATER", False
    else:
        return tries, "The number is LESS", False


# --- Handle Input ---
def handle_input(event, user_text, game_over, number, tries):
    message = None

    if event.type == pygame.KEYDOWN:

        # Restart
        if game_over and event.key == pygame.K_r:
            return "", *init_game()

        if not game_over:

            if event.key == pygame.K_RETURN:
                if user_text != "":
                    guess = int(user_text)
                    tries, message, game_over = check_guess(guess, number, tries)
                    user_text = ""

            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]

            else:
                if event.unicode.isdigit():
                    user_text += event.unicode

    return user_text, number, tries, message, game_over


# --- Draw Screen ---
def draw(screen, font, message, tries, user_text, game_over):
    screen.fill((30, 30, 30))

    msg_surface = font.render(message, True, (255, 255, 255))
    screen.blit(msg_surface, (50, 100))

    tries_surface = font.render(f"Tries left: {tries}", True, (255, 255, 0))
    screen.blit(tries_surface, (50, 150))

    pygame.draw.rect(screen, (200, 200, 200), (200, 250, 200, 40), 2)
    text_surface = font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (210, 255))

    if game_over:
        restart_surface = font.render("Press R to restart", True, (180, 180, 180))
        screen.blit(restart_surface, (170, 320))

    pygame.display.flip()


# --- Main ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Guess the Number")
    font = pygame.font.SysFont("Arial", 28)
    clock = pygame.time.Clock()

    number, tries, message, game_over = init_game()
    user_text = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            result = handle_input(event, user_text, game_over, number, tries)
            user_text, number, tries, new_message, game_over = result

            if new_message:
                message = new_message

        draw(screen, font, message, tries, user_text, game_over)
        clock.tick(60)


if __name__ == "__main__":
    main()