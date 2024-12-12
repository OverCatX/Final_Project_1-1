import time

import pygame


class Sound:
    def __init__(self):
        self.hit_wall_sound = pygame.mixer.Sound('sounds/hit_wall_sound.wav')
        self.hit_paddle_sound = pygame.mixer.Sound('sounds/hit_paddle_sound.wav')
        self.background_sound = pygame.mixer.Sound('sounds/background_music.wav')

    def run_background_sound(self):
        self.background_sound.play(-1)
        self.background_sound.set_volume(5)

    def run_sound(self, sound):
        if sound == 'wall':
            self.hit_wall_sound.play()
        elif sound == 'paddle':
            self.hit_paddle_sound.play()

    def stop_wall_sound(self):
        self.hit_wall_sound.stop()