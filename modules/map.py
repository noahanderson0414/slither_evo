import pygame
from modules.food import Food
from modules.player import Player
from modules.enemy import Enemy

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(width, height)
        self.foods = []
        self.spawn_timer = 0
        self.spawn_interval = 2
        self.enemies = []
        self.enemies.append(Enemy(width, height))
        self.wave_number = 1
        self.wave_timer = 0
        self.enemy_spawn_timer = 0
        self.enemy_spawn_interval = 8
        self.wave_active = True


    def update(self, delta_time):
        # Get key inputs.
        keys = pygame.key.get_pressed()

        # Waits for player input before the next wave can start
        if not self.wave_active:
            if keys[pygame.K_SPACE]:
                self.wave_active = True
            return

        # Recreate the player if it dies.
        if self.player.dead:
            self.player = Player(self.width, self.height)


        # Handle input and update the player.
        self.player.handle_input(delta_time, keys)
        self.player.update(delta_time)

        # If player collides with enemy body, player dies
        for enemy in self.enemies:
            for i in enemy.position_history:
                if i.distance_to(self.player.position) <= (self.player.radius + enemy.radius):
                    self.player.dead = True


        # If enemy ai collides with player body, enemy dies
        for enemy in self.enemies.copy():
            for i in self.player.position_history:
                if i.distance_to(enemy.position) <= (self.player.radius + enemy.radius):
                    enemy.dead = True
                    self.enemies.remove(enemy)
                    break

        # Creating enemy ai
        for enemy in self.enemies:
            enemy.update(delta_time)

        # If player and food radius cross, remove the food and give the player xp
        for food in self.foods.copy():
            if self.player.position.distance_to(food.position) <= (25 + 10):
                self.foods.remove(food)
                self.player.gain_xp()

        # Spawn interval timer for food
        self.spawn_timer += delta_time
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0
            self.foods.append(Food(self.width, self.height))

        # Keeps track of the time in the current wave, each wave is 60 seconds
        self.wave_timer += delta_time
        if self.wave_timer >= 60:
            self.wave_timer = 0
            self.wave_number += 1
            self.wave_active = False
            self.enemy_spawn_interval = max(1, self.enemy_spawn_interval - 0.5)

        # Spawn interval timer for enemy
        self.enemy_spawn_timer += delta_time
        if self.enemy_spawn_timer >= self.enemy_spawn_interval:
            self.enemy_spawn_timer = 0
            self.enemies.append(Enemy(self.width, self.height))

    def draw(self, screen):
        # Draw the player.
        self.player.draw(screen)

        # Draw the enemy ai
        for enemies in self.enemies:
            enemies.draw(screen)

        # Drawing food into the game
        for food in self.foods:
            food.draw(screen)

