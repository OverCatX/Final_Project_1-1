import pygame.draw


class Ball:
    def __init__(self, size:int = 20, x:int = 0, y:int = 0,vx:float = 0, vy: float =0
                 , color: str='', count: int=1, id: int = 0):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.count = count
        self.id = id
        self.screen_width = 800
        self.screen_height = 600

    def draw(self):
        display = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.draw.circle(display,self.color, (self.x, self.y), self.size)

    def on_hit_screen_edge(self):
        if self.x - self.size < 0 or self.x + self.size > self.screen_width:
            self.vx = -self.vx
        if self.y - self.size < 0 or self.y + self.size > self.screen_height:
            self.vy = -self.vy


