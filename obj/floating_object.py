import pygame

from sounds.sound import Sound


class FloatingObject:
    def __init__(self, size: int, x: int, y: int, vx: float, vy: float, color: tuple[int, int, int]
                 , screen_width: int, screen_height: int):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.sound = Sound()

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.x, self.y), self.size)

    def updates(self):
        self.x += self.vx
        self.y += self.vy
        self.on_hit_screen_edge()

    def on_hit_screen_edge(self):
        if self.x - self.size < 0 or self.x + self.size > self.screen_width:
            self.vx = -self.vx
        if self.y - self.size < 0 or self.y + self.size > self.screen_height:
            self.vy = -self.vy