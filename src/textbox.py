import pygame
from settings import *

class Text:
    def __init__(self, text : str, pos : tuple, color : tuple):

        self.text = text
        self.visible = True
        self.color = color
        self.text_surface = FONT.render(self.text, True, self.color)
        self.width = self.text_surface.get_width() 
        self.height = self.text_surface.get_height() 
        self.pos = (pos[0] - self.text_surface.get_width()//2, pos[1] - self.text_surface.get_height()//2)

    def render(self, win : pygame.Surface):
        if not self.visible:
            return
        win.blit(self.text_surface, self.pos)