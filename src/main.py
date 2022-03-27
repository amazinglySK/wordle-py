import time
import pygame
from pygame import Surface, mixer
from board import Board
from settings import *
from start import Start_Screen
from textbox import Text
from keypad import Keypad

def music_init():
    mixer.init()
    mixer.music.load("assets/musik.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play(-1, 26.0)


def screen_initialize() -> Surface:
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("WORDLE")
    gameicon = pygame.image.load("assets/wordle.png")
    pygame.display.set_icon(gameicon)
    return window

def main():
    pygame.font.init()
    WIN = screen_initialize()

    game_board = Board(6, 5, COLORS.DEFAULT)
    game_board.create((300, HEIGHT//2), 80, 80, 20, marginy=10)

    keypad = Keypad((800, HEIGHT//2), COLORS.DEFAULT)
    keypad.create(60, 60, 10)

    start_screen = Start_Screen(WIDTH, HEIGHT - 50)

    WIN.fill(COLORS.BACKGROUND)

    title = Text('WORDLE', (WIDTH//2, 40), COLORS.ACCENT)

    clock = pygame.time.Clock()
    running = True

    music_init()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            start = start_screen.handle(event, WIN)
            if start:
                game_board.visible = True
                keypad.visible = True
            status = game_board.handleEvents(event, keypad)
            count = 1 if status != None else 0
            if status == True:
                print("You won")
            elif status == False:
                print("Game Over")

        start_screen.render(WIN)
        title.render(WIN)
        game_board.render(WIN)
        keypad.render(WIN)
        pygame.display.flip()

        if count == 1:
            time.sleep(1)
            count = 0
            game_board.restart()
            keypad.reset()
            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()