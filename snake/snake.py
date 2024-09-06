import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)

# Game window dimensions
WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set the clock
clock = pygame.time.Clock()

# Snake properties
SNAKE_SIZE = 10
SNAKE_SPEED = 5

# Font
font = pygame.font.SysFont(None, 35)

# Function to display score
def show_score(score):
    value = font.render("Score: " + str(score), True, WHITE)
    window.blit(value, [0, 0])

# Function to draw snake
def draw_snake(snake_body):
    for x, y in snake_body:
        pygame.draw.rect(window, GREEN, [x, y, SNAKE_SIZE, SNAKE_SIZE])

# Game loop
def game():
    # Starting position of snake
    snake_x = WIDTH // 2
    snake_y = HEIGHT // 2
    snake_body = []
    snake_length = 1

    # Snake direction (initially not moving)
    dx = 0
    dy = 0

    # Food position
    food_x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0

    score = 0
    game_over = False
    snake_speed = SNAKE_SPEED

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -SNAKE_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = SNAKE_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -SNAKE_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = SNAKE_SIZE
                    dx = 0

        # Move snake
        snake_x += dx
        snake_y += dy

        # Check for wall collision
        if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
            game_over = True

        # Snake grows
        snake_head = [snake_x, snake_y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check if snake runs into itself
        for block in snake_body[:-1]:
            if block == snake_head:
                game_over = True

        # Check if snake eats food
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0
            snake_length += 1
            score += 1
            snake_speed += 1
        # Update the window
        window.fill(BLACK)
        draw_snake(snake_body)
        pygame.draw.rect(window, RED, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])
        show_score(score)

        pygame.display.update()

        # Control the snake speed
        clock.tick(snake_speed)

    pygame.quit()

if __name__ == "__main__":
    game()
