import pygame
import sys
import time
from score import ScoreManager
from circle import Circle
from realsense_input import RealSenseMotion
from ui_zone import GestureZone
from player import Player

# Initialize Pygame
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Motion-Based Circle Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game objects
circle = Circle(width, height)
score_manager = ScoreManager()

# Define a rectangular gesture zone
# zone_rect = pygame.Rect(100, 100, 200, 150)

zone_left = GestureZone(pygame.Rect(50, 350, 150, 50), "Left")
zone_right = GestureZone(pygame.Rect(450, 350, 150, 50), "Right")
zones = [zone_left, zone_right]

player = Player(width, height)

# try:
#     motion_detector = RealSenseMotion(width, height)

# except RuntimeError as e:
#     if "No device connected" in str(e):
#         print("[ERROR] No Intel RealSense device detected. Please check USB connection.")
#         sys.exit(1)

clock = pygame.time.Clock()
running = True
# simulate_trigger = False

try:
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Simulate trigger with keyboard "space"
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         simulate_trigger = True        
        
        # Get motion position from RealSense
        # motion_pos = motion_detector.get_motion_position()

        # Simulate trigger with keyboard "space"
        # motion_pos = (circle.center[0], circle.center[1]) if simulate_trigger else None
        # simulate_trigger = False    # Reset after one frame

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, RED, mouse_pos, 5)

        player.draw(screen)

        for zone in zones:
            if zone.check_overlap(mouse_pos):
                if zone.label == "Left":
                    player.move_left()  # Player move left
                elif zone.label == "Right":
                    player.move_right()
            zone.draw(screen)

        # Simulate motion if mouse hovers over the circle
        motion_pos = mouse_pos if circle.check_overlap(mouse_pos) else None

        # pygame.draw.rect(screen, GREEN, zone_rect, 2)

        # Check overlap bet. zone and motion
        # if motion_pos:
        # if zone_rect.collidepoint(mouse_pos):
        #     print("Motion detected in gesture zone!")

        if motion_pos:
            score_manager.increment()
            circle.schedule_respawn(0.5)
            print("Pop balloon")
                    
        circle.try_respawn()
        circle.draw(screen)
        score_manager.render(screen)

        pygame.display.flip()
        clock.tick(30)

finally:
    # motion_detector.stop()
    pygame.quit()
    sys.exit()
