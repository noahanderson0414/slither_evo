"""
Defines the UIElement class.
"""

import pygame

class UIElement:
    """
    A basic UI element that is just a rect with a user defined size.

    Attributes:
    - rect: Rect: The rect to be drawn.
    - background_color: Color: The color of the drawn rect.
    - border_radius: float: The radius of the circular borders.
    """
    def __init__(
        self,
        rect,
        background_color = (0, 0, 0, 128),
        border_radius = 10,
    ):
        self.rect = rect
        self.background_color = background_color
        self.border_radius = border_radius

    def draw(self, surface):
        """
        Draw the UI element onto a surface.

        Arguments:
        - surface: Surface: The surface to draw to.
        """

        # Create a temporary surface so we can draw with transparency.
        temp_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        # Draw the rect to the temporary surface.
        pygame.draw.rect(
            temp_surface,
            self.background_color,
            temp_surface.get_rect(),
            border_radius = self.border_radius
        )

        # Blit the temporary surface to the draw surface.
        surface.blit(temp_surface, self.rect.topleft)
