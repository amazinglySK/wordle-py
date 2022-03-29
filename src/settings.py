import pygame

pygame.init()
FONT = pygame.font.Font('assets/game_font.ttf', 40)
NORMAL_FONT = pygame.font.SysFont(None, 30)
HEIGHT = 700
WIDTH= 1080
FPS= 60

class COLORS:
    INCORRECT = (70, 73, 76)
    DEFAULT = (229, 236, 244)
    SELECT = (218, 204, 62)
    MISMATCH = (203, 121, 58)
    CORRECT = (161, 232, 135)
    BACKGROUND = (230, 95, 92)
    ACCENT = (255, 255, 255)