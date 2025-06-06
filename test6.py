import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity: Cork vs Super Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 80, 80)
BLUE = (80, 80, 255)

# Ball properties
gravity = 0.5  # acceleration due to gravity

# Ball 1: Super Ball
super_y = 50
super_speed = 0
super_mass = 0.1

# Ball 2: Cork Ball
cork_y = 50
cork_speed = 0
cork_mass = 0.16

clock = pygame.time.Clock()

# Main Loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Super Ball Physics
    super_force = gravity * super_mass
    super_speed += super_force
    super_y += super_speed

    # Cork Ball Physics
    cork_force = gravity * cork_mass
    cork_speed += cork_force
    cork_y += cork_speed

    # Ground Collision
    if super_y >= HEIGHT - 50:
        super_y = HEIGHT - 50
        super_speed = -super_speed * 0.7  # bounce effect

    if cork_y >= HEIGHT - 50:
        cork_y = HEIGHT - 50
        cork_speed = -cork_speed * 0.7

    # Draw Balls
    pygame.draw.circle(screen, BLUE, (200, int(super_y)), 20)
    pygame.draw.circle(screen, RED, (400, int(cork_y)), 20)

    # Labels
    font = pygame.font.SysFont(None, 24)
    screen.blit(font.render("Super Ball", True, (0, 0, 0)), (160, 20))
    screen.blit(font.render("Cork Ball", True, (0, 0, 0)), (370, 20))

    pygame.display.flip()
    clock.tick(60)
