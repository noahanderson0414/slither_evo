import pygame

from .label import UILabel

class UIButton(UILabel):
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
        self.hovered = False
        self.clicked = False

        mouse_pos = pygame.mouse.get_pos()
        mouse_button_held = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse_pos):
            self.hovered = True
            if mouse_button_held and not self.mouse_button_held:
                self.clicked = True
                self.click_held = True
                self.callback()
        
        self.mouse_button_held = mouse_button_held
        self.click_held = self.click_held and mouse_button_held

    def draw(self, surface):
        background_color = self.background_color

        if self.click_held:
            self.background_color = self.clicked_background_color
        elif self.hovered:
            self.background_color = self.hover_background_color
        
        super().draw(surface)
        self.background_color = background_color

        