import pygame

class SnekPart:
    def __init__(self, current, prev):
        self.current = current
        self.prev = prev

class Cell:
    def __init__(self, surface, x, y, size, state, width):
        self.surface = surface
        self.state = state
        self.thickness = thickness
        self.borderRect = pygame.Rect(x, y, x+size, y+size)
        self.innerRect = pygame.Rect(self.borderRect.x+self.thickness, 
                                    self.borderRect.y+self.thickness, 
                                    self.borderRect.w-self.thickness,
                                    self.borderRect.h-self.thickness)
