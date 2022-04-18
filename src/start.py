import pygame
from button import Button
from settings import *

class Start_Screen:
    def __init__(self, width : int, height : int):
        self.visible = True
        self.start_button = Button('PLAY', (width//2, height//2 + 20), COLORS.ACCENT, 10, 10, is_centered = True)
        self.rules_button = Button('HOW TO PLAY', (width//2, height//2 +100), COLORS.ACCENT, 10, 10, is_centered=True)
        self.buttons = [self.start_button, self.rules_button]

    def render(self, win : pygame.Surface):
        if not self.visible : return
        for button in self.buttons:
            button.render(win)
    
    def handle(self, event : pygame.event.Event) -> bool:
        if self.start_button.click(event):
            self.visible = False
            return "Start"
 