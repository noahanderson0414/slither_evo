import pygame
from modules.snake import Snake
import random

class Enemy(Snake):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.turn_speed = 200.0

    def update(self, delta_time):
        # Random movement for now, change later
        self.direction = self.direction.rotate(random.uniform(-5,5))
        super().update(delta_time)



