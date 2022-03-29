import pygame
from button import Button
from textbox import Text
from settings import *

class Game_Over:
    def __init__(self, width : int, height : int):
        self.visible = False
        self.status_text = Text('', (width//2, height//2 - 60), COLORS.ACCENT)
        self.continue_btn = Button('CONTINUE', (width//2, height//2 + 20), COLORS.ACCENT, 10, 10, is_centered = True)
        self.exit_btn = Button('EXIT', (width//2, height//2 +100), COLORS.ACCENT, 10, 10, is_centered=True)
        self.buttons = [self.continue_btn, self.exit_btn]

    def render(self, status, win : pygame.Surface):
        if not self.visible:
            return
        if self.status_text.text != status : 
            print(status)
            self.status_text.change_text(status)
        self.status_text.render(win)
        for button in self.buttons:
            button.render(win)

    def handle(self, event : pygame.event.Event):
        if not self.visible: return
        if self.continue_btn.click(event):
            self.visible = False
            return "Continue"
        elif self.exit_btn.click(event):
            self.visible = False
            return "Exit"