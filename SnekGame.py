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
        
        # Init Snake
        self.snekHead = self.grid[0][0]
        self.snekHead.state = "head"
        self.snekHead.render()

        self.snekHead.direction = "right"

        self.clock = pygame.time.Clock()

        self.main()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.snekHead.direction = "up"
            if event.key == pygame.K_DOWN:
                self.snekHead.direction = "down"
            if event.key == pygame.K_LEFT:
                self.snekHead.direction = "left"
            if event.key == pygame.K_RIGHT:
                self.snekHead.direction = "right"
    
    def on_loop(self):
        previous = self.snekHead

        if self.snekHead.indexX-1 < 0:
            self.snekHead = self.grid[len(self.grid[self.snekHead.indexY])-1][self.snekHead.indexY]
        elif self.snekHead.indexX+1 > len(self.grid[self.snekHead.indexY])-1:
            self.snekHead = self.grid[self.snekHead.indexX][self.snekHead.indexY]

        self.snekHead.prev = previous
        self.snekHead.prev.state = None


    def on_render(self):
        self.snekHead.prev.render()
        self.snekHead.render()

    def on_cleanup(self):
        pygame.quit()
    
    def main(self):
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(1)

        self.on_cleanup()

snekGame = SnekGame(width=500, height=500, size=50)