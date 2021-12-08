from SnekGame import SnekGame
import pygame
from pygame.locals import *

displayRes = width, height = (500, 200)

if __name__ == "__main__":
    # Init Window
    pygame.init()
    displaySurf = pygame.display.set_mode(displayRes, pygame.HWSURFACE | pygame.DOUBLEBUF)
    clock = pygame.time.Clock()
    running = True

    snekGame = SnekGame(displaySurf, width, height, size=50)
        
    while running:
        for event in pygame.event.get():
            snekGame.on_event(event)
        snekGame.on_loop()
        snekGame.on_render()

        print(snekGame.get_state())

        pygame.display.flip()
        clock.tick(7)

    snekGame.on_cleanup()