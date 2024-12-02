import pygame.draw

class MysteryBlock:
    def __init__(self, width:int, height: int, x: int, y: int, vy: float, color: str, id: int):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vy = vy
        self.color = color
        self.id = id
        self.screen_width = 800
        self.screen_height = 600

    def draw(self):
        display = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.draw.rect(display,self.color, (self.x, self.y), 30, 3)