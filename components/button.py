import pygame


class Button:
    def __init__(self, x, y, width, height, text, text_color, button_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.button_color = button_color
        self.font = pygame.font.Font(None, 36)

    def draw(self, display):
        pygame.draw.rect(display, self.button_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        display.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
