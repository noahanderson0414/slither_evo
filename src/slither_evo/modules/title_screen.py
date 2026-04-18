import pygame

from .map import Map
from .ui.element import UIElement
from .ui.label import UILabel
from .ui.button import UIButton

class TitleScreen:
    def __init__(self, width, height):
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
        self.creators_label = UILabel(pygame.Rect(self.width / 2 - 200, self.height - 55, 400, 50), self.small_font, "Created by Noah Anderson & Jonathan Pomeroy")
        self.start_button = UIButton(pygame.Rect(self.width / 2 - 125, self.height / 2 - 37.5, 250, 75), self.large_font, self.try_start, text = "Start!")
        self.color_rect = UIElement(pygame.Rect(self.width / 2 - 67.5, self.height / 2 + 42.5, 135, 75), self.colors[self.player_color])
        self.next_color_button = UIButton(pygame.Rect(self.width / 2 + 72.5, self.height / 2 + 42.5, 50, 75), self.large_font, self.try_next_color, text = ">")
        self.previous_color_button = UIButton(pygame.Rect(self.width / 2 - 122.5, self.height / 2 + 42.5, 50, 75), self.large_font, self.try_previous_color, text = "<")
        self.map = None
        self.started = False
    
    def update(self):
        self.start_button.update()
        self.next_color_button.update()
        self.previous_color_button.update()
    
    def try_start(self):
        self.started = True
        self.map = Map(self.width, self.height, self.colors[self.player_color])
    
    def try_next_color(self):
        self.player_color = (self.player_color + 1) % len(self.colors)
        self.color_rect.background_color = self.colors[self.player_color]

    def try_previous_color(self):
        self.player_color = (self.player_color - 1) % len(self.colors)
        self.color_rect.background_color = self.colors[self.player_color]
    
    def draw(self, surface):
        self.title_label.draw(surface)
        self.creators_label.draw(surface)
        self.start_button.draw(surface)
        self.color_rect.draw(surface)
        self.next_color_button.draw(surface)
        self.previous_color_button.draw(surface)