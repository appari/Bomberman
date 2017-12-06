from game import *
import time
NUM_TICKS = 5


class Bomb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.num_ticks = NUM_TICKS
        self.cur_ticks = NUM_TICKS
        self.created_at = time.time()
        self.radius = 3

    def update(self, score):
        self.cur_ticks = int(self.num_ticks - (time.time() - self.created_at))
        if self.cur_ticks == 0:
            return
        else:
            self.cur_ticks -= 1
        return self.cur_ticks

    def populate(self, x, y, c=3):
        if self.cur_ticks > 0:
            board[x][y] = c
            board[x][y + 1] = c
            board[x][y + 2] = c
            board[x][y + 3] = c
            board[x + 1][y] = c
            board[x + 1][y + 1] = c
            board[x + 1][y + 2] = c
            board[x + 1][y + 3] = c

    def explode(self, score):
        i = self.x
        j = self.y
        for u in [i - 2, i, i + 2]:
            for v in [j - 4, j, j + 4]:
                if(board[u][v] == '[' and ((u - i) == 0 or (v - j) == 0)):
                    score = score
                elif(board[u][v] == '/' and ((u - i) == 0 or (v - j) == 0)):
                    self.populate(u, v, ' ')
                    temp_free.append((u, v))
                    score += 20
                elif(board[u][v] == ' ' and ((u - i) == 0 or (v - j) == 0)):
                    self.populate(u, v, '^')
                elif(board[u][v] == 'E'):
                    self.populate(u, v, ' ')
                    temp_free.append((u, v))
                    score += 100
        return score

    def depopulate(self):
        i = self.x
        j = self.y
        x = True
        for u in [i - 2, i, i + 2]:
            for v in [j - 4, j, j + 4]:
                if(board[u][v] == '[' and ((u - i) == 0 or (v - j) == 0)):
                    x = False
                elif(board[u][v] == '^'):
                    self.populate(u, v, ' ')
                elif(board[u][v] == 'B' or board[u][v] == 0 or board[u][v] == 1):
                    self.populate(u, v, ' ')
        return x

    def _del_(self):
        del self
