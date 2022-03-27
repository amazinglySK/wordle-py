from settings import *
import pygame

class Notification:
    def __init__(self, message : str):
        self.x = 0
        self.y = 0
        self.msg = message
        self.txt_surface = FONT.render(self.msg, True, COLORS.MISMATCH)
        self.rect = pygame.Rect(self.x, self.y, self.txt_surface.get_width(), self.txt_surface.get_height())

    def show(self, win : pygame.Surface):
        win.blit(self.txt_surface, (self.x, self.y))
        
    def delete(self):
        del self