import pygame
from pygame.locals import *

class SnekGame:
    def __init__(self):
        self.running = True
        self.displaySurf = None
        self.size = self.weight, self.height = 500, 500
    
    def on_init(self):
        pygame.init()
        self.displaySurf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
    
    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()
    
    def on_execute(self):
        if self.on_init() == False:
            self.running = False
        
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

SnekGame().on_execute()