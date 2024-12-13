from obj.floating_object import FloatingObject

class Ball(FloatingObject):
    def __init__(self, size: int = 20, x: int = 0, y: int = 0, vx: float = 0, vy: float = 0
                 , color: tuple[int, int, int] = (0, 0, 0), screen_width: int = 800, screen_height: int = 600):
        super().__init__(size, x, y, vx, vy, color, screen_width, screen_height)

    def updates(self, paddle=None, wood_paddle=None):
        super().updates()
        if paddle is not None:
            self.on_hit_paddle(paddle)
        if wood_paddle is not None:
            self.on_hit_wood_paddle(wood_paddle)

    def on_hit_screen_edge(self):
        if self.x - self.size < 0 or self.x + self.size > self.screen_width:
            self.vx = -self.vx
            self.sound.run_sound('paddle')
        if self.y - self.size < 0 or self.y + self.size > self.screen_height:
            self.vy = -self.vy
            self.sound.run_sound('paddle')

    def on_hit_paddle(self, paddle):
        if (paddle.x - self.size <= self.x <= paddle.x + paddle.width + self.size and
                paddle.y - self.size <= self.y <= paddle.y + paddle.height + self.size):

            # Detect which side of the paddle the ball hit
            if paddle.y - self.size <= self.y <= paddle.y:  # Top side
                self.vy = -abs(self.vy)  # Ensure upward bounce
                self.y = paddle.y - self.size  # Reposition above the paddle
                print("+1 (top)")
            elif paddle.y + paddle.height <= self.y <= paddle.y + paddle.height + self.size:  # Bottom side
                self.vy = abs(self.vy)  # Ensure downward bounce
                self.y = paddle.y + paddle.height + self.size  # Reposition below the paddle
                print("+1 (bottom)")
            elif paddle.x - self.size <= self.x <= paddle.x:  # Left side
                self.vx = -abs(self.vx)  # Ensure leftward bounce
                self.x = paddle.x - self.size  # Reposition to the left
                print("+1 (left)")
            elif paddle.x + paddle.width <= self.x <= paddle.x + paddle.width + self.size:  # Right side
                self.vx = abs(self.vx)  # Ensure rightward bounce
                self.x = paddle.x + paddle.width + self.size  # Reposition to the right
                print("+1 (right)")

    def on_hit_wood_paddle(self, paddle) -> bool:
        # All sides of paddle ><
        if (paddle.x - self.size <= self.x <= paddle.x + paddle.width + self.size and
                paddle.y - self.size <= self.y <= paddle.y + paddle.height + self.size):

            # Detect which side of the paddle the ball hit
            if paddle.y - self.size <= self.y <= paddle.y:  # Top side
                self.vy = -abs(self.vy)  # Ensure upward bounce
                self.y = paddle.y - self.size  # Reposition above the paddle
                print("+1 (top)")
            elif paddle.y + paddle.height <= self.y <= paddle.y + paddle.height + self.size:  # Bottom side
                self.vy = abs(self.vy)  # Ensure downward bounce
                self.y = paddle.y + paddle.height + self.size  # Reposition below the paddle
                print("+1 (bottom)")
            elif paddle.x - self.size <= self.x <= paddle.x:  # Left side
                self.vx = -abs(self.vx)  # Ensure leftward bounce
                self.x = paddle.x - self.size  # Reposition to the left
                print("+1 (left)")
            elif paddle.x + paddle.width <= self.x <= paddle.x + paddle.width + self.size:  # Right side
                self.vx = abs(self.vx)  # Ensure rightward bounce
                self.x = paddle.x + paddle.width + self.size  # Reposition to the right
                print("+1 (right)")
            return True
        return False

    def __str__(self):
        return 'ball'