import pygame
import sys
import time
from score import ScoreManager
from circle import Circle
# from realsense_input import RealSenseMotion

# Initialize Pygame
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Motion-Based Circle Game")

WHITE = (255, 255, 255)

# Game objects
circle = Circle(width, height)
score_manager = ScoreManager()
# motion_detector = RealSenseMotion(width, height)

clock = pygame.time.Clock()
running = True

try:
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get motion position from RealSense
        # motion_pos = motion_detector.get_motion_position()

        # if motion_pos and circle.check_overlap(motion_pos):
        #     score_manager.increment()
        #     circle.schedule_respawn(1)
        
        circle.try_respawn()
        circle.draw(screen)
        score_manager.render(screen)

        # circlePosX = circle.center
        # print(circlePosX)

        pygame.display.flip()
        clock.tick(30)

finally:
    # motion_detector.stop()
    pygame.quit()
    sys.exit()
