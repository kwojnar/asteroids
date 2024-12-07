import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    

    asteroidField = AsteroidField()

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for updatable in updatables:
            updatable.update(dt)
       
        for drawable in drawables:
            drawable.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game Over!")
                return
            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()
