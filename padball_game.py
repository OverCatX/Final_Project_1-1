import random
import sys

import pygame
from db.player_db import PlayerDB
from components.button import Button
from obj.ball import Ball
from obj.paddle import Paddle
from sounds.sound import Sound


class PadBallGame:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen_width = 600
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("PadBallGame V.1")
        self.clock = pygame.time.Clock()

        """ Background Music No cc."""
        self.sound = Sound()
        self.sound.run_background_sound()
        """"""

        self.running = True
        self.state = "home"
        self.username = ''
        self.player = None

        self.floating_balls = [Ball(random.randint(10, 30), x = random.randint(50, 550)
                             , y = random.randint(50, 750), vx = random.choice([-2, 2]), vy = random.choice([-2, 2])
                             , color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                             , screen_width=self.screen_width, screen_height = self.screen_height)
                               for i in range(1)]
        self.paddle = Paddle(100,30,(self.screen_width - 100 )//2, self.screen_height - 40,(255,255,255), 5)

        self.fonts = {
            "Large": pygame.font.Font(None, 74),
            "Medium": pygame.font.Font(None, 36),
            "Small": pygame.font.Font(None, 26)
        }

        self.buttons = {
            "start": Button(200, 300, 200, 60, "Start Game", (255, 255, 255), (0, 200, 0)),
            "settings": Button(300, 400, 200, 60, "Settings", (255, 255, 255), (100, 100, 100)),
            "leaderboard":  Button(200, 400, 200, 60, "Leaderboard", (255, 255, 255), (0, 0, 200)),
            "report": Button(200, 500, 200, 60, "Report", (255, 255, 255), (200, 128, 0)),
            "exit": Button(200, 600, 200, 60, "Exit", (255, 255, 255), (200, 0, 0)),
            "back": Button(300, 500, 200, 60, "Back", (255, 255, 255), (100, 100, 100)),
            "login_button": Button(200, 600, 200, 60, "Enter Game", (255, 255, 255), (0, 200, 0))
        }

        self.color_codes = {
            'white': (255, 255, 255),
            'black': (0, 0, 0),
            'gray' : (128,128,128)
        }

    def authorization_screen(self):
        while self.state == 'authorization':
            """Set White Background Screen"""
            self.screen.fill(self.color_codes['white'])
            """"""

            title_text = self.fonts['Large'].render("Enter Your Username", True, self.color_codes['black'])
            subtitle_text = self.fonts['Small'].render("The length of the name must not exceed 10 characters.", True, self.color_codes['gray'])
            self.screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 100))
            self.screen.blit(subtitle_text, (self.screen_width // 2 - subtitle_text.get_width() // 2, 200))

            """ Display the username being typed """
            username_surface = self.fonts['Medium'].render(self.username, True, (255, 255, 255))
            pygame.draw.rect(self.screen, (50, 50, 50), (100, 350, 400, 50))
            self.screen.blit(username_surface, (110, 360))
            """"""

            self.buttons['login_button'].draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.username = self.username[:-1]
                    elif event.key == pygame.K_RETURN and self.username.strip():
                        self.state = "home"
                    elif len(self.username) < 10:
                        self.username += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    """ Enter Game button """
                    if self.buttons['login_button'].is_clicked(mouse_pos) and self.username.strip():
                        player_db = PlayerDB()
                        self.player = player_db.player_login(self.username)
                        self.state = "lobby"
                    """"""

            pygame.display.flip()
            self.clock.tick(60)

    def home_screen(self):
        while self.state == 'home':
            """ Set White Background Screen """
            self.screen.fill(self.color_codes['white'])
            """"""

            """ Floating ball """
            for balls in self.floating_balls:
                balls.updates()
                balls.draw(self.screen)
            """"""

            title_text = self.fonts['Medium'].render("Welcome to PadBallGame V.1", True, (0, 0, 0))
            self.screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 100))
            self.buttons['start'].draw(self.screen)
            self.buttons['leaderboard'].draw(self.screen)
            self.buttons['report'].draw(self.screen)
            self.buttons['exit'].draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.buttons['start'].is_clicked(mouse_pos):
                        self.state = "authorization"
                    elif self.buttons['leaderboard'].is_clicked(mouse_pos):
                        print("Leaderboard clicked!")
                    elif self.buttons['report'].is_clicked(mouse_pos):
                        self.state = "home"
                    elif self.buttons['exit'].is_clicked(mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
            self.clock.tick(60)

    def lobby_screen(self):
        while self.state == 'lobby':
            """ Set White Background Screen """
            self.screen.fill(self.color_codes['white'])
            """"""

            """ Floating ball """
            for balls in self.floating_balls:
                balls.updates()
                balls.draw(self.screen)
            """"""

            title_text = self.fonts['Medium'].render(f"Welcome's {self.player.username}", True, (0, 0, 0))
            self.screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 100))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    # if self.buttons['start'].is_clicked(mouse_pos):
                    #     self.state = "authorization"
                    # elif self.buttons['leaderboard'].is_clicked(mouse_pos):
                    #     print("Leaderboard clicked!")
                    # elif self.buttons['report'].is_clicked(mouse_pos):
                    #     self.state = "home"
                    # elif self.buttons['exit'].is_clicked(mouse_pos):
                    #     pygame.quit()
                    #     sys.exit()

            pygame.display.flip()
            self.clock.tick(60)
    
    def on_game(self):
        while self.state == 'on_game':
            """ Set White Background Screen """
            self.screen.fill(self.color_codes['white'])
            """"""

            title_text = self.fonts['Medium'].render(f"Welcome's {self.player.username}", True, (0, 0, 0))
            self.screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 100))

            """ Paddle Movement Control"""
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.paddle.x > 0:
                self.paddle.x -= self.paddle.speed
            if keys[pygame.K_RIGHT] and self.paddle.x < self.screen_height - self.screen_width:
                self.paddle.x += self.paddle.speed
            """"""

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

            pygame.display.flip()
            self.clock.tick(60)

    def run(self):
        while self.running:
            if self.state == 'authorization':
                self.authorization_screen()
            elif self.state == 'home':
                self.home_screen()
            elif self.state == 'lobby':
                self.lobby_screen()
        pygame.quit()
        sys.exit()

padball = PadBallGame()
padball.run()