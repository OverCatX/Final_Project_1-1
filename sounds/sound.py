import pygame


class Sound:
    def __init__(self):
        self.hit_wall_sound = pygame.mixer.Sound('hit_wall_sound.wav')
        self.hit_paddle_sound = pygame.mixer.Sound('hit_paddle_sound.wav')
        self.background_sound = pygame.mixer.Sound('background_music.wav')

    def run_background_sound(self):
        self.background_sound.play(-1)

    def run_sound(self, sound):
        if sound == 'wall':
            self.hit_wall_sound.play(maxtime=10)
        elif sound == 'paddle':
            self.hit_paddle_sound.play(maxtime=10)