import pygame
import random

class Food:
    def __init__(self, width, height):
        x = random.randint(0, width)
        y = random.randint(0, height)
        self.position = pygame.Vector2(x, y)

    def draw(self, surface: pygame.Surface):
        # Draws the food object
        pygame.draw.circle(surface, pygame.Color(0, 255, 0, 255), self.position, 8.0)
