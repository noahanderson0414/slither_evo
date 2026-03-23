import pygame

class Snake:
    """
    Class that represents a Snake (character) that can move around the world, collide, die, etc.

    Attributes:
      - position: Vector2: 2D position of the Snake.
      - position_history: List[Vector2]: Past positions of the Snake. Length of this List also determines the length of the Snake.
      - speed: float: Speed that the Snake should move.
      - length: int: Number of segments the Snake can have.
      - xp: int: How much XP the Snake has.
      - dead: bool: Whether the Snake is dead or not.
      - width: int: Width of the Map.
      - height: int: Height of the Map.
      - radius: float: Radius of each segment of the Snake.
    """

    def __init__(self, width, height):
        self.position = pygame.Vector2()
        self.position_history = []
        self.direction = pygame.Vector2(1.0, 0.0)
        self.speed = 200.0
        self.length = 100
        self.xp = 0
        self.dead = False
        self.width = width
        self.height = height
        self.radius = 25.0

    def gain_xp(self):
        """
        Give the Snake some XP.
        """

        # XP function, can sort it out later.
        self.xp += 1

    def update(self, delta_time: float) -> None:
        """
        Update the physics of the Snake.

        Arguments:
          - delta_time: float: Time since last frame.
        """

        # Wraps around to the other side of the Map if you hit the edge.
        if self.position.x > self.width:
            self.position.x = 0
            self.position.y = self.height - self.position.y
        if self.position.x < 0:
            self.position.x = self.width
            self.position.y = self.height - self.position.y
        if self.position.y > self.height:
            self.position.y = 0
            self.position.x = self.width - self.position.x
        if self.position.y < 0:
            self.position.y = self.height
            self.position.x = self.width - self.position.x

        # Add the old position to position_history.
        self.position_history.append(pygame.Vector2(self.position.x, self.position.y))
        if len(self.position_history) >= self.length:
            self.position_history.pop(0)

        # Integrate our velocity (direction * magnitude) to position.
        self.position += self.direction * self.speed * delta_time

        # Commenting out self-collision code for now to try and test movement functions.
        '''
        for i in range(len(self.position_history) - 50):
            if self.position.distance_to(self.position_history[i]) <= 50.0:
                self.dead = True
        '''

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the Snake.

        Arguments:
          - surface: Surface: The Surface to draw the Snake to.
        """

        # Draw a circle at the current position of the Snake and all positions in the history.
        pygame.draw.circle(surface, pygame.Color(255, 255, 255, 255), self.position, self.radius)
        for position in self.position_history:
            pygame.draw.circle(surface, pygame.Color(255, 255, 255, 255), position, self.radius)
