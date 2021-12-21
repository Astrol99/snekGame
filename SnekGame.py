import pygame
from pygame.locals import *
from Cell import *
import random

class SnekGame:
    def __init__(self, surface, width, height, size, thickness=1):
        self.running = True
        self.displaySurf = surface
        self.displayRes = self.width, self.height = width, height
        self.size = size
        self.thickness = thickness

        # Grid Max Index Size Constants
        self.maxRows = (self.height//self.size) - 1
        self.maxCols = (self.width//self.size)  - 1

        # Init Grid 
        self.grid = []

        for y in range(0, self.height, self.size):
            row = []
            for x in range(0, self.width, self.size):
                cell = Cell(self.displaySurf, x, y, self.size)
                cell.render()

                row.append(cell)
            self.grid.append(row)
        
        # Init Apple
        self.apple = self.grid[0][0]
        self.apple.state = "blah"
        self.regenerate_apple()
        
        # Init Snake
        self.snekHead = self.grid[0][0]
        self.snekHead.state = "head"
        self.snekHead.direction = "right"
        self.snekHead.render()

        self.snekLength = 0

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            # Movement keys restricted from going opposite direction
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
        
        # Movement and check if within bounds
        if self.snekHead.direction == "up" and self.snekHead.row-1 >= 0:
            self.snekHead = self.grid[previous.row-1][previous.col]                         # Up
        elif self.snekHead.direction == "down" and self.snekHead.row+1 <= self.maxRows:
            self.snekHead = self.grid[previous.row+1][previous.col]                         # Down
        elif self.snekHead.direction == "left" and self.snekHead.col-1 >= 0:
            self.snekHead = self.grid[previous.row][previous.col-1]                         # Left
        elif self.snekHead.direction == "right" and self.snekHead.col+1 <= self.maxCols:
            self.snekHead = self.grid[previous.row][previous.col+1]                         # Right
        else:
            self.running = False
    
        # Collision Checks
        if self.snekHead.state == "apple":
            self.snekLength += 1
            self.regenerate_apple()
        elif self.snekHead.state == "tail":
            self.running = False

        # Update new head and inherit direction of previous cell
        self.snekHead.state = "head"
        self.snekHead.direction = previous.direction
        self.snekHead.prev = previous
        
        # Backtrack through previous cells and assigning them as tails
        # to depth of the amount of apples eaten (using same concept as
        # linked lists)
        current = self.snekHead.prev
        for i in range(self.snekLength):
            if current != None:
                current.state = "tail"
                current.render()
                current = current.prev
        
        # Always update last end to regular cell so tail follows head
        current.reset()

    def regenerate_apple(self):
        # Keep on looking for empty cell that new apple can be placed
        # in order to prevent tragedies i.e. new apple on snek tail
        # TODO: Add win condition when max length has been reached and fix infinite loop looking for new apple cell at win con
        while self.apple.state != None:
            self.apple = self.grid[random.randint(0, self.maxRows)][random.randint(0, self.maxCols)]
        self.apple.state = "apple"
        self.apple.render()
    
    # Returns new 2D array that represents grid array in simple number states
    # 0 = empty
    # 1 = apple
    # 2 = tail
    # 3 = head
    def get_state(self):
        state = []
        for row in self.grid:
            new_row = []
            for item in row:
                if item.state == "head":
                    new_row.append(1)
                elif item.state == "tail":
                    new_row.append(2)
                elif item.state == "apple":
                    new_row.append(3)
                else:
                    new_row.append(0)
            state.append(new_row)
        return state

    def on_render(self):
        self.snekHead.render()

    def on_cleanup(self):
        pygame.quit()