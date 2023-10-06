import pygame
import random

class SnakeGame:
    def __init__(self):
        # Initialize the game
        pygame.init()

        # Set the size of the game window
        self.window_width = 400
        self.window_height = 400

        # Set the size of each cell in the grid
        self.cell_size = 20

        # Set the number of cells in the grid
        self.grid_width = self.window_width // self.cell_size
        self.grid_height = self.window_height // self.cell_size

        # Set the initial position and length of the snake
        self.snake_start = (self.grid_width // 2, self.grid_height // 2)
        self.snake = [self.snake_start, (self.snake_start[0] - 1, self.snake_start[1]),
                      (self.snake_start[0] - 2, self.snake_start[1])]
        self.snake_length = len(self.snake)

        # Set the initial position of the apple
        self.apple_pos = (random.randint(0, self.grid_width - 1), random.randint(0, self.grid_height - 1))

        # Set the initial score
        self.score = 0

        # Set the initial direction of the snake
        self.snake_direction = "right"

        # Set the game window
        self.game_window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Snake Game")

        # Set the game clock
        self.clock = pygame.time.Clock()

        # Set the font
        self.font = pygame.font.Font(None, 24)

        # Set the button colors
        self.button_color = (0, 255, 0)
        self.button_hover_color = (0, 200, 0)

        # Set the game state
        self.game_active = True

    def show_end_screen(self):
        # Display the game over text
        game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        self.game_window.blit(game_over_text, (self.window_width // 2 - game_over_text.get_width() // 2,
                                                self.window_height // 2 - game_over_text.get_height() // 2))

        # Create the new game button
        new_game_button = pygame.Rect(self.window_width // 2 - 100, self.window_height // 2 + 50, 100, 50)
        pygame.draw.rect(self.game_window, self.button_color, new_game_button)
        new_game_text = self.font.render("New Game", True, (255, 255, 255))
        new_game_text_rect = new_game_text.get_rect()
        new_game_text_rect.center = new_game_button.center
        self.game_window.blit(new_game_text, new_game_text_rect)

        # Create the quit button
        quit_button = pygame.Rect(self.window_width // 2 + 50, self.window_height // 2 + 50, 100, 50)
        pygame.draw.rect(self.game_window, self.button_color, quit_button)
        quit_text = self.font.render("Quit", True, (255, 255, 255))
        quit_text_rect = quit_text.get_rect()
        quit_text_rect.center = quit_button.center
        self.game_window.blit(quit_text, quit_text_rect)

        # Check for mouse button clicks
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if new_game_button.collidepoint(mouse_pos):
                    # Start a new game loop
                    self.__init__()
                    self.game_loop()
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()



    def game_loop(self):
        # Main game loop
        while True:
            if self.game_active:
                # Event handling
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP and self.snake_direction != "down":
                            self.snake_direction = "up"
                        elif event.key == pygame.K_DOWN and self.snake_direction != "up":
                            self.snake_direction = "down"
                        elif event.key == pygame.K_LEFT and self.snake_direction != "right":
                            self.snake_direction = "left"
                        elif event.key == pygame.K_RIGHT and self.snake_direction != "left":
                            self.snake_direction = "right"

                # Update snake position
                snake_head = self.snake[0]
                if self.snake_direction == "up":
                    new_head = (snake_head[0], snake_head[1] - 1)
                elif self.snake_direction == "down":
                    new_head = (snake_head[0], snake_head[1] + 1)
                elif self.snake_direction == "left":
                    new_head = (snake_head[0] - 1, snake_head[1])
                elif self.snake_direction == "right":
                    new_head = (snake_head[0] + 1, snake_head[1])

                self.snake.insert(0, new_head)

                # Check if snake hits apple
                if self.snake[0] == self.apple_pos:
                    # Increase snake length and score
                    self.snake_length += 1
                    self.score += 100
                    # Generate new apple position
                    self.apple_pos = (random.randint(0, self.grid_width - 1), random.randint(0, self.grid_height - 1))

                # Check if snake hits wall or itself
                if (self.snake[0][0] < 0 or self.snake[0][0] >= self.grid_width or
                        self.snake[0][1] < 0 or self.snake[0][1] >= self.grid_height or
                        self.snake[0] in self.snake[1:]):
                    self.game_active = False

                # Update snake length
                if len(self.snake) > self.snake_length:
                    self.snake.pop()

                # Render the game window
                self.game_window.fill((0, 0, 0))

                # Draw the snake
                for pos in self.snake:
                    pygame.draw.rect(self.game_window, (0, 255, 0),
                                     (pos[0] * self.cell_size, pos[1] * self.cell_size, self.cell_size, self.cell_size))

                # Draw the apple
                pygame.draw.rect(self.game_window, (255, 0, 0),
                                 (self.apple_pos[0] * self.cell_size, self.apple_pos[1] * self.cell_size,
                                  self.cell_size, self.cell_size))

                # Draw the score
                score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
                self.game_window.blit(score_text, (10, 10))
            else:
                self.show_end_screen()

            # Update the game display
            pygame.display.flip()

            # Set the game FPS
            self.clock.tick(10)

# Call the game loop function from __main__
if __name__ == "__main__":
    game = SnakeGame()
    game.game_loop()
