"""
Defines the TitleScreen class.
"""

import pygame

from slither_evo.modules.map import Map
from slither_evo.modules.ui.element import UIElement
from slither_evo.modules.ui.label import UILabel
from slither_evo.modules.ui.button import UIButton

class TitleScreen:
    """
    Class that represents the title screen shown when the game launches.

    Attributes:
      - width: int: Width of the screen.
      - height: int: Height of the screen.
      - player_color: int: Active Player color.
      - colors: List[Color]: The List of Colors to iterate through for the Player.
      - large_font: Font: The large Font to draw the UI with.
      - small_font: Font: The small Font to draw the UI with.
      - title_label: UILabel: Label that shows the game title.
      - creators_label: UILabel: Label that shows the game developers.
      - start_button: UIButton: Button that starts the game when clicked.
      - color_rect: UIElement: Rect that shows the selected Player color.
      - next_color_button: UIButton: Button that selects the next Player color when clicked.
      - previous_color_button: UIButton: Button that selects the previous Player color when clicked.
      - map: Map: The active Map/game world.
      - started: bool: Whether the game has started or not.
    """

    def __init__(self, width, height):
        """
        Initialize the TitleScreen.

        Arguments:
          - width: int: Width of the screen.
          - height: int: Height of the screen.
        """

        self.width = width
        self.height = height
        self.player_color = 0
        self.colors = [
            pygame.Color(255, 255, 255, 255),
            pygame.Color(255, 0, 0, 255),
            pygame.Color(0, 255, 0, 255),
            pygame.Color(0, 0, 255, 255),
            pygame.Color(255, 255, 0, 255),
            pygame.Color(255, 0, 255, 255),
            pygame.Color(0, 255, 255, 255),
            pygame.Color(0, 0, 0, 255),
        ]
        self.large_font = pygame.font.SysFont("Arial", 64)
        self.small_font = pygame.font.SysFont("Arial", 24)
        self.title_label = UILabel(pygame.Rect(self.width / 2 - 200, 5, 400, 75), self.large_font, "Slither.evo")
        self.creators_label = UILabel(pygame.Rect(self.width / 2 - 300, self.height - 55, 600, 50), self.small_font, "Created by Noah Anderson & Jonathan Pomeroy")
        self.start_button = UIButton(pygame.Rect(self.width / 2 - 125, self.height / 2 - 37.5, 250, 75), self.large_font, self.try_start, text = "Start!")
        self.color_rect = UIElement(pygame.Rect(self.width / 2 - 67.5, self.height / 2 + 42.5, 135, 75), self.colors[self.player_color])
        self.next_color_button = UIButton(pygame.Rect(self.width / 2 + 72.5, self.height / 2 + 42.5, 50, 75), self.large_font, self.try_next_color, text = ">")
        self.previous_color_button = UIButton(pygame.Rect(self.width / 2 - 122.5, self.height / 2 + 42.5, 50, 75), self.large_font, self.try_previous_color, text = "<")
        self.map = None
        self.started = False

    def update(self):
        """
        Update the TitleScreen.
        """

        self.start_button.update()
        self.next_color_button.update()
        self.previous_color_button.update()

    def try_start(self):
        """
        Start the game.
        """

        self.started = True
        self.map = Map(self.width, self.height, self.colors[self.player_color])

    def try_next_color(self):
        """
        Set the player color to the next color.
        """

        self.player_color = (self.player_color + 1) % len(self.colors)
        self.color_rect.background_color = self.colors[self.player_color]

    def try_previous_color(self):
        """
        Set the player color to the previous color.
        """

        self.player_color = (self.player_color - 1) % len(self.colors)
        self.color_rect.background_color = self.colors[self.player_color]

    def draw(self, surface):
        """
        Draw the TitleScreen.

        Arguments:
          - surface: Surface: The Surface to draw the TitleScreen to.
        """

        self.title_label.draw(surface)
        self.creators_label.draw(surface)
        self.start_button.draw(surface)
        self.color_rect.draw(surface)
        self.next_color_button.draw(surface)
        self.previous_color_button.draw(surface)
