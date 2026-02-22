import pygame

class Snake:
    def __init__(self):
        self.position = pygame.Vector2()
        self.direction = pygame.Vector2(1.0, 0.0)
        self.speed = 200.0
        # Angle we're facing
        self.angle = 0.0
        # Turn speed, can tweak later
        self.turn_speed = 200.0

    def update(self, delta_time: float, keys) -> None:
        # Key inputs, just A/D for now, can change later
        if keys[pygame.K_a]:
            self.angle -= self.turn_speed * delta_time
        if keys[pygame.K_d]:
            self.angle += self.turn_speed * delta_time
        self.direction = pygame.Vector2(1, 0).rotate(self.angle)
        self.position += self.direction * self.speed * delta_time
        #print(delta_time)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, pygame.Color(255, 255, 255, 255), self.position, 50.0)