"""
Defines the Player class.
"""

import pygame

from slither_evo.modules.snake import Snake

class Player(Snake):
    """
    Class that inherits Snake.
    Adds user input for movement.

    Attributes:
      - position: Vector2: 2D position of the Snake.
      - position_history: List[Vector2]: Past positions of the Snake. Length of this List also determines the length of the Snake.
      - speed: float: Speed that the Snake should move.
      - length: int: Number of segments the Snake can have.
      - xp: int: How much XP the Snake has.
      - dead: bool: Whether the Snake is dead or not.
      - width: int: Width of the Map.
      - height: int: Height of the Map.
      - radius: float: Radius of each segment of the Snake.
      - color: Color: Color to draw the Snake with.
      - turn_speed: float: The speed that the Player will turn at.
    """

    def __init__(self, width, height, color = pygame.Color(255, 255, 255, 255)):
        super().__init__(width, height, color)
        self.position = pygame.Vector2(width / 2, height / 2)
        self.turn_speed = 200.0

    def handle_input(self, delta_time, keys):
        """
        Handle user input to change the direction of the Player.

        Arguments:
          - delta_time: float: Time since last frame.
          - keys: Keys that are pressed.
        """

        # Handle A and D to rotate the direction of the Player.
        if keys[pygame.K_a]:
            self.direction = self.direction.rotate(-self.turn_speed * delta_time)
        if keys[pygame.K_d]:
            self.direction = self.direction.rotate(self.turn_speed * delta_time)
