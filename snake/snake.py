import pygame
import random

# Initialize the game
pygame.init()

# Set the size of the game window
window_width = 400
window_height = 400

# Set the size of each cell in the grid
cell_size = 20

# Set the number of cells in the grid
grid_width = window_width // cell_size
grid_height = window_height // cell_size

# Set the initial position and length of the snake
snake_start = (grid_width // 2, grid_height // 2)
snake = [snake_start, (snake_start[0]-1, snake_start[1]), (snake_start[0]-2, snake_start[1])]
snake_length = len(snake)

# Set the initial position of the apple
apple_pos = (random.randint(0, grid_width-1), random.randint(0, grid_height-1))

# Set the initial score
score = 0

# Set the initial direction of the snake
snake_direction = "right"

# Set the game window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set the game clock
clock = pygame.time.Clock()

# Main game loop
game_over = False
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"
            elif event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"

    # Update snake position
    snake_head = snake[0]
    if snake_direction == "up":
        new_head = (snake_head[0], snake_head[1]-1)
    elif snake_direction == "down":
        new_head = (snake_head[0], snake_head[1]+1)
    elif snake_direction == "left":
        new_head = (snake_head[0]-1, snake_head[1])
    elif snake_direction == "right":
        new_head = (snake_head[0]+1, snake_head[1])

    snake.insert(0, new_head)

    # Check if snake hits apple
    if snake[0] == apple_pos:
        # Increase snake length and score
        snake_length += 1
        score += 100
        # Generate new apple position
        apple_pos = (random.randint(0, grid_width-1), random.randint(0, grid_height-1))

    # Check if snake hits wall or itself
    if (snake[0][0] < 0 or snake[0][0] >= grid_width or
        snake[0][1] < 0 or snake[0][1] >= grid_height or
        snake[0] in snake[1:]):
        game_over = True

    # Update snake length
    if len(snake) > snake_length:
        snake.pop()

    # Render the game window
    game_window.fill((0, 0, 0))

    # Draw the snake
    for pos in snake:
        pygame.draw.rect(game_window, (0, 255, 0), (pos[0]*cell_size, pos[1]*cell_size, cell_size, cell_size))

    # Draw the apple
    pygame.draw.rect(game_window, (255, 0, 0), (apple_pos[0]*cell_size, apple_pos[1]*cell_size, cell_size, cell_size))

    # Draw the score
    font = pygame.font.Font(None, 24)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    game_window.blit(score_text, (10, 10))

    # Update the game display
    pygame.display.flip()

    # Set the game FPS
    clock.tick(10)

# Quit the game
pygame.quit()

