import pygame
from .food import Food
from .player import Player
from .upgrade import UpgradeMenu
import random
from .enemy import Enemy, FastEnemy, SlowEnemy, HunterEnemy
from .ui.label import UILabel

class Map:
    """
    Class that represents the entire Map of the game.

    Attributes:
      - width: int: Width of the Map.
      - height: int: Height of the Map.
      - player_color: Color: The color of the main Player.
      - player: Player: The main Player.
      - foods: List[Food]: All of the Food on the Map.
      - spawn_timer: float: Time remaining for Food to be spawned.
      - spawn_interval: float: How often Food should be spawned.
      - enemies: List[Enemy]: All of the Enemy(s) on the map.
      - wave_number: int: The wave the Map is on.
      - wave_timer: float: Time in the current wave.
      - enemy_spawn_timer: float: Time remaining to spawn an Enemy.
      - enemy_spawn_interval: float: How often to spawn an Enemy.
      - wave_active: bool: If a wave is currently active.
    """

    def __init__(self, width, height, player_color = pygame.Color(255, 255, 255, 255)):
        self.width = width
        self.height = height
        self.player_color = player_color
        self.player = Player(width, height, player_color)
        self.foods = []
        self.spawn_timer = 0
        self.spawn_interval = 2
        self.enemies = []
        self.wave_number = 1
        self.wave_timer = 0
        self.enemy_spawn_timer = 0
        self.enemy_spawn_interval = 8
        self.wave_active = True
        self.font = pygame.font.SysFont("Arial", 32)
        self.wave_label = UILabel(pygame.Rect(5, 5, 125, 50), self.font)
        self.experience_label = UILabel(pygame.Rect(5, 60, 125, 50), self.font)
        self.time_label = UILabel(pygame.Rect(5, 115, 125, 50), self.font)
        self.upgrade_menu = UpgradeMenu(self.player, self.width, self.height)

    def update(self, delta_time):
        """
        Update the Map and everything in it.

        Arguments:
          - delta_time: float: Time since last frame.
        """

        # Get key inputs.
        keys = pygame.key.get_pressed()

        # Waits for player input before the next wave can start.
        if not self.wave_active:
            # Update upgrade menu and continue to next wave if player presses space.
            self.upgrade_menu.update()
            if keys[pygame.K_SPACE]:
                self.wave_active = True

            return

        # Recreate the player if it dies.
        if self.player.dead:
            self.player = Player(self.width, self.height, self.player_color)

        # Handle input and update the Player.
        self.player.handle_input(delta_time, keys)
        self.player.update(delta_time)

        # If Player collides with Enemy body, Player dies.
        for enemy in self.enemies:
            for i in enemy.position_history:
                if i.distance_to(self.player.position) <= (self.player.radius + enemy.radius):
                    self.player.dead = True

        # If Enemy AI collides with Player body, Enemy dies.
        for enemy in self.enemies.copy():
            for i in self.player.position_history:
                if i.distance_to(enemy.position) <= (self.player.radius + enemy.radius):
                    enemy.dead = True
                    self.enemies.remove(enemy)
                    break

        # Update Enemy AI.
        for enemy in self.enemies:
            enemy.update(delta_time)

        # If Player and Food radius cross, remove the Food and give the Player XP.
        for food in self.foods.copy():
            if self.player.position.distance_to(food.position) <= (25 + 10):
                self.foods.remove(food)
                self.player.gain_xp()

        # Spawn interval timer for Food.
        self.spawn_timer += delta_time
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0
            self.foods.append(Food(self.width, self.height))

        # Keeps track of the time in the current wave. Each wave is 60 seconds.
        self.wave_timer += delta_time
        if self.wave_timer >= 60:
            self.wave_timer = 0
            self.wave_number += 1
            self.wave_active = False
            self.enemy_spawn_interval = max(1, self.enemy_spawn_interval - 0.5)

        # Spawn interval timer for Enemy.
        self.enemy_spawn_timer += delta_time
        if self.enemy_spawn_timer >= self.enemy_spawn_interval:
            self.enemy_spawn_timer = 0
            enemy_type = random.choice([FastEnemy, SlowEnemy, HunterEnemy])
            if enemy_type == HunterEnemy:
                self.enemies.append(HunterEnemy(self.width, self.height, self.player))
            else:
                self.enemies.append(enemy_type(self.width, self.height))

    def draw(self, surface):
        """
        Draw every object in the Map.

        Arguments:
          - surface: Surface: Surface to draw the objects to.
        """

        # Draw the Player.
        self.player.draw(surface)

        # Draw the Enemy(s).
        for enemies in self.enemies:
            enemies.draw(surface)

        # Draw all Food.
        for food in self.foods:
            food.draw(surface)

        # Draw the wave number.
        self.wave_label.text = f"Wave: {self.wave_number}"
        self.wave_label.draw(surface)

        # Draw the experience text.
        self.experience_label.text = f"XP: {self.player.xp}"
        self.experience_label.draw(surface)

        # Draw the wave time remaining text.
        self.time_label.text = f"Time: {int(60 - self.wave_timer)}"
        self.time_label.draw(surface)

        # Draw the upgrade menu between waves.
        if not self.wave_active:
            self.upgrade_menu.draw(surface)

        

