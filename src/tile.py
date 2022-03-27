import pygame
from settings import *
from word import is_allowed
from textbox import Text

class Tile_Group:
    
    def __init__(self, tiles : list, index : int):

        self.index = index
        self.tiles = tiles
        self.is_done = False
        self.is_finalized = False
        self.word = ''
    
    def reset(self):

        self.is_done = False
        self.is_finalized = False
        self.word = ''
        for tile in self.tiles:
            tile.reset()

    def update_status(self):

        check_list = []
        for tile in self.tiles:
            if tile.text == '':
                check_list.append(False)
                continue
            check_list.append(True)

        self.is_done = all(check_list)
        
    def evaluate(self, word : str, keypad) -> bool:
        # TODO : Check for exceptions
        unique_vals = list(set([x for x in self.word]))
        greened = []
        counter = {x:0 for x in unique_vals}

        for i,j,count in zip(self.word, word, range(len(self.word))):
            if i == j:
                self.tiles[count].color = COLORS.CORRECT
                greened.append(self.tiles[count])
                keypad.change_status(i, COLORS.CORRECT)
                counter[i] += 1


        for idx, i in enumerate(self.word):
            if self.tiles[idx] in greened:
                continue
            if i in word:
                if counter[i] < word.count(i):
                    self.tiles[idx].color = COLORS.MISMATCH
                    keypad.change_status(i, COLORS.MISMATCH)
                    counter[i] += 1
                else:
                    self.tiles[idx].color = COLORS.INCORRECT
            else:
                self.tiles[idx].color = COLORS.INCORRECT
                keypad.change_status(i, COLORS.INCORRECT)
        
            
    def lock_group(self, event : pygame.event.Event) -> bool | str:

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.is_done == True:
                    self.is_finalized = True
                    word = ''
                    for tile in self.tiles:
                        if tile.active == True:
                            tile.active = False
                        word += tile.text
                    self.word = word
                    if is_allowed(self.word):
                        return word
                    return False

    def update(self, event : pygame.event.Event):

        for i in self.tiles:
            col = i.handleEvent(event)
            if col or col == 0:
                self.tiles[col].active = True
                break

class Tile:

    def __init__(self, x : int, y: int, width : int, height : int, color: tuple, text_color : tuple, index,text = ''):

        self.rect = pygame.Rect(x, y, width, height)
        self.text_color = text_color
        self.color = color
        self.active_color = COLORS.SELECT
        self.index = index
        self.text = text
        self.active = False
        self.text_surface = Text(self.text, self.rect.center, text_color)

    def draw(self, win:pygame.Surface):

        color = self.color if self.active != True else self.active_color
        pygame.draw.rect(win, color, self.rect, border_radius=5)
        self.text_surface.render(win)

    def reset(self, keep_text = False):

        self.color = COLORS.DEFAULT
        self.active_color = COLORS.SELECT
        if keep_text == False:
            self.text = ''
            self.text_surface = Text(self.text, self.rect.center, self.text_color)
        self.active = False

    def handleEvent(self, event : pygame.event.Event) -> int:

        if event.type == pygame.KEYDOWN:

            if self.active and event.key != pygame.K_RETURN:

                if event.key == pygame.K_BACKSPACE:
                    self.text = ''
                    self.text_surface = Text(self.text, self.rect.center, self.text_color)
                    col_idx = self.index - 1
                    self.active = False
                    if col_idx < 0 :
                        self.active = True
                        return 0
                    return col_idx

                elif event.unicode.isalpha():
                    if self.text == '':
                        self.text = event.unicode.upper()
                        self.text_surface = Text(self.text, self.rect.center, self.text_color)
                    self.active = False
                    col_idx = self.index + 1
                    if col_idx > 4:
                        return 4
                    return col_idx

                elif event.key == pygame.K_RIGHT:
                    self.active = False
                    col_idx = self.index + 1
                    if col_idx > 4:
                        return 0
                    return col_idx
                
                elif event.key == pygame.K_LEFT:
                    self.active = False
                    col_idx = self.index - 1
                    if col_idx < 0:
                        return 4
                    return col_idx


