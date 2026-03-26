import pygame
import random

class Food:
    """
    Class that represents an item to be eaten by a Snake.

    Attributes:
      - position: Vector2: 2D position of the item.
    """

    def __init__(self, width, height):
        x = random.randint(0, width)
        y = random.randint(0, height)
        self.position = pygame.Vector2(x, y)

    def draw(self, surface: pygame.Surface):
        """
        Draws the Food item.

        Arguments:
          - surface: Surface: The Surface to draw the Food to.
        """

        pygame.draw.circle(surface, pygame.Color(0, 255, 0, 255), self.position, 8.0)
