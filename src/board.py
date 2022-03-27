from types import NoneType
from tile import Tile, Tile_Group
from settings import *
from word import choose_word

class Board:
    def __init__(self,rows : int, cols : int, color : tuple):
        self.x = 0
        self.y = 0
        self.visible = False
        self.word = ''
        self.rows = rows
        self.cols = cols
        self.color = color
        self.board_width = 0
        self.board_height = 0
        self.tiles = []
        self.tile_groups = []
        self.tile_groups_remaining = []

    def create(self, center : tuple, height : int, width : int, gap : int, marginx = 0, marginy = 0):

        self.board_width = self.cols*width + gap*(self.cols - 1)
        self.board_height = self.rows*height + gap*(self.rows - 1)
        self.x = center[0] - self.board_width//2
        self.y = center[1] - self.board_height//2
        for row in range(self.rows):
            row_tiles = []
            for col in range(self.cols):
                x = self.x + col + gap*col + width*col + marginx
                y = self.y + row + gap*row + height*row + marginy
                newTile = Tile(x,y,width, height, self.color, (0,0,0), col)
                if row==col==0:
                    self.current_tile = newTile
                    newTile.active = True
                self.tiles.append(newTile)
                row_tiles.append(newTile)
                
            new_row = Tile_Group(row_tiles, row)
            self.tile_groups += [new_row]
            self.tile_groups_remaining += [new_row]
        self.word = choose_word().upper()
        print(self.word)

    def render(self, win : pygame.Surface):
        if not self.visible:
            return
        for tile in self.tiles:
            tile.draw(win)

    def restart(self):
        self.word = choose_word().upper()
        print(self.word)
        for group in self.tile_groups:
            group.reset()
        self.tile_groups_remaining = [x for x in self.tile_groups]
        self.tile_groups_remaining[0].tiles[0].active = True

    def handleEvents(self, event : pygame.event.Event, keypad) -> bool | NoneType:

        if len(self.tile_groups_remaining) == 0:
            return False
        group = self.tile_groups_remaining[0]
        group.update(event)
        group.update_status()
        word = group.lock_group(event)
        if word == False:
            # notification = Notification()
            print("Not in word list")
            group.tiles[4].active = True
            return
        elif word:
            group.evaluate(self.word, keypad)
            if group.word.strip() == self.word:
                return True
            self.tile_groups_remaining.pop(0)
            if self.tile_groups_remaining:
                self.tile_groups_remaining[0].tiles[0].active = True
            print(f"============\n{word}\n{self.word}\n============")
        