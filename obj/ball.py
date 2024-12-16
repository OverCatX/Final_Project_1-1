from obj.floating_object import FloatingObject

class Ball(FloatingObject):
    def __init__(self, size: int = 20, x: int = 0, y: int = 0, vx: float = 0, vy: float = 0
                 , color: tuple[int, int, int] = (0, 0, 0), screen_width: int = 800, screen_height: int = 600):
        super().__init__(size, x, y, vx, vy, color, screen_width, screen_height)

    def updates(self, paddle=None, wood_paddle=None, mystery_box=None, box_active=False
                , save_ball_paddle=None, save_ball_active=False, other_ball=None):
        super().updates()
        if paddle is not None:
            self.on_hit_paddle(paddle)
        if wood_paddle is not None:
            self.on_hit_wood_paddle(wood_paddle)
        if mystery_box is not None:
            self.on_hit_mystery_box(mystery_box, box_active)
        if save_ball_paddle is not None:
            self.on_hit_save_paddle(save_ball_paddle, save_ball_active)
        if other_ball is not None:
            self.on_hit_balls(other_ball)

    def on_hit_screen_edge(self):
        if self.x - self.size < 0 or self.x + self.size > self.screen_width:
            self.vx = -self.vx
            self.sound.run_sound('paddle')
        if self.y - self.size < 0:
            self.vy = -self.vy
            # print(self.y)
            self.sound.run_sound('paddle')

    def on_hit_paddle(self, paddle):
        if (paddle.x - self.size <= self.x <= paddle.x + paddle.width + self.size and
                paddle.y - self.size <= self.y <= paddle.y + paddle.height + self.size):
            # Detect which side of the paddle the ball hit
            if paddle.y - self.size <= self.y <= paddle.y:
                self.vy = -abs(self.vy)
                self.y = paddle.y - self.size
                print("+1 (top)")
            elif paddle.y + paddle.height <= self.y <= paddle.y + paddle.height + self.size:  # Bottom
                self.vy = abs(self.vy)
                self.y = paddle.y + paddle.height + self.size
                print("+1 (bottom)")
            elif paddle.x - self.size <= self.x <= paddle.x:  # Left
                self.vx = -abs(self.vx)
                self.x = paddle.x - self.size
                print("+1 (left)")
            elif paddle.x + paddle.width <= self.x <= paddle.x + paddle.width + self.size:  # Right side
                self.vx = abs(self.vx)
                self.x = paddle.x + paddle.width + self.size
                print("+1 (right)")

    def on_hit_wood_paddle(self, paddle) -> bool:
        # All sides of paddle ><
        if (paddle.x - self.size <= self.x <= paddle.x + paddle.width + self.size and
                paddle.y - self.size <= self.y <= paddle.y + paddle.height + self.size):
            if paddle.y - self.size <= self.y <= paddle.y:
                self.vy = -abs(self.vy)
                self.y = paddle.y - self.size
                print("+1 (top)")
            elif paddle.y + paddle.height <= self.y <= paddle.y + paddle.height + self.size:  # Bottom
                self.vy = abs(self.vy)
                self.y = paddle.y + paddle.height + self.size
                print("+1 (bottom)")
            elif paddle.x - self.size <= self.x <= paddle.x:  # Left
                self.vx = -abs(self.vx)
                self.x = paddle.x - self.size
                print("+1 (left)")
            elif paddle.x + paddle.width <= self.x <= paddle.x + paddle.width + self.size:
                self.vx = abs(self.vx)
                self.x = paddle.x + paddle.width + self.size
                print("+1 (right)")
            return True
        return False

    def on_hit_save_paddle(self, paddle, save_ball_active) -> bool:
        if (save_ball_active and paddle.x - self.size <= self.x <= paddle.x + paddle.width + self.size and
                paddle.y - self.size <= self.y <= paddle.y + paddle.height + self.size):
            if paddle.y - self.size <= self.y <= paddle.y:
                self.vy = -abs(self.vy)
                self.y = paddle.y - self.size
            elif paddle.y + paddle.height <= self.y <= paddle.y + paddle.height + self.size:  # Bottom
                self.vy = abs(self.vy)
                self.y = paddle.y + paddle.height + self.size
            elif paddle.x - self.size <= self.x <= paddle.x:  # Left
                self.vx = -abs(self.vx)
                self.x = paddle.x - self.size
            elif paddle.x + paddle.width <= self.x <= paddle.x + paddle.width + self.size:
                self.vx = abs(self.vx)
                self.x = paddle.x + paddle.width + self.size
            return True
        return False

    def on_hit_balls(self, balls: list) -> bool:
        collision_detected = False  # To track if a collision happens with any ball

        for ball in balls:
            # Avoid checking collision with itself
            if ball is self:
                continue

            # Check if there's a collision with another ball
            if (ball.x - self.size <= self.x <= ball.x + ball.size + self.size and
                    ball.y - self.size <= self.y <= ball.y + ball.size + self.size):

                # Handle collision based on the side of impact
                if ball.y - self.size <= self.y <= ball.y:  # Top
                    self.vy = -abs(self.vy)
                    self.y = ball.y - self.size
                elif ball.y + ball.size <= self.y <= ball.y + ball.size + self.size:  # Bottom
                    self.vy = abs(self.vy)
                    self.y = ball.y + ball.size + self.size
                elif ball.x - self.size <= self.x <= ball.x:  # Left
                    self.vx = -abs(self.vx)
                    self.x = ball.x - self.size
                elif ball.x + ball.size <= self.x <= ball.x + ball.size + self.size:  # Right
                    self.vx = abs(self.vx)
                    self.x = ball.x + ball.size + self.size

                collision_detected = True  # Mark collision as true

        return collision_detected

    def on_hit_mystery_box(self, box, box_active) -> bool:
        if box_active and box.x <= self.x <= box.x + box.width and box.y <= self.y <= box.y + box.width:
            print("Got box!")
            return True
        return False

    def __str__(self):
        return 'ball'