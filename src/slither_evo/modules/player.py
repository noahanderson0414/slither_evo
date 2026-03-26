import pygame
from modules.snake import Snake

class Player(Snake):
    """
    Class that inherits Snake.
    Adds user input for movement.
    """

    def __init__(self, width, height):
        super().__init__(width, height)
        self.position = pygame.Vector2(width / 2, height / 2)
        self.turn_speed = 200.0

    def handle_input(self, delta_time: float, keys) -> None:
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
