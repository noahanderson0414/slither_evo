import pygame

class Snake:
    def __init__(self):
        self.position = pygame.Vector2()
        self.direction = pygame.Vector2(1.0, 0.0)
        self.speed = 100.0

    def update(self, delta_time: float) -> None:
        self.position += self.speed * self.direction * delta_time
        print(delta_time)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, pygame.Color(255, 255, 255, 255), self.position, 50.0)
