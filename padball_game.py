import pygame

class PadBallGame:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("PadBallGame V.1")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font_large = pygame.font.Font(None, 74)
        self.state = "home"