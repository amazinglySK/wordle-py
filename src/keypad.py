from settings import *
from tile import Tile

class Keypad:

    def __init__(self,pos : tuple, color : tuple,  cols = 6, rows = 5):
        self.visible = False
        self.keys = []
        self.cols = cols
        self.color = color
        self.pos = pos
        self.rows = rows
        self.x = 0
        self.y = 0
        self.board_width = 0
        self.board_height = 0

    def create(self, height : int, width : int, gap : int, marginx = 0, marginy = 0):

        self.board_width = self.cols*width + gap*(self.cols - 1)
        self.board_height = self.rows*height + gap*(self.rows - 1)

        self.x = self.pos[0] - self.board_width//2
        self.y = self.pos[1] - self.board_height//2
        letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
        for idx, char in enumerate(letters):
            col = idx%self.cols
            row = idx//self.cols
            x = self.x + col + gap*col + width*col + marginx
            y = self.y + row + gap*row + height*row + marginy
            newTile = Tile(x,y,width, height, self.color, (0,0,0), col, char)
            self.keys.append(newTile)

    def render(self, win : pygame.Surface):

        if not self.visible:
            return
        for tile in self.keys:
            tile.draw(win)

    def change_status(self, letter :int, color : tuple):
        for i in self.keys:
            if i.text.upper() == letter:
                if i.color != COLORS.CORRECT:
                    i.color = color

    def reset(self):
        for key in self.keys:
            key.reset(True)
        