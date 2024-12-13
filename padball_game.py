import random
import sys

import pygame
from db.player_db import PlayerDB
from components.button import Button
from obj.ball import Ball, FloatingObject
from obj.mystery_box import MysteryBlock
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
        self.game_data = {
            'username': '',
            'state': 'home',
            'scores': 0,
            'mystery_box_active': False,
            'mystery_box_timer': 0,
            'mystery_box_appear_time': 0,
            'time_start': 3,
            'screen_color': (255, 255, 255),
            'event_status': False,
            'event_id': '', #001 = x2 score (10secs), #002 = slowed ball (10 secs), #003 = expanded wood paddle(5 secs), #004 = save ball(5 sec), #005 x3 score(10 sec)
            'event_startTime': 0,
            'event_duration': 0,
            'event_random_select': '',
            'event_multiply_score': 1
        }
        self.events = {
            '#001': {
                'title': 'x2 Score',
                'duration': 10
            },
            '#002': {
                'title': 'Slowed Ball',
                'duration': 10
            },
            '#003': {
                'title': 'Big paddle',
                'duration': 5
            },
            '#004': {
                'title': 'Save Ball',
                'duration': 5
            },
            '#005': {
                'title': 'x3 Score',
                'duration': 6
            }
        }
        self.player = None

        self.floating_balls = [FloatingObject(random.randint(10, 30), x = random.randint(50, 550)
                             , y = random.randint(50, 750), vx = random.choice([-2, 2]), vy = random.choice([-2, 2])
                             , color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                             , screen_width=self.screen_width, screen_height = self.screen_height)
                               for i in range(10)]
        self.ball_game = Ball(20, x=self.screen_width //2,y=self.screen_height//2, vx=10
                               , vy=10, color=(0,0,0)
                               ,screen_width=self.screen_width, screen_height=self.screen_height)
        self.mystery_box = MysteryBlock(50,50, 0, 0, (255,195,0))

        self.paddle = Paddle(150,30,(self.screen_width - 100 )//2, self.screen_height - 120,(0,0,255), speed=25)
        self.wood_paddle = Paddle(200,25,(self.screen_width - 200)//2, 0,(0,0,0), speed=0)

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
            'gray' : (128,128,128),
            'lavender': (230, 230, 250),
            'thistle': (216, 191, 216)
        }

    def authorization_screen(self):
        while self.game_data['state'] == 'authorization':
            """Set White Background Screen"""
            self.screen.fill(self.color_codes['white'])
            """"""

            title_text = self.fonts['Large'].render("Enter Your Username", True, self.color_codes['black'])
            subtitle_text = self.fonts['Small'].render("The length of the name must not exceed 10 characters.", True, self.color_codes['gray'])
            self.screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 100))
            self.screen.blit(subtitle_text, (self.screen_width // 2 - subtitle_text.get_width() // 2, 200))

            """ Display the username being typed """
            username_surface = self.fonts['Medium'].render(self.game_data['username'], True, (255, 255, 255))
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
                        self.game_data['username'] = self.game_data['username'][:-1]
                    elif event.key == pygame.K_RETURN and self.game_data['username'].strip():
                        self.game_data['state'] = "home"
                    elif len(self.game_data['username']) < 10:
                        self.game_data['username'] += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    """ Enter Game button """
                    if self.buttons['login_button'].is_clicked(mouse_pos) and self.game_data['username'].strip():
                        player_db = PlayerDB()
                        self.player = player_db.player_login(self.game_data['username'])
                        self.game_data['state'] = "lobby"
                    """"""

            pygame.display.flip()
            self.clock.tick(60)

    def home_screen(self):
        while self.game_data['state'] == 'home':
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
                        self.game_data['state'] = "authorization"
                    elif self.buttons['leaderboard'].is_clicked(mouse_pos):
                        print("Leaderboard clicked!")
                    elif self.buttons['report'].is_clicked(mouse_pos):
                        self.game_data['state'] = "home"
                    elif self.buttons['exit'].is_clicked(mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
            self.clock.tick(60)

    def lobby_screen(self):
        while self.game_data['state'] == 'lobby':
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
        while self.game_data['state'] == 'lobby':
            """ Set White Background Screen """
            self.screen.fill(self.game_data['screen_color'])
            """"""
            
            score_text = self.fonts['Medium'].render(f"Score {self.game_data['scores']}", True, (0, 0, 0))
            best_score_text = self.fonts['Small'].render(f"BestScore {self.player.highscore}", True, (255, 0, 0))
            self.screen.blit(score_text, (self.screen_width // 2 - score_text.get_width() // 2, 100))
            self.screen.blit(best_score_text, (self.screen_width // 2 - best_score_text.get_width() // 2, 130))

            """ Mystery Box """
            if self.game_data['scores'] >= 1:
                # If hit mystery_box
                if self.ball_game.on_hit_mystery_box(self.mystery_box, self.game_data['mystery_box_active']):
                    self.game_data['mystery_box_active'] = False
                    self.game_data['event_status'] = True
                    self.game_data['event_startTime'] = pygame.time.get_ticks() // 1000
                    print('event started')

                # Box not active
                if not self.game_data['mystery_box_active']:
                    current_time = pygame.time.get_ticks() // 1000
                    if current_time - self.game_data['mystery_box_appear_time'] >= self.game_data['mystery_box_timer']:
                        self.game_data['mystery_box_timer'] = random.randint(15,30)
                        self.mystery_box.x = random.randint(50, self.screen_width - 50)
                        self.mystery_box.y = random.randint(100, self.screen_height - 200)
                        self.game_data['mystery_box_active'] = True
                        self.game_data['mystery_box_appear_time'] = current_time
                        event_id_lists = [event_ids for event_ids in self.events.keys()]
                        self.game_data['event_random_select'] = event_id_lists[random.randint(0, len(event_id_lists) - 1)]
                else:
                    self.mystery_box.draw(self.screen)
                """"""

                """ Events-Bonus """
                if self.game_data['event_status']:
                    self.game_data['screen_color'] = self.color_codes['thistle']

                    # Set event
                    self.game_data['event_id'] = '#003'
                    # print(self.game_data['event_id'])
                    self.game_data['event_duration'] = self.events[self.game_data['event_id']]['duration']

                    if self.game_data['event_id'] == '#001':
                        self.game_data['event_multiply_score'] = 2
                    elif self.game_data['event_id'] == '#002':
                        pass
                    elif self.game_data['event_id'] == '#003':
                        self.wood_paddle.width = self.screen_width
                    elif self.game_data['event_id'] == '#004':
                        pass
                    elif self.game_data['event_id'] == '#005':
                        self.game_data['event_multiply_score'] = 3

                    # Text Event Bonus ><
                    event_title = self.fonts['Small'].render(f"Bonus: {self.events[self.game_data['event_id']]['title']}"
                                                             , True,(255, 128, 0))
                    self.screen.blit(event_title, (self.screen_width // 2 - event_title.get_width() // 2, 180))

                    # End Event
                    current_time = pygame.time.get_ticks() // 1000
                    if current_time - self.game_data['event_startTime'] >= self.game_data['event_duration']:
                        self.game_data['event_status'] = False  # End event ><
                        self.game_data['screen_color'] = self.color_codes['lavender']

                        # Back to Original value
                        self.game_data['event_multiply_score'] = 1
                        self.wood_paddle.width = 200
                """"""

            """ Draw Wood Paddle """
            self.wood_paddle.draw(self.screen)
            """"""

            """ Draw Paddle """
            self.paddle.draw(self.screen)
            """"""

            """ Draw ball """
            self.ball_game.updates(self.paddle, self.wood_paddle, self.mystery_box, self.game_data['mystery_box_active'])
            self.ball_game.draw(self.screen)
            """"""

            """ Updates score when ball hit wood_paddle"""
            if self.ball_game.on_hit_wood_paddle(self.wood_paddle):
                if self.game_data['scores'] >= int(self.player.highscore):
                    self.game_data['scores'] += (1 * self.game_data['event_multiply_score'])
                    self.player.updates_best_score(self.game_data['scores'])
                else:
                    self.game_data['scores'] += (1 * self.game_data['event_multiply_score'])
            """"""

            """ On prime score """
            if self.game_data['scores'] == 5:
                self.game_data['screen_color'] = self.color_codes['lavender']
            """"""

            """ Paddle Movement Control """
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.paddle.x > 0:
                self.paddle.x -= self.paddle.speed
            if keys[pygame.K_RIGHT] and self.paddle.x < self.screen_width - self.paddle.width:
                self.paddle.x += self.paddle.speed
            """"""

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(60)

    def run(self):
        while self.running:
            if self.game_data['state'] == 'authorization':
                self.authorization_screen()
            elif self.game_data['state'] == 'home':
                self.home_screen()
            elif self.game_data['state'] == 'lobby':
                self.on_game()
            elif self.game_data['state'] == 'on_game':
                self.on_game()
        pygame.quit()
        sys.exit()

padball = PadBallGame()
padball.run()