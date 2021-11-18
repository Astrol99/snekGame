import pygame
from pygame.locals import *
from Cell import *

class SnekGame:
    def __init__(self, width, height, size, thickness):
        self.displayRes = self.width, self.height = width, height
        self.size = size
        self.thickness = thickness        

        self.on_execute()
    
    def on_init(self):
        # Init Window
        pygame.init()
        self.displaySurf = pygame.display.set_mode(self.displayRes, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True

        # Init Grid 
        self.grid = []

        for y in range(0, self.height, self.size):
            row = []
            for x in range(0, self.width, self.size):
                cell = Cell(self.displaySurf, x, y, self.size, self.thickness, state=None)
                cell.render()

                row.append(cell)
            self.grid.append(row)

        # Init Snake Head
        self.grid[1][1].state = "apple"
        self.grid[1][1].render()

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

            pygame.display.flip()
            pygame.display.update()

        self.on_cleanup()

SnekGame(width=500,height=500,size=10,thickness=1)