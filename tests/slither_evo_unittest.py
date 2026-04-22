"""
Initializes pygame and tests various features of the program.
"""

import sys
import os
import unittest

import pygame

from slither_evo.modules.snake import Snake
from slither_evo.modules.player import Player
from slither_evo.modules.upgrade import UpgradeMenu

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
pygame.font.init()

class TestXP(unittest.TestCase):
    """Tests for XP system."""

    def setUp(self):
        self.snake = Snake(1280, 720)

    def test_gain_xp(self):
        """Req9: XP increases by 1 on pickup."""
        self.snake.gain_xp()
        self.assertEqual(self.snake.xp, 1)

    def test_gain_multiple_xp(self):
        """Req9: XP accumulates correctly."""
        self.snake.gain_xp()
        self.snake.gain_xp()
        self.snake.gain_xp()
        self.snake.gain_xp()
        self.snake.gain_xp()
        self.assertEqual(self.snake.xp, 5)

    def test_xp_does_not_start_negative(self):
        """Req9: XP should not start below zero."""
        self.assertGreaterEqual(self.snake.xp, 0)

    def test_xp_does_not_increase_by_two(self):
        """Req9: XP should not increase by more than 1 per pickup."""
        self.snake.gain_xp()
        self.assertNotEqual(self.snake.xp, 2)

class TestUpgrades(unittest.TestCase):
    """Tests for upgrade system."""

    def setUp(self):
        self.player = Player(1280, 720)
        self.player.xp = 10
        self.menu = UpgradeMenu(self.player, 1280, 720)

    def test_upgrade_length_deducts_xp(self):
        """Req11: Purchasing upgrade deducts correct XP."""
        self.menu.try_upgrade_length()
        self.assertEqual(self.player.xp, 7)

    def test_upgrade_length_increases_stat(self):
        """Req12: Purchasing length upgrade increases player length."""
        original = self.player.length
        self.menu.try_upgrade_length()
        self.assertGreater(self.player.length, original)

    def test_upgrade_speed_deducts_xp(self):
        """Req11: Purchasing speed upgrade deducts correct XP."""
        self.menu.try_upgrade_speed()
        self.assertEqual(self.player.xp, 7)

    def test_upgrade_speed_increases_stat(self):
        """Req12: Purchasing speed upgrade increases player speed."""
        original = self.player.speed
        self.menu.try_upgrade_speed()
        self.assertGreater(self.player.speed, original)

    def test_upgrade_radius_deducts_xp(self):
        """Req11: Purchasing radius upgrade deducts correct XP."""
        self.menu.try_upgrade_radius()
        self.assertEqual(self.player.xp, 7)

    def test_upgrade_radius_increases_stat(self):
        """Req12: Purchasing radius upgrade increases player radius."""
        original = self.player.radius
        self.menu.try_upgrade_radius()
        self.assertGreater(self.player.radius, original)

    def test_upgrade_fails_insufficient_xp(self):
        """Req11: Upgrade does not apply when XP is insufficient."""
        self.player.xp = 0
        original_length = self.player.length
        self.menu.try_upgrade_length()
        self.assertEqual(self.player.length, original_length)

    def test_upgrade_does_not_give_xp(self):
        """Req11: Purchasing an upgrade should not increase XP."""
        self.menu.try_upgrade_length()
        self.assertLess(self.player.xp, 10)

    def test_upgrade_does_not_decrease_below_zero(self):
        """Req11: XP should not go negative after upgrade."""
        self.player.xp = 3
        self.menu.try_upgrade_length()
        self.assertGreaterEqual(self.player.xp, 0)

class TestCollision(unittest.TestCase):
    """Tests for collision detection."""

    def setUp(self):
        self.player = Player(1280, 720)

    def test_player_spawns_at_center(self):
        """Player spawns at center of screen."""
        self.assertEqual(self.player.position.x, 640)
        self.assertEqual(self.player.position.y, 360)

    def test_player_does_not_spawn_at_origin(self):
        """Player should not spawn at top left corner."""
        self.assertNotEqual(self.player.position.x, 0)
        self.assertNotEqual(self.player.position.y, 0)

    def test_player_radius_is_positive(self):
        """Player radius should always be positive."""
        self.assertGreater(self.player.radius, 0)

    def test_player_speed_is_positive(self):
        """Player speed should always be positive."""
        self.assertGreater(self.player.speed, 0)

    def test_wrap_right_edge(self):
        """Player wraps to left side when going off right edge."""
        self.player.position.x = 1281
        self.player.update(0.016)
        self.assertLessEqual(self.player.position.x, 1280)

    def test_wrap_left_edge(self):
        """Player wraps to right side when going off left edge."""
        self.player.position.x = -1
        self.player.update(0.016)
        self.assertGreaterEqual(self.player.position.x, 0)

    def test_wrap_bottom_edge(self):
        """Player wraps to top when going off bottom edge."""
        self.player.position.y = 721
        self.player.update(0.016)
        self.assertLessEqual(self.player.position.y, 720)

    def test_wrap_top_edge(self):
        """Player wraps to bottom when going off top edge."""
        self.player.position.y = -1
        self.player.update(0.016)
        self.assertGreaterEqual(self.player.position.y, 0)

if __name__ == "__main__":
    unittest.main()
