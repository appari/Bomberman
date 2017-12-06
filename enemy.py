from person import *
from board import *


class Enemy(Person):
    def __init__(self, x, y):
        Person.__init__(self, x, y, True)

    def cur_pos(self):
        self.x = x

    def spawn(self):
        self.populate(self.x, self.y)
        if((self.x, self.y) in temp_free):
            temp_free.remove((self.x, self.y))

    def populate(self, x, y):
        u = self.x
        v = self.y
        if(board[u][v] != '['):
            board[u][v] = board[u][v + 1] = board[u][v + 2] = " "
            board[u][v + 3] = board[u + 1][v + 1] = board[u + 1][v + 2] = " "
        self.x = x
        self.y = y
        board[x][y] = 'E'
        board[x][y + 1] = 'E'
        board[x][y + 2] = 'E'
        board[x][y + 3] = 'E'
        board[x + 1][y + 1] = 'E'
        board[x + 1][y + 2] = 'E'

    def move(self, dx, dy):
        x = self.x + dx
        y = self.y + dy
        if((x, y) in temp_free):
            self.populate(x, y)
            temp_free.remove((x, y))
            temp_free.append((x - dx, y - dy))

    def movement(self, x, xu, yu):
        if((x is 'a')):
            if((xu, yu - 4) in temp_free):
                self.move(0, -4)
            elif(board[xu][yu - 4] == '['):
                return False
        elif((x is's')):
            if((xu + 2, yu) in temp_free):
                self.move(2, 0)
            elif(board[xu + 2][yu] == '['):
                return False
        elif((x is 'd')):
            if((xu, yu + 4) in temp_free):
                self.move(0, 4)
            elif(board[xu][yu + 4] == '['):
                return False
        elif((x is 'w')):
            if((xu - 2, yu) in temp_free):
                self.move(-2, 0)
            elif(board[xu - 2][yu] == '['):
                return False
        return True

    def __del__(self):
        del self
