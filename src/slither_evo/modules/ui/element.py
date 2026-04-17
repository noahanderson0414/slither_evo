import pygame

class UIElement:
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