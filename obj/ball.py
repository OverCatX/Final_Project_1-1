from obj.floating_object import FloatingObject
from sounds.sound import Sound


class Ball(FloatingObject):
    def __init__(self, size: int = 20, x: int = 0, y: int = 0, vx: float = 0, vy: float = 0
                 , color: tuple[int, int, int] = (0, 0, 0), screen_width: int = 800, screen_height: int = 600):
        super().__init__(size, x, y, vx, vy, color, screen_width, screen_height)
        self.sound = Sound()

    def on_hit_screen_edge(self):
        if self.x - self.size < 0 or self.x + self.size > self.screen_width:
            self.vx = -self.vx
            self.sound.run_sound('wall')
        if self.y - self.size < 0 or self.y + self.size > self.screen_height:
            self.vy = -self.vy
            self.sound.run_sound('wall')

    def on_hit_paddle(self, paddle):
        if self.x - self.size < 0 or self.x + self.size > paddle.width:
            self.vx = -self.vx
            self.sound.run_sound('paddle')
        if self.y - self.size < 0 or self.y + self.size > paddle.height:
            self.vy = -self.vy
            self.sound.run_sound('paddle')