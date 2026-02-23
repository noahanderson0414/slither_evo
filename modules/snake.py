import pygame

class Snake:
    def __init__(self):
        self.position = pygame.Vector2()
        self.direction = pygame.Vector2(1.0, 0.0)
        self.speed = 200.0

    def update(self, delta_time: float) -> None:
        # Integrate our velocity (direction * magnitude) to position.
        self.position += self.direction * self.speed * delta_time

    def draw(self, surface: pygame.Surface) -> None:
        # Draw a circle at the position of the Snake.
        pygame.draw.circle(surface, pygame.Color(255, 255, 255, 255), self.position, 50.0)
