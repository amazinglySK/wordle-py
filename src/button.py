from turtle import color
import pygame
from textbox import Text
from settings import *


class Button:
    def __init__(self, txt : str, pos : tuple, txt_color : tuple, bg_color : tuple, padding : int = 0, is_centered = False):
        self.bg = bg_color
        self.visible = True
        self.text = Text(txt, pos, txt_color)
        self.x, self.y = pos if not is_centered else (pos[0] - self.text.width//2 - padding, pos[1] - self.text.height//2 - padding)
        self.rect = pygame.Rect(self.x, self.y, self.text.width + padding*2, self.text.height + padding*2)

    def render(self, win : pygame.Surface):
        if not self.visible:
            return
        pygame.draw.rect(win, self.bg, self.rect, border_radius=5)
        # x_offset = self.text.get_width()//2
        # y_offset = self.text.get_height()//2
        self.text.render(win)

    def click(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.rect.collidepoint(event.pos)