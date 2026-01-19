import pygame
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

    player = Player(x = SCREEN_WIDTH // 2, y =SCREEN_HEIGHT // 2)
    while True:
        log_state()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0)) # Clear screen with black
        player.draw(screen) # Draw the player
        pygame.display.flip() # Refresh the screen
        clock.tick(60) # Cap the frame rate at 60 FPS
        dt = clock.tick() / 1000.0 # Delta time in seconds
        

if __name__ == "__main__":
    main()
