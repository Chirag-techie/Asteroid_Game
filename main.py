import pygame
import sys
from shot import *
from asteroid import *
from asteroidfield import *
from player import *
from logger import *
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
def main():
    pygame.init()
    print("Starting Asteroids with pygame version: 2.6.1")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #initialising gropus
    
    asteroids=pygame.sprite.Group()
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    shots=pygame.sprite.Group()

    #Initialising Class to containers

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers=(updatable,)
    Shot.containers=(shots,updatable,drawable)

    asteroidfield=AsteroidField()
    clock=pygame.time.Clock()
    dt=0
    player=Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black")
        
        for shape in drawable:
            shape.draw(screen)
        
        pygame.display.flip()
        dt=clock.tick(60)/1000
                

if __name__ == "__main__":
    main()
