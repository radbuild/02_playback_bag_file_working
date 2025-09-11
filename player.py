import pygame

class Player:
    def __init__(self, screen_width, screen_height, image_path="player.png"):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, (screen_height // 2) - 150)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move_left(self, pixels=10):
        self.rect.x -= pixels
        # self.rect.x = max(0, self.rect.x - pixels)

    def move_right(self, pixels=10):
        self.rect.x += pixels
        # self.rect.x = max(0, self.rect.x - pixels)