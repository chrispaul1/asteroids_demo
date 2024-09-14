import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()

    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for update_obj in updatable:
            update_obj.update(dt)

        for asteroid in asteroids:
            if player.collision_detection(asteroid):
                print("Game Over!")
                sys.exit()

        for draw_obj in drawable:
            draw_obj.draw(screen)
    
        pygame.display.flip()

        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()