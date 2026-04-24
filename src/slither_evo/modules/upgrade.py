"""
Defines the UpgradeMenu class.
"""

import pygame

from slither_evo.modules.ui.button import UIButton
from slither_evo.modules.ui.label import UILabel

class UpgradeMenu:
    """
    Class that represents the upgrade menu shown between waves.
    Allows the player to spend XP on upgrades.

    Attributes:
      - player: Player: The player to upgrade.
      - width: int: Width of the Map.
      - height: int: Height of the Map.
      - font: Font: The Font to draw the UI with.
      - upgrade_costs: dict: Dictionary that gives the cost for each upgrade.
      - length_label: UILabel: Label that shows the length of the Player.
      - length_button: UIButton: Button that tries to upgrade the length of the Player when clicked.
      - speed_label: UILabel: Label that shows the speed of the Player.
      - speed_button: UIButton: Button that tries to upgrade the speed of the Player when clicked.
      - radius_label: UILabel: Label that shows the radius of the Player.
      - radius_button: UIButton: Button that tries to upgrade the radius of the Player when clicked.
      - xp_label: UILabel: Label that shows the XP of the Player.
      - continue_prompt: UILabel: Label that shows what key to press to continue the game.
    """

    def __init__(self, player, width, height):
        """
        Initialize the UpgradeMenu.

        Arguments:
          - player: Player: The player to upgrade.
          - width: int: Width of the Map.
          - height: int: Height of the Map.
        """

        self.player = player
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("Arial", 32)
        self.upgrade_costs = {
            "length" : 3,
            "speed": 3,
            "radius": 3
        }
        self.length_label = UILabel(pygame.Rect(self.width / 2 - 275, self.height / 2 - 80, 250, 50), self.font)
        self.length_button = UIButton(pygame.Rect(self.width / 2 - 20, self.height / 2 - 80, 300, 50), self.font, self.try_upgrade_length)
        self.speed_label = UILabel(pygame.Rect(self.width / 2 - 275, self.height / 2 - 25, 250, 50), self.font)
        self.speed_button = UIButton(pygame.Rect(self.width / 2 - 20, self.height / 2 - 25, 300, 50), self.font, self.try_upgrade_speed)
        self.radius_label = UILabel(pygame.Rect(self.width / 2 - 275, self.height / 2 + 30, 250, 50), self.font)
        self.radius_button = UIButton(pygame.Rect(self.width / 2 - 20, self.height / 2 + 30, 300, 50), self.font, self.try_upgrade_radius)

        title_font = pygame.font.SysFont("Arial", 64)
        self.xp_label = UILabel(pygame.Rect(self.width / 2 - 175, 5, 350, 75), title_font)
        self.continue_prompt = UILabel(pygame.Rect(self.width / 2 - 500, self.height - 80, 1000, 75), title_font, "[PRESS SPACE TO CONTINUE]")

    def update(self):
        """
        Update the UpgradeMenu.
        """

        self.length_button.update()
        self.speed_button.update()
        self.radius_button.update()

    def try_upgrade_length(self):
        """
        Attempt to upgrade the player's length.
        """

        if self.player.xp >= self.upgrade_costs["length"]:
            self.player.xp -= self.upgrade_costs["length"]
            self.player.length += 10

    def try_upgrade_speed(self):
        """
        Attempt to upgrade the player's speed.
        """

        if self.player.xp >= self.upgrade_costs["speed"]:
            self.player.xp -= self.upgrade_costs["speed"]
            self.player.speed += 10

    def try_upgrade_radius(self):
        """
        Attempt to upgrade the player's radius.
        """

        if self.player.xp >= self.upgrade_costs["radius"]:
            self.player.xp -= self.upgrade_costs["radius"]
            self.player.radius += 10

    def draw(self, screen):
        """
        Draw the UpgradeMenu.

        Arguments:
          - screen: Surface: The Surface to draw the UpgradeMenu to.
        """

        # Screen text between waves showing upgrades.

        # Length
        self.length_label.text = f"Length: {self.player.length}"
        self.length_label.draw(screen)
        self.length_button.text = f"Upgrade ({self.upgrade_costs["length"]} XP)"
        self.length_button.draw(screen)

        # Speed
        self.speed_label.text = f"Speed: {self.player.speed}"
        self.speed_label.draw(screen)
        self.speed_button.text = f"Upgrade ({self.upgrade_costs["speed"]} XP)"
        self.speed_button.draw(screen)

        # Radius
        self.radius_label.text = f"Radius: {self.player.radius}"
        self.radius_label.draw(screen)
        self.radius_button.text = f"Upgrade ({self.upgrade_costs["radius"]} XP)"
        self.radius_button.draw(screen)

        # XP and Continue Prompt
        self.xp_label.text = f"XP: {self.player.xp}"
        self.xp_label.draw(screen)
        self.continue_prompt.draw(screen)
