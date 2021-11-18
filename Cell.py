import pygame

class SnekPart:
    def __init__(self, current, prev):
        self.current = current
        self.prev = prev

class Cell:
    def __init__(self, surface, x, y, size, thickness, state):
        self.surface = surface
        self.state = state
        self.thickness = thickness
        self.rect = pygame.Rect(x, y, x+size, y+size)
    
    def render(self):
        if self.state == "head":
            color = pygame.Color(0,255,0)
        elif self.state == "tail":
            color = pygame.Color(0,255,135)
        elif self.state == "apple":
            color = pygame.Color(255,0,0)
        else:
            color = pygame.Color(0,0,0)
        
        innerRect = pygame.Rect(self.rect.x+self.thickness, 
                                self.rect.y+self.thickness, 
                                self.rect.w-self.thickness, 
                                self.rect.h-self.thickness)
        pygame.draw.rect(self.surface, color, innerRect)  # Fill
        pygame.draw.rect(self.surface, (255,255,255), self.rect, width=self.thickness)  # Border