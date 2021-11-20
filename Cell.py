import pygame

class Cell:
    def __init__(self, surface, x, y, size, thickness=1, state=None):
        self.surface = surface
        self.x = x
        self.y = y
        self.size = size
        self.thickness = thickness
        self.state = state

        self.indexX = self.x//size
        self.indexY = self.y//size

        self.direction = None
        self.prev = None

    def render(self):
        if self.state == "head":
            color = pygame.Color(0,255,0)
        elif self.state == "tail":
            color = pygame.Color(0,255,135)
        elif self.state == "apple":
            color = pygame.Color(255,0,0)
        else:
            color = pygame.Color(0,0,0)
        
        self.borderRect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.innerRect = pygame.Rect(self.borderRect.x+self.thickness, 
                                    self.borderRect.y+self.thickness, 
                                    self.borderRect.w-self.thickness,
                                    self.borderRect.h-self.thickness)

        pygame.draw.rect(self.surface, (255,255,255), self.borderRect, width=self.thickness)  # Border
        pygame.draw.rect(self.surface, color, self.innerRect)