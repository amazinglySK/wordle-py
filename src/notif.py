from button import Button
from settings import *
import pygame

class Notification_Box:
    def __init__(self, message : str):
        self.x = 800
        self.y = 600
        self.msg = message
        self.visible = False
        self.box = Button(self.msg, (self.x, self.y), COLORS.INCORRECT, COLORS.DEFAULT,padding=10, is_centered=True, text_is_centered=True, font = NORMAL_FONT)

    def render(self, win : pygame.Surface):
        if not self.visible:
            return
        self.box.render(win)

    def update_msg(self, message, win):
        self.msg = message
        win.fill(COLORS.BACKGROUND)
        self.box = Button(self.msg, (self.x, self.y), COLORS.INCORRECT, COLORS.DEFAULT,padding=10, is_centered=True, text_is_centered=True, font = NORMAL_FONT)
        