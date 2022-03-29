import pygame
from button import Button
from settings import *

class Start_Screen:
    def __init__(self, width : int, height : int):
        self.visible = True
        self.start_button = Button('PLAY', (width//2, height//2 + 20), COLORS.ACCENT, 10, 10, is_centered = True)
        self.rules_button = Button('HOW TO PLAY', (width//2, height//2 +100), COLORS.ACCENT, 10, 10, is_centered=True)
        self.buttons = [self.start_button, self.rules_button]

    def activation_only(func):
        def wrapper(self, *args, **kwargs):
            if not self.visible:
                return
            func(self, *args, **kwargs)
        return wrapper

    @activation_only
    def render(self, win : pygame.Surface):
        for button in self.buttons:
            button.render(win)
    
    # @activation_only
    def handle(self, event : pygame.event.Event, win : pygame.Surface) -> bool:
        if self.start_button.click(event):
            self.visible = False
            # win.fill(COLORS.BACKGROUND)
            return True
 