import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pool Game Demo")

clock = pygame.time.Clock()

# Load ball and hole images
ball_image = pygame.image.load("assets/biy/real-biy-1.png").convert_alpha()
hole_image = pygame.image.load("assets/gure.png").convert_alpha()

# Define constants
BALL_RADIUS = 2
FRICTION = 0.99
GRAVITY = 0.1


# Ball class
class Ball:
    def __init__(self, x, y, vx=0, vy=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self, balls):
        self.x += self.vx
        self.y += self.vy

        self.vx *= FRICTION
        self.vy *= FRICTION

        self.vy += GRAVITY

        # Keep the ball within the screen bounds
        if self.x < BALL_RADIUS:
            self.x = BALL_RADIUS
            self.vx *= -1
        elif self.x > width - BALL_RADIUS:
            self.x = width - BALL_RADIUS
            self.vx *= -1
        if self.y < BALL_RADIUS:
            self.y = BALL_RADIUS
            self.vy *= -1
        elif self.y > height - BALL_RADIUS:
            self.y = height - BALL_RADIUS
            self.vy *= -1

        # Handle ball-ball collisions
        for ball in balls:
            if ball != self:
                dx = self.x - ball.x
                dy = self.y - ball.y
                distance = math.sqrt(dx ** 2 + dy ** 2)

                if distance < 2 * BALL_RADIUS:
                    angle = math.atan2(dy, dx)
                    sin_angle = math.sin(angle)
                    cos_angle = math.cos(angle)

                    # Rotate the velocities
                    vx1 = self.vx * cos_angle + self.vy * sin_angle
                    vy1 = self.vy * cos_angle - self.vx * sin_angle
                    vx2 = ball.vx * cos_angle + ball.vy * sin_angle
                    vy2 = ball.vy * cos_angle - ball.vx * sin_angle

                    # Calculate new velocities after collision
                    v1x = ((BALL_RADIUS - BALL_RADIUS) * vx1 + (2 * BALL_RADIUS) * vx2) / (BALL_RADIUS + BALL_RADIUS)
                    v2x = ((2 * BALL_RADIUS) * vx1 + (BALL_RADIUS - BALL_RADIUS) * vx2) / (BALL_RADIUS + BALL_RADIUS)
                    v1y = vy1
                    v2y = vy2

                    # Rotate the velocities back
                    self.vx = v1x * cos_angle - v1y * sin_angle
                    self.vy = v1y * cos_angle + v1x * sin_angle
                    ball.vx = v2x * cos_angle - v2y * sin_angle
                    ball.vy = v2y * cos_angle + v2x * sin_angle

    def apply_force(self, force):
        self.vx += force[0]
        self.vy += force[1]

    def draw(self, surface):
        ball_rect = ball_image.get_rect(center=(self.x, self.y))
        surface.blit(ball_image, ball_rect)


# Hole class
class Hole:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        hole_rect = hole_image.get_rect(center=(self.x, self.y))
        surface.blit(hole_image, hole_rect)


if __name__ == "__main__":
    # Create balls and holes
    ball1 = Ball(200, 300)
    ball2 = Ball(400, 300)
    hole = Hole(400, 100)
    balls = [ball1, ball2]

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Apply forces to the balls (e.g., from user input or collisions)
        # In this example, we apply a constant force to ball1
        force = (0.1, 0.1)
        ball1.apply_force(force)

        # Update the balls' positions and velocities
        for ball in balls:
            ball.update(balls)

        # Clear the screen
        screen.fill((0, 128, 0))

        # Draw the balls and holes
        ball1.draw(screen)
        ball2.draw(screen)
        hole.draw(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    # Quit the game
    pygame.quit()
