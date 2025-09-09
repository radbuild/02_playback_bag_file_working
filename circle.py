import pygame
import random

class Circle:
    def __init__(self, screen_width, screen_height, radius=50, color=(0, 0, 255)):
        self.radius = radius
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.center = (screen_width // 2, screen_height // 2)
        self.exists = True
        self.respawn_time = None

    def draw(self, surface):
        if self.exists:
            pygame.draw.circle(surface, self.color, self.center, self.radius)

    def check_overlap(self, position):
        """Check if a given (x, y) position overlaps the circle."""
        if not self.exists or position is None:
            return False
        dx = position[0] - self.center[0]
        dy = position[1] - self.center[1]
        if dx**2 + dy**2 <= self.radius**2:
            self.exists = False
            return True
        return False

    def schedule_respawn(self, delay_seconds):
        import time
        self.respawn_time = time.time() + delay_seconds

    def try_respawn(self):
        import time
        if not self.exists and self.respawn_time and time.time() >= self.respawn_time:
            self.center = (
                random.randint(self.radius, self.screen_width - self.radius),
                random.randint(self.radius, self.screen_height - self.radius)
            )
            self.exists = True
            self.respawn_time = None
