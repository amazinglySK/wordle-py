import pygame
from settings import *

class Text:
    def __init__(self, text : str, pos : tuple, color : tuple, is_centered : bool = True, font = FONT):

        self.text = text
        self.font = font
        self.visible = True
        self.color = color
        self.is_centered = is_centered
        self.text_surface = font.render(self.text, True, self.color)
        self.width = self.text_surface.get_width() 
        self.height = self.text_surface.get_height() 
        self.raw_pos = pos
        self.pos = (pos[0] - self.text_surface.get_width()//2, pos[1] - self.text_surface.get_height()//2) if is_centered else pos

    def render(self, win : pygame.Surface):
        if not self.visible:
            return
        win.blit(self.text_surface, self.pos)

    def change_text(self, new_text : str):
        self.text = new_text
        self.text_surface = self.font.render(new_text, True, self.color)
        self.recalc_pos()
        print('Changed text')

    def recalc_pos(self):
        self.pos = (self.raw_pos[0] - self.text_surface.get_width()//2, self.raw_pos[1] - self.text_surface.get_height()//2) if self.is_centered else self.pos