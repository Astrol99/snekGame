import pygame
from pygame.locals import *

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
                cell = Cell(self.displaySurf, x, y, self.size, self.thickness, state=None)
                self.render_cell(cell)

                row.append(cell)
            self.grid.append(row)

        # Init Snake Head
        self.grid[1][1].state = "apple"
        print(self.grid[1][1].borderRect)
        print(self.grid[1][1].innerRect)
        self.grid[1][1].render()

        self.main()
    
    def render_cell(self, cell):
        if self.state == "head":
            color = pygame.Color(0,255,0)
        elif self.state == "tail":
            color = pygame.Color(0,255,135)
        elif self.state == "apple":
            color = pygame.Color(255,0,0)
        else:
            color = pygame.Color(0,0,0)

        pygame.draw.rect(self.displaySurf, (255,255,255), cell.borderRect, width=self.thickness)  # Border
        pygame.draw.rect(self.displaySurf, color, cell.innerRect)  

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

snekGame = SnekGame(width=500, height=500,size=50)