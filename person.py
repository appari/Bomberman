
from board import *
import os


class Person:
    def __init__(self, x, y, enemy):
        self.x = x
        self.y = y
        self.enemy = enemy

    def move(self, dx, dy):
        x = self.x + dx
        y = self.y + dy
        if((x, y) in temp_free):
            self.populate(x, y)
            temp_free.remove((x, y))
            temp_free.append((x - dx, y - dy))
        elif(board[x][y] == 'E'):
            return False
        return True

    def cur_pos(self):
        return (self.x, self.y)


class Bomberman(Person):
    def __init__(self, x=2, y=4):
        Person.__init__(self, x, y, False)

    def spawn(self, x=2, y=4):
        board[x][y] = '['
        board[x][y + 1] = '^'
        board[x][y + 2] = '^'
        board[x][y + 3] = ']'
        board[x + 1][y + 1] = ']'
        board[x + 1][y + 2] = '['

    def populate(self, fx, fy):
        y = fy
        x = fx
        u = self.x
        v = self.y
        if(board[u][v] == '['):
            board[u][v] = board[u][v + 1] = board[u][v + 2] = " "
            board[u][v + 3] = board[u + 1][v + 1] = board[u + 1][v + 2] = " "
            board[u + 1][v] = board[u + 1][v + 3] = " "
        self.x = x
        self.y = y
        board[x][y] = '['
        board[x][y + 1] = '^'
        board[x][y + 2] = '^'
        board[x][y + 3] = ']'
        board[x + 1][y + 1] = ']'
        board[x + 1][y + 2] = '['
        board[x + 1][y] = ' '
        board[x + 1][y + 3] = ' '

    def move(self, dx, dy):
        x = self.x + dx
        y = self.y + dy
        if((x, y) in temp_free):
            self.populate(x, y)
            temp_free.remove((x, y))
            temp_free.append((x - dx, y - dy))
        elif(board[x][y] == 'E'):
            return False
        return True

    def cur_pos(self):
        return (self.x, self.y)
