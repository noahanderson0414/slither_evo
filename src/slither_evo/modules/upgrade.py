import pygame

class UpgradeMenu:
    def __init__(self, player, width, height):
        self.player = player
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("Arial", 30)
        self.upgrade_costs = {
            "length" : 3,
            "speed": 3,
            "radius": 3
        }

    def update(self, keys):
        # Input keys 1,2,3 to upgrade player.
        if keys[pygame.K_1]:
            if self.player.xp >= self.upgrade_costs["length"]:
                self.player.xp -= self.upgrade_costs["length"]
                self.player.length += 10
        if keys[pygame.K_2]:
            if self.player.xp >= self.upgrade_costs["speed"]:
                self.player.xp -= self.upgrade_costs["speed"]
                self.player.speed += 10
        if keys[pygame.K_3]:
            if self.player.xp >= self.upgrade_costs["radius"]:
                self.player.xp -= self.upgrade_costs["radius"]
                self.player.radius += 10

    def draw(self, screen):
        # Screen text between waves showing upgrades.
        # Length
        # Length
        text = self.font.render(f"Length: {self.player.length}", True, (255, 255, 255))
        screen.blit(text, ((self.width - text.get_width()) // 2, 250))
        text = self.font.render(f"1 - Upgrade Length (Cost: {self.upgrade_costs['length']} XP)", True, (255, 255, 255))
        screen.blit(text, ((self.width - text.get_width()) // 2, 290))

        # Speed
        text = self.font.render(f"Speed: {self.player.speed}", True, (255, 255, 255))
        screen.blit(text, ((self.width - text.get_width()) // 2, 340))
        text = self.font.render(f"2 - Upgrade Speed (Cost: {self.upgrade_costs['speed']} XP)", True, (255, 255, 255))
        screen.blit(text, ((self.width - text.get_width()) // 2, 380))

        # Radius
        text = self.font.render(f"Radius: {self.player.radius}", True, (255, 255, 255))
        screen.blit(text, ((self.width - text.get_width()) // 2, 430))
        text = self.font.render(f"3 - Upgrade Radius (Cost: {self.upgrade_costs['radius']} XP)", True, (255, 255, 255))
        screen.blit(text, ((self.width - text.get_width()) // 2, 470))

        # XP and prompt
        text = self.font.render(f"XP: {self.player.xp}", True, (255, 255, 0))
        screen.blit(text, ((self.width - text.get_width()) // 2, 530))
        text = self.font.render("Press SPACE to continue", True, (200, 200, 200))
        screen.blit(text, ((self.width - text.get_width()) // 2, 570))