'''
根据某个云课堂上面的免费教程，写出来的2048游戏
采用了pyglet库，功能简单，有重置游戏和保存十步的回退功能。
'''
import copy
import random

import pyglet
from pyglet.window import key

WIN_WIDTH = 530
WIN_HEIGHT = 720

STARTX = 15
STARTY = 110

WINDOW_BLOCK_NUM = 4

BOARD_WIDTH = (WIN_WIDTH - 2 * STARTX)
BLOCK_WIDTH = BOARD_WIDTH / WINDOW_BLOCK_NUM

COLORS = {
    0: (204, 192, 179), 2: (238, 228, 218), 4: (237, 224, 200), 8: (242, 177, 121),
    16: (245, 149, 99), 32: (246, 124, 95), 64: (246, 94, 59), 128: (237, 207, 114),
    256: (233, 170, 7), 512: (215, 159, 14), 1024: (222, 186, 30), 2048: (222, 212, 30)
}

LABEL_COLOR = (119, 110, 101, 255)
BG_COLOR = (250, 248, 239, 255)
LINE_COLOR = (165, 165, 165, 255)


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        self.game_init()

    def game_init(self):
        self.main_batch = pyglet.graphics.Batch()
        # self.data = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.data = [[0 for i in range(WINDOW_BLOCK_NUM)] for j in range(WINDOW_BLOCK_NUM)]
        count = 0

        while count <2:
            row = random.randint(0,WINDOW_BLOCK_NUM-1)
            col = random.randint(0,WINDOW_BLOCK_NUM-1)
            if self.data[row][col]!=0:
                count +=1
                continue
            self.data[row][col] =2 if random.randint(0,1) else 4
            count +=1

        self.buffer = [copy.deepcopy(self.data)]
        self.max_buffer_len = 10


        background_img = pyglet.image.SolidColorImagePattern(color=BG_COLOR)
        self.background = pyglet.sprite.Sprite(
            background_img.create_image(WIN_WIDTH, WIN_HEIGHT), 0, 0
        )

        self.title_label = pyglet.text.Label(text='2048', bold=True,
                                             color=LABEL_COLOR, x=STARTX, y=BOARD_WIDTH + STARTY + 30,
                                             font_size=36, batch=self.main_batch)

        self.score = 0
        self.score_label = pyglet.text.Label(text='Score=%d' % (self.score), bold=True,
                                             color=LABEL_COLOR, x=200, y=BOARD_WIDTH + STARTY + 30,
                                             font_size=36, batch=self.main_batch)

        self.help_label = pyglet.text.Label(text='please use up,down,left,right to play!', bold=True,
                                            color=LABEL_COLOR, x=STARTX, y=STARTY - 30,
                                            font_size=18, batch=self.main_batch)
        self.undo_lable = pyglet.text.Label(text='please u to undo,you can undo %d times.' %(len(self.buffer)), bold=True,
                                            color=(119,110,101,255), x=STARTX, y=60,
                                            font_size=16, batch=self.main_batch)
        self.restart_lable = pyglet.text.Label(text='please R to restart,ESC to quit.', bold=True,
                                            color=(119,110,101,255), x=STARTX, y=35,
                                            font_size=16, batch=self.main_batch)

    def on_draw(self):
        self.clear()
        self.score_label.text = 'Score=%d' % (self.score)
        self.undo_lable.text = 'please u to undo,you can undo %d times.' %(len(self.buffer))
        self.background.draw()


        for row in range(WINDOW_BLOCK_NUM):
            for col in range(WINDOW_BLOCK_NUM):
                x = STARTX + BLOCK_WIDTH * col
                y = STARTY + BOARD_WIDTH - BLOCK_WIDTH - BLOCK_WIDTH * row
                self.draw_tile((x, y, BLOCK_WIDTH, BLOCK_WIDTH), self.data[row][col])

        self.main_batch.draw()
        self.draw_grid(STARTX, STARTY)

    def draw_grid(self, startx, starty):
        rows = columns = WINDOW_BLOCK_NUM + 1
        for i in range(rows):
            pyglet.graphics.draw(
                2, pyglet.gl.GL_LINES,
                ('v2f',
                 (startx, i * BLOCK_WIDTH + starty, WINDOW_BLOCK_NUM * BLOCK_WIDTH + startx,
                  i * BLOCK_WIDTH + starty)
                 ),
                ('c4B', LINE_COLOR * 2)
            )
        for j in range(columns):
            pyglet.graphics.draw(
                2, pyglet.gl.GL_LINES,
                ('v2f',
                 (j * BLOCK_WIDTH + startx, starty, j * BLOCK_WIDTH + startx, WINDOW_BLOCK_NUM * BLOCK_WIDTH + starty)
                 ),
                ('c4B', LINE_COLOR * 2)
            )

    def draw_tile(self, xywh, data):
        x, y, dx, dy = xywh
        color_rgb = COLORS[data]
        corners = [x + dx, y + dy, x, y + dy, x, y, x + dx, y]
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', corners), ('c3B', color_rgb * 4))

        if data != 0:
            a = pyglet.text.Label(text=str(data), bold=True, anchor_x='center', anchor_y='center',
                                  color=(0, 0, 0, 255), x=x + dx / 2, y=y + dy / 2, font_size=28)
            a.draw()

    def on_key_press(self, symbol, modifiers):
        eq_tile = False
        key_press = False
        score = 0

        if symbol == key.UP:
            self.data, eq_tile, score = self.slideUpDown(True)
            key_press = True
        elif symbol == key.DOWN:
            self.data, eq_tile, score = self.slideUpDown(False)
            key_press = True
        elif symbol == key.LEFT:
            self.data, eq_tile, score = self.slideLeftRight(True)
            key_press = True
        elif symbol == key.RIGHT:
            self.data, eq_tile, score = self.slideLeftRight(False)
            key_press = True
        elif symbol == key.ESCAPE:
            self.close()
        elif symbol == key.U:
            #undo
            if len(self.buffer)>0:
                self.data = self.buffer[-1]
                del self.buffer[-1]
        elif symbol == key.R:
            #reset
            self.game_init()

        self.score += score

        if key_press and (not self.put_tile()):
            _,a,_ =self.slideUpDown(True)
            _,b,_ = self.slideUpDown(False)
            _,c,_ = self.slideLeftRight(True)
            _,d,_ = self.slideLeftRight(False)
            if a and b and c and d:
                print('game over')
                txt = pyglet.text.Label(text='You Lose,\nPlease try again!', bold=True, anchor_x='center', anchor_y='center',
                                      color=(255, 255, 205, 255), x=WIN_WIDTH/ 2, y=WIN_HEIGHT/ 2, width=500,
                                      font_size=28,batch=self.main_batch)

        if key_press and (not eq_tile):
            if len(self.buffer)==self.max_buffer_len:
                del self.buffer[0]
            self.buffer.append(copy.deepcopy(self.data))

    def merge(self, vlist, direct):
        score = 0
        if direct:
            i = 1
            while i < len(vlist):
                if vlist[i - 1] == vlist[i]:
                    del vlist[i]
                    vlist[i - 1] *= 2
                    score += vlist[i - 1]
                i += 1
        else:
            i = len(vlist) - 1
            while i > 0:
                if vlist[i - 1] == vlist[i]:
                    del vlist[i]
                    vlist[i - 1] *= 2
                    score += vlist[i - 1]
                i -= 1
        return score

    def slideUpDown(self, up):
        oldData = copy.deepcopy(self.data)
        score = 0

        for col in range(WINDOW_BLOCK_NUM):
            cvl = [oldData[row][col] for row in range(WINDOW_BLOCK_NUM) if oldData[row][col] != 0]

            if len(cvl) >= 2:
                score += self.merge(cvl, up)

            for i in range(WINDOW_BLOCK_NUM - len(cvl)):
                if up:
                    cvl.append(0)
                else:
                    cvl.insert(0, 0)

            for row in range(WINDOW_BLOCK_NUM): oldData[row][col] = cvl[row]
        return oldData, oldData == self.data, score

    def slideLeftRight(self, left):
        oldData = copy.deepcopy(self.data)
        score = 0

        for row in range(WINDOW_BLOCK_NUM):
            cvl = [oldData[row][col] for col in range(WINDOW_BLOCK_NUM) if oldData[row][col] != 0]

            if len(cvl) >= 2:
                score += self.merge(cvl, left)

            for i in range(WINDOW_BLOCK_NUM - len(cvl)):
                if left:
                    cvl.append(0)
                else:
                    cvl.insert(0, 0)

            for col in range(WINDOW_BLOCK_NUM): oldData[row][col] = cvl[col]
        return oldData, oldData == self.data, score

    def put_tile(self):
        available =[]
        for row in range(WINDOW_BLOCK_NUM):
            for col in range(WINDOW_BLOCK_NUM):
                if self.data[row][col]== 0:available.append((row,col))
        if available:
            row,col = available[random.randint(0,len(available)-1)]
            self.data[row][col] = 2 if random.randint(0,1) else 4
            return True
        else:
            return False

if __name__ == '__main__':
    win = Window(WIN_WIDTH, WIN_HEIGHT)

    pyglet.app.run()
