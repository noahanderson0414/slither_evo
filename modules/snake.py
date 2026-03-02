import pygame

class Snake:
    def __init__(self):
        self.position = pygame.Vector2()
        self.position_history = []
        self.direction = pygame.Vector2(1.0, 0.0)
        self.speed = 200.0
        self.length = 100
        self.xp = 0


    def gain_xp(self):
        # Xp function, can sort it out later
        self.xp += 1

    def update(self, delta_time: float) -> None:
        # Add the old position to position_history.
        self.position_history.append(pygame.Vector2(self.position.x, self.position.y))
        if len(self.position_history) >= self.length:
            self.position_history.pop(0)

        # Integrate our velocity (direction * magnitude) to position.
        self.position += self.direction * self.speed * delta_time


    def draw(self, surface: pygame.Surface) -> None:
        # Draw a circle at the current position of the Snake and all positions in the history.
        pygame.draw.circle(surface, pygame.Color(255, 255, 255, 255), self.position, 25.0)
        for position in self.position_history:
            pygame.draw.circle(surface, pygame.Color(255, 255, 255, 255), position, 25.0)