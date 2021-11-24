import pygame
from pygame.locals import *
from Cell import *

# TODO: FIX MOVEMENT ERROR IN GOING DIAGONAL FOR NO REASON

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

        # Movement
        if self.snekHead.direction == "up":
            # Top bounds check
            if previous.indexY-1 < 0:
                # Reset at bottom
                self.snekHead = self.grid[previous.indexX][len(self.grid)-1]
            else:
                self.snekHead = self.grid[previous.indexX][previous.indexY-1]
        elif self.snekHead.direction == "down":
            # Bottom bounds check
            if previous.indexY+1 > len(self.grid)-1:
                # Reset at top
                self.snekHead = self.grid[previous.indexX][0]
            else:
                self.snekHead = self.grid[previous.indexX][previous.indexY+1]
        elif self.snekHead.direction == "left":
            # Left bounds check
            if previous.indexX-1 < 0:
                # Reset at right
                self.snekHead = self.grid[len(self.grid[0])-1][previous.indexY]
            else:
                self.snekHead = self.grid[previous.indexX-1][previous.indexY]
        elif self.snekHead.direction == "right":
            # Right bounds check
            if previous.indexX+1 > len(self.grid[0])-1:
                # Reset at left
                self.snekHead = self.grid[0][previous.indexY]
            else:
                self.snekHead = self.grid[previous.indexX+1][previous.indexY]

        self.snekHead.direction = previous.direction
        self.snekHead.state = "head"
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
            self.clock.tick(5)

        self.on_cleanup()

snekGame = SnekGame(width=500, height=500, size=50)