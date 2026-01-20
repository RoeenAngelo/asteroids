import sys
import pygame
from asteroid import Asteroid
from asteroidfields import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from circleshape import CircleShape
from player import Player
from shot import Shot
      
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, shots) # every shot object will be added to these groups

    Asteroid.containers = (updatable, drawable, asteroids) # every asteroid object will be added to these groups

    AsteroidField.containers = updatable # only added to updatable group because it doesn't need to be drawn
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable) # every player object will be added to these groups
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    dt = 0


    while True:
        log_state()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt) # Update all updatable objects

        for asteroid in asteroids:
           if asteroid.collides_with(player):
               log_event("player_hit")
               print("Game over!")
               sys.exit()

        screen.fill((0, 0, 0)) # Clear screen with black
        
        for obj in drawable:
            obj.draw(screen) # Draw all drawable objects

        pygame.display.flip() # Refresh the screen
        # clock.tick(60) Cap the frame rate at 60 FPS
        dt = clock.tick(60) / 1000.0 # Delta time in seconds
        

if __name__ == "__main__":
    main()
