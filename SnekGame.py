import pygame
from pygame.locals import *
from Cell import *
import random

class SnekGame:
    def __init__(self, width, height, size, thickness=1):
        self.displayRes = self.width, self.height = width, height
        self.size = size
        self.thickness = thickness

        # Grid Max Index Size Constants
        self.indexHeight = (self.height//self.size) - 1
        self.indexWidth  = (self.width//self.size)  - 1

        # Init Window
        pygame.init()
        self.displaySurf = pygame.display.set_mode(self.displayRes, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True

        # Init Grid 
        self.grid = []

        for x in range(0, self.height, self.size):
            row = []
            for y in range(0, self.width, self.size):
                cell = Cell(self.displaySurf, x, y, self.size)
                cell.render()

                row.append(cell)
            self.grid.append(row)
        
        # Init Snake
        self.snekHead = self.grid[1][0]
        self.snekHead.state = "head"
        self.snekHead.direction = "right"
        self.snekHead.render()

        self.snekLength = 0

        # Init Apple
        self.apple = self.grid[5][5]
        self.apple.state = "apple"
        self.apple.render()

        self.clock = pygame.time.Clock()

        self.main()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.snekHead.direction != "down":
                self.snekHead.direction = "up"
            if event.key == pygame.K_DOWN and self.snekHead.direction != "up":
                self.snekHead.direction = "down"
            if event.key == pygame.K_LEFT and self.snekHead.direction != "right":
                self.snekHead.direction = "left"
            if event.key == pygame.K_RIGHT and self.snekHead.direction != "left":
                self.snekHead.direction = "right"
    
    def on_loop(self):
        previous = self.snekHead
        
        # Movement
        if self.snekHead.direction == "up":
            # Top bounds check
            if previous.indexY-1 < 0:
                # Reset at bottom
                self.snekHead = self.grid[previous.indexX][self.indexHeight]
            else:
                self.snekHead = self.grid[previous.indexX][previous.indexY-1]
        elif self.snekHead.direction == "down":
            # Bottom bounds check
            if previous.indexY+1 > self.indexHeight:
                # Reset at top
                self.snekHead = self.grid[previous.indexX][0]
            else:
                self.snekHead = self.grid[previous.indexX][previous.indexY+1]
        elif self.snekHead.direction == "left":
            # Left bounds check
            if previous.indexX-1 < 0:
                # Reset at right
                self.snekHead = self.grid[self.indexWidth][previous.indexY]
            else:
                self.snekHead = self.grid[previous.indexX-1][previous.indexY]
        elif self.snekHead.direction == "right":
            # Right bounds check
            if previous.indexX+1 > self.indexWidth:
                # Reset at left
                self.snekHead = self.grid[0][previous.indexY]
            else:
                self.snekHead = self.grid[previous.indexX+1][previous.indexY]
        
        # Apple Check
        if self.snekHead.state == "apple":
            self.snekLength += 1
            self.regenerate_apple()

        self.snekHead.state = "head"
        self.snekHead.direction = previous.direction
        self.snekHead.prev = previous
        self.snekHead.prev.reset()

    def regenerate_apple(self):
        self.apple = self.grid[random.randint(0, self.indexWidth)][random.randint(0, self.indexHeight)]
        self.apple.state = "apple"
        self.apple.render()

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
            self.clock.tick(7)

        self.on_cleanup()

snekGame = SnekGame(width=500, height=500, size=50)