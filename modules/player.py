import pygame
from modules.snake import Snake

class Player(Snake):
    def __init__(self):
        super().__init__()
        self.turn_speed = 200.0

    def handle_input(self, delta_time: float, keys) -> None:
        # Handle A and D to rotate the direction of the Player.
        if keys[pygame.K_a]:
            self.direction = self.direction.rotate(-self.turn_speed * delta_time)
        if keys[pygame.K_d]:
            self.direction = self.direction.rotate(self.turn_speed * delta_time)
