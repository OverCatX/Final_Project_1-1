import pygame

class Paddle:
    def __init__(self, width: int, height: int, x: int, y:int,color: str, speed:int):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed

    def draw(self, display):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))

    def __str__(self):
        return "paddle"