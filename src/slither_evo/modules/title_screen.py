import pygame

from .ui.label import UILabel
from .ui.button import UIButton

class TitleScreen:
    """
    Class that represents the title screen shown when the game launches.
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
        self.large_font = pygame.font.SysFont("Arial", 64)
        self.small_font = pygame.font.SysFont("Arial", 24)
        self.title_label = UILabel(pygame.Rect(self.width / 2 - 200, 5, 400, 75), self.large_font, "Slither.evo")
        self.creators_label = UILabel(pygame.Rect(self.width / 2 - 200, self.height - 55, 400, 50), self.small_font, "Created by Noah Anderson & Jonathan Pomeroy")
        self.start_button = UIButton(pygame.Rect(self.width / 2 - 125, self.height / 2 - 37.5, 250, 75), self.large_font, self.try_start, text = "Start!")
        self.started = False

    def update(self):
        """
        Update the TitleScreen.
        """

        self.start_button.update()

    def try_start(self):
        """
        Start the game.
        """

        self.started = True

    def draw(self, surface):
        """
        Draw the TitleScreen.

        Arguments:
          - surface: Surface: The Surface to draw the TitleScreen to.
        """

        self.title_label.draw(surface)
        self.creators_label.draw(surface)
        self.start_button.draw(surface)