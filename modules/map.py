import pygame
from modules.food import Food
from modules.player import Player

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player()
        self.foods = []
        self.spawn_timer = 0
        self.spawn_interval = 2

    def update(self, delta_time):
        # Recreate the player if it dies.
        if self.player.dead:
            self.player = Player()

        # Get key inputs.
        keys = pygame.key.get_pressed()

        # Handle input and update the player.
        self.player.handle_input(delta_time, keys)
        self.player.update(delta_time)

        # If player and food radius cross, remove the food and give the player xp
        for food in self.foods.copy():
            if self.player.position.distance_to(food.position) <= (25 + 10):
                self.foods.remove(food)
                self.player.gain_xp()

        self.spawn_timer += delta_time
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0
            self.foods.append(Food(self.width, self.height))

    def draw(self, screen):
        # Draw the player.
        self.player.draw(screen)

        # Drawing food into the game
        for food in self.foods:
            food.draw(screen)

