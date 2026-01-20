from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, LINE_WIDTH, PLAYER_SPEED, SHOT_RADIUS
from circleshape import CircleShape
import pygame

from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # in degrees
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt  # Rotate clockwise
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt) # Rotate counter-clockwise
        if keys[pygame.K_d]: 
            self.rotate(dt) # Rotate clockwise
        if keys[pygame.K_s]:
            self.move(-dt) # Move backward
        if keys[pygame.K_w]:
            self.move(dt)  # Move forward
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation) #rotate method from pygame
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        shot  = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


        # from shot import Shot  # Import here to avoid circular dependency
        # shot = Shot(self.position.x, self.position.y, radius=5)
        # direction = pygame.Vector2(0, 1).rotate(self.rotation)
        # shot.velocity = direction * 500  # Set shot speed
        # return shot
    