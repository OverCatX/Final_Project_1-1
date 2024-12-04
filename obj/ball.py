import pygame.draw

from ..padball_game import PadBallGame

class Ball:
    def __init__(self, size: int = 20, x: int = 0, y: int = 0, vx: float = 0, vy: float = 0
                 , color: tuple[int, int, int] = (0, 0, 0), screen_width: int = 800, screen_height: int = 600):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.x, self.y), self.size)

    def updates(self, paddle = None):
        self.x += self.vx
        self.y += self.vy

        self.on_hit_screen_edge()
        if paddle is not None:
            self.on_hit_paddle(paddle)

    def on_hit_screen_edge(self):
        if self.x - self.size < 0 or self.x + self.size > self.screen_width:
            self.vx = -self.vx
        if self.y - self.size < 0 or self.y + self.size > self.screen_height:
            self.vy = -self.vy

    def on_hit_paddle(self, paddle):
        if self.x - self.size < 0 or self.x + self.size > paddle.width:
            self.vx = -self.vx
            PadBallGame.hit_paddle_sound.play()
        if self.y - self.size < 0 or self.y + self.size > paddle.height:
            self.vy = -self.vy
            PadBallGame.hit_paddle_sound.play()