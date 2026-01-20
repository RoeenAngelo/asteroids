import pygame
from asteroid import Asteroid
from asteroidfields import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from circleshape import CircleShape
from player import Player
      
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()


    while True:
        log_state()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt) # Update all updatable objects
        screen.fill((0, 0, 0)) # Clear screen with black
        for obj in drawable:
            obj.draw(screen) # Draw all drawable objects
        pygame.display.flip() # Refresh the screen
        # clock.tick(60) Cap the frame rate at 60 FPS
        dt = clock.tick(60) / 1000.0 # Delta time in seconds
        

if __name__ == "__main__":
    main()
