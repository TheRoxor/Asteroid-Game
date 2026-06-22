import pygame
import player
import asteroid
import asteroidfield
import shot
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, drawable, updatable)

    Player1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField = asteroidfield.AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for item in updatable:
            item.update(dt)
        
        for item in asteroids:
            if item.collides_with(Player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for item in asteroids:
            for bullet in shots:
                if item.collides_with(bullet):
                    log_event("asteroid_shot")
                    bullet.kill()
                    item.split()

                

        for item in drawable:
            item.draw(screen)
        
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

    
    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
