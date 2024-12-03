import random
import sys

import pygame
from obj.ball import Ball
from components.button import Button


class PadBallGame:

    def __init__(self):
        pygame.init()
        self.screen_width = 600
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("PadBallGame V.1")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font_large = pygame.font.Font(None, 74)
        self.font_medium = pygame.font.Font(None, 36)
        self.state = "authorization"
        self.username = ''

        self.ball = Ball(20, x=self.screen_width // 2, y=self.screen_height // 2
                         , vx=5, vy=4, color=(0, 255, 0), count=1, id=random.randint(1000, 2000)
                         , screen_width=self.screen_width, screen_height=self.screen_height)

        self.buttons = {
            "start": Button(300, 300, 200, 60, "Start Game", (255, 255, 255), (0, 200, 0)),
            "settings": Button(300, 400, 200, 60, "Settings", (255, 255, 255), (100, 100, 100)),
            "exit": Button(300, 500, 200, 60, "Exit", (255, 255, 255), (200, 0, 0)),
            "back": Button(300, 500, 200, 60, "Back", (255, 255, 255), (100, 100, 100)),
            "Login_button": Button(200, 600, 200, 60, "Enter Game", (255, 255, 255), (0, 200, 0))
        }

        self.color_codes = {
            'white': (255, 255, 255),
            'black': (0, 0, 0)
        }

    def authorization_screen(self):
        while self.state == 'authorization':
            """Set White Background Screen"""
            self.screen.fill(self.color_codes['white'])
            title_text = self.font_large.render("Enter Your Username", True, self.color_codes['black'])
            self.screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 100))
            """"""

            """Display the username being typed"""
            username_surface = self.font_medium.render(self.username, True, (255, 255, 255))
            pygame.draw.rect(self.screen, (50, 50, 50), (100, 350, 400, 50))
            self.screen.blit(username_surface, (110, 360))
            """"""

            self.buttons['Login_button'].draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.username = self.username[:-1]
                    elif event.key == pygame.K_RETURN and self.username.strip():
                        self.state = "home"
                    elif len(self.username) < 20:
                        self.username += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.buttons['Login_button'].is_clicked(mouse_pos) and self.username.strip():
                        self.state = "home"

            pygame.display.flip()
            self.clock.tick(60)

    def home_screen(self):
        pass

    def run(self):
        while self.running:
            if self.state == 'authorization':
                self.authorization_screen()
            elif self.state == 'home':
                self.home_screen()
        pygame.quit()
        sys.exit()
