"""
Defines the UIButton class.
"""

import pygame

from slither_evo.modules.ui.label import UILabel

class UIButton(UILabel):
    """
    A UI button that draws a label and calls a callback when the user clicks it.

    Attributes:
    - rect: Rect: The rect to be drawn.
    - background_color: Color: The color of the drawn rect.
    - border_radius: float: The radius of the circular borders.
    - font: Font: The font to draw the text with.
    - text: str: The text to be drawn.
    - text_color: Color: The color of the drawn text.
    - callback: Callable: The function to be called when the button is clicked.
    - hover_background_color: Color: The color to draw the rect with when the button is hovered.
    - clicked_background_color: Color: The color to draw the rect with when the button is clicked.
    - mouse_button_held: bool: Whether the mouse button is held.
    - hovered: bool: Whether the button is hovered.
    - clicked: bool: Whether the button was just clicked.
    - click_held: bool: Whether the button is being held since the last click.
    """

    def __init__(
        self,
        rect,
        font,
        callback,
        hover_background_color = (32, 32, 32, 128),
        clicked_background_color = (255, 255, 255, 128),
        **kwargs
    ):
        super().__init__(rect, font, **kwargs)

        self.callback = callback
        self.hover_background_color = hover_background_color
        self.clicked_background_color = clicked_background_color
        self.mouse_button_held = False
        self.hovered = False
        self.clicked = False
        self.click_held = False

    def update(self):
        """Update the button and its input."""

        self.hovered = False
        self.clicked = False

        mouse_pos = pygame.mouse.get_pos()
        mouse_button_held = pygame.mouse.get_pressed()[0]

        # If the mouse_pos is contained within the rect, the button is being hovered.
        if self.rect.collidepoint(mouse_pos):
            self.hovered = True

            # If the mouse button is held this frame and not last frame, then the button was clicked.
            if mouse_button_held and not self.mouse_button_held:
                self.clicked = True
                self.click_held = True
                self.callback()
        
        self.mouse_button_held = mouse_button_held
        self.click_held = self.click_held and mouse_button_held

    def draw(self, surface):
        """
        Draw the button onto some surface.

        Arguments:
        - surface: Surface: The surface to draw onto.
        """

        background_color = self.background_color

        # If the button is held or hovered, change the background color.
        if self.click_held:
            self.background_color = self.clicked_background_color
        elif self.hovered:
            self.background_color = self.hover_background_color
        
        super().draw(surface)
        self.background_color = background_color
