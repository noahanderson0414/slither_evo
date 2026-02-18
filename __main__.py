import pygame
from modules.snake import Snake

# Initialize Pygame.
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
delta_time = 0
our_snake = Snake()

while running:
    # Check each event that has happened since last frame.
    for event in pygame.event.get():
        # If the quit event is sent, stop the loop next frame.
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a solid color.
    screen.fill(pygame.Color(50, 50, 50, 255))

    our_snake.update(delta_time)
    our_snake.draw(screen)

    # Flip framebuffers to show our drawn content.
    pygame.display.flip()

    # Sets the delta_time (time since last frame) in seconds.
    # Since we are calling clock.tick(60), the framerate is also limited to 60 FPS.
    delta_time = clock.tick(60) / 1000.0

pygame.quit()
