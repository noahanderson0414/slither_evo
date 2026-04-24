"""
Entry-point for the program.
"""

import pygame

from slither_evo.modules.title_screen import TitleScreen

# Define constant variables.
WIDTH = 1280
HEIGHT = 720

# Initialize Pygame.
#pygame.init()
pygame.font.init()
pygame.display.set_caption("Slither.evo")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
delta_time = 0
title_screen = TitleScreen(WIDTH, HEIGHT)

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
        title_screen.map.update(delta_time)
        title_screen.map.draw(screen)
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
