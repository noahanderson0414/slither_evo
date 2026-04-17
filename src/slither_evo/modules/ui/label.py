import pygame

from .element import UIElement

class UILabel(UIElement):
    def __init__(
        self,
        rect,
        font,
        text = "Placeholder",
        text_color = (255, 255, 255),
        **kwargs
    ):
        super().__init__(rect, **kwargs)

        self.font = font
        self.text = text
        self.text_color = text_color
    
    def draw(self, surface):
        super().draw(surface)

        # Create a surface with the desired text, and then blit it to the center of the draw surface.
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center = self.rect.center)
        surface.blit(text_surface, text_rect)