import random

from ball import Ball

class FloatingBall(Ball):
    def __init__(self, size: int = random.randint(10, 30), x: int = random.randint(50, 550)
                 , y: int = random.randint(50, 750), vx: float = random.choice([-2, 2])
                 , vy: float = random.choice([-2, 2])
                 , color: tuple[int, int, int] = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                 , count: int = 10):
        super().__init__(size, x, y, vx, vy, color, count)

    def __str__(self):
        return 'floating_ball'

