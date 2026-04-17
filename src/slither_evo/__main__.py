import pygame

from modules.map import Map
from modules.snake import Snake
from modules.player import Player
from modules.title_screen import TitleScreen

# Initialize Pygame.
# pygame.init()
pygame.font.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
delta_time = 0
title_screen = TitleScreen(width, height)
map = Map(width, height)

while running:
    # Check each event that has happened since last frame.
    for event in pygame.event.get():
        # If the quit event is sent, stop the loop next frame.
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a solid color.
    screen.fill(pygame.Color(50, 50, 50, 255))

    if title_screen.started:
        # Update and draw the map.
        map.update(delta_time)
        map.draw(screen)
    else:
        # Update and draw the title screen.
        title_screen.update()
        title_screen.draw(screen)

    # Flip framebuffers to show our drawn content.
    pygame.display.flip()

    # Sets the delta_time (time since last frame) in seconds.
    # Since we are calling clock.tick(60), the framerate is also limited to 60 FPS.
    delta_time = clock.tick(60) / 1000.0

# Clean up Pygame and quit.
pygame.quit()
