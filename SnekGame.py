import pygame
from pygame.locals import *
from Cell import *

class SnekGame:
    def __init__(self, width, height, size, thickness=1):
        self.displayRes = self.width, self.height = width, height
        self.size = size
        self.thickness = thickness        

        # Init Window
        pygame.init()
        self.displaySurf = pygame.display.set_mode(self.displayRes, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True

        # Init Grid 
        self.grid = []

        for y in range(0, self.height, self.size):
            row = []
            for x in range(0, self.width, self.size):
                cell = Cell(self.displaySurf, x, y, self.size)
                cell.render()

                row.append(cell)
            self.grid.append(row)
        
        self.grid[0][0].state = "head"
        self.grid[0][0].render()

        self.main()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
    
    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()
    
    def main(self):
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

            pygame.display.flip()

        self.on_cleanup()

snekGame = SnekGame(width=500, height=500, size=50)