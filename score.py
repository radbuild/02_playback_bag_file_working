import pygame

class ScoreManager:
    def __init__(self, font_size=48, color=(0, 0, 0)):
        self.score = 0
        self.font = pygame.font.SysFont(None, font_size)
        self.color = color

    def increment(self):
        self.score += 1

    def render(self, surface, position=(20, 20)):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        surface.blit(score_text, position)
