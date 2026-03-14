import pygame
from modules.snake import Snake
import random

class Enemy(Snake):
    def __init__(self, width, height):
        super().__init__(width, height)
        x = random.randint(0, width)
        y = random.randint(0, height)
        self.position = pygame.Vector2(x, y)
        self.turn_speed = 200.0
        self.radius = 10

    def update(self, delta_time):
        # Random movement for now, change later
        self.direction = self.direction.rotate(random.uniform(-10,10))
        super().update(delta_time)



