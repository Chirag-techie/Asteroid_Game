import pygame
from player import Player
from logger import log_state
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
def main():
    pygame.init()
    print("Starting Asteroids with pygame version: 2.6.1")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    clock=pygame.time.Clock()
    dt=0
    player=Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        screen.fill("black")
        
        for shape in drawable:
            shape.draw(screen)
        
        pygame.display.flip()
        dt=clock.tick(60)/1000
                

if __name__ == "__main__":
    main()
