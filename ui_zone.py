import pygame

class GestureZone:
    def __init__(self, rect, label, color=(0, 255, 0), active_color=(255, 0, 0)):
        self.rect = rect
        self.label = label
        self.color = color
        self.active_color = active_color
        self.is_active = False
        self.font = pygame.font.SysFont(None, 36)

    def check_overlap(self, position):
        if position and self.rect.collidepoint(position):
            self.is_active = True
            return True
        self.is_active = False
        return False

    def draw(self, surface):
        pygame.draw.rect(surface, self.active_color if self.is_active else self.color, self.rect, 2)
        label_surface = self.font.render(self.label, True, self.color)
        surface.blit(label_surface, (self.rect.x + 5, self.rect.y + 5))
