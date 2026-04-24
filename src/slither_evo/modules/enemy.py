"""
Defines the Enemy class and special child classes.
"""

import random

import pygame

from slither_evo.modules.snake import Snake

class Enemy(Snake):
    """
    Class that inherits from Snake.
    Implements random movement.
    """

    def __init__(self, width, height):
        """
        Initialize the Enemy.

        Arguments:
            - width: int: Width of the Map.
            - height: int: Height of the Map.
        """
        super().__init__(width, height)

        # Override position to spawn at a random location on the map.
        x = random.randint(0, width)
        y = random.randint(0, height)
        self.position = pygame.Vector2(x, y)
        self.turn_speed = 200.0
        self.radius = 10

    def update(self, delta_time):
        """
        Update the physics state of the Enemy.

        Arguments:
          - delta_time: float: Time since last frame.
        """

        # Move randomly.
        self.direction = self.direction.rotate(random.uniform(-10,10))
        super().update(delta_time)


class FastEnemy(Enemy):
    """
    Class that inherits from Enemy.
    Fast but short enemy snake.
    """

    def __init__(self, width, height):
        """
        Initialize the FastEnemy.

        Arguments:
          - width: int: Width of the Map.
          - height: int: Height of the Map.
        """

        super().__init__(width, height)
        self.speed = 350.0
        self.radius = 6
        self.length = 20
        self.color = pygame.Color(255, 100, 100, 255)


class SlowEnemy(Enemy):
    """
    Class that inherits from Enemy.
    Slow but long enemy snake.
    """

    def __init__(self, width, height):
        """
        Initialize the SlowEnemy.

        Arguments:
          - width: int: Width of the Map.
          - height: int: Height of the Map.
        """
        super().__init__(width, height)
        self.speed = 50.0
        self.radius = 30
        self.length = 500
        self.color = pygame.Color(100, 100, 255, 255)


class HunterEnemy(Enemy):
    """
    Class that inherits from Enemy.
    Steers toward the player.
    """

    def __init__(self, width, height, player):
        """
        Initialize the HunterEnemy.

        Arguments:
          - width: int: Width of the Map.
          - height: int: Height of the Map.
          - player: Player: The player to hunt.
        """

        super().__init__(width, height)
        self.speed = 180.0
        self.radius = 12
        self.player = player
        self.color = pygame.Color(255, 0, 255, 255)

    def update(self, delta_time):
        """
        Update the physics state of the HunterEnemy.

        Arguments:
          - delta_time: float: Time since last frame.
        """

        # Calculate direction toward player.
        to_player = self.player.position - self.position
        if to_player.length() > 0:
            to_player = to_player.normalize()
        # Steer toward player.
        self.direction = self.direction.lerp(to_player, 0.05).normalize()
        super(Enemy, self).update(delta_time)
