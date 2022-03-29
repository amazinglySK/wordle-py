import time
import pygame
from pygame import Surface, mixer
from board import Board
from settings import *
from start import Start_Screen
from textbox import Text
from keypad import Keypad
from notif import Notification_Box
from gameover import Game_Over

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
    game_over = Game_Over(WIDTH, HEIGHT - 50)

    # WIN.fill(COLORS.BACKGROUND)

    title = Text('WORDLE', (WIDTH//2, 40), COLORS.ACCENT)

    notif = Notification_Box("Game Started")

    clock = pygame.time.Clock()
    played = False
    running = True
    game_status = ''
    count = 0

    WIN.fill(COLORS.BACKGROUND)

    # music_init()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            start = start_screen.handle(event, WIN)
            if start:
                if played:
                    game_board.restart()
                    keypad.reset()
                    notif.update_msg('Game started', WIN)
                    played = False
                start_screen.visible = False
                game_board.visible = True
                keypad.visible = True
                notif.visible = True
            choice = game_over.handle(event)
            if choice == "Continue":
                keypad.visible = True
                game_board.visible = True
                notif.visible = True
                keypad.reset()
                game_board.restart()
                notif.update_msg('Game started', WIN)
                # WIN.fill(COLORS.BACKGROUND)
            elif choice == "Exit":
                played = True
                start_screen.visible=True

            status = game_board.handleEvents(event, keypad, notif, WIN)
            if status != None: count = 1
            if status == True:
                game_status = "You won !!"
                notif.update_msg('Whoa Nelly !', WIN)
            elif status == False:
                game_status = "Better luck next time"
                notif.update_msg('Awww....', WIN)

        WIN.fill(COLORS.BACKGROUND)
        notif.render(WIN)
        start_screen.render(WIN)
        title.render(WIN)
        game_board.render(WIN)
        keypad.render(WIN)
        game_over.render(game_status, WIN)
        pygame.display.flip()
        if count == 1:
            count = 0
            keypad.visible = False
            game_board.visible = False
            notif.visible = False
            game_over.visible = True
            time.sleep(0.5)


    pygame.quit()


if __name__ == "__main__":
    main()