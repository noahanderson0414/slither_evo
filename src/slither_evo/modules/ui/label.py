"""Defines the UILabel class."""

from slither_evo.modules.ui.element import UIElement

class UILabel(UIElement):
    """
    A UI label that draws some text on a rect.

    Attributes:
    - rect: Rect: The rect to be drawn.
    - background_color: Color: The color of the drawn rect.
    - border_radius: float: The radius of the circular borders.
    - font: Font: The font to draw the text with.
    - text: str: The text to be drawn.
    - text_color: Color: The color of the drawn text.
    """
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
        """Draw the label."""

        super().draw(surface)

        # Create a surface with the desired text, and then blit it to the center of the draw surface.
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center = self.rect.center)
        surface.blit(text_surface, text_rect)
