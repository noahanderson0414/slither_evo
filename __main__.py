import pygame

from modules.map import Map
from modules.snake import Snake
from modules.player import Player

# Initialize Pygame.
# pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
delta_time = 0
player = Player()
map = Map(width, height, player)

while running:
    # Check each event that has happened since last frame.
    for event in pygame.event.get():
        # If the quit event is sent, stop the loop next frame.
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a solid color.
    screen.fill(pygame.Color(50, 50, 50, 255))

    # Get key inputs.
    keys = pygame.key.get_pressed()

    player.handle_input(delta_time, keys)
    player.update(delta_time)
    player.draw(screen)

    map.update(delta_time)
    map.draw(screen)

    # Flip framebuffers to show our drawn content.
    pygame.display.flip()

    # Sets the delta_time (time since last frame) in seconds.
    # Since we are calling clock.tick(60), the framerate is also limited to 60 FPS.
    delta_time = clock.tick(60) / 1000.0

pygame.quit()
