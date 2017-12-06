from colorama import Fore
from random import randint
import os
board = []
free = []
temp_free = []
bricks = []


class Brick:
    def __inti__(self, x, y):
        self.x = x
        self.y = y


class Board:
    def __init__(self, hei=46, wid=164):
        self.hei = hei
        self.wid = wid
        for i in range(hei):
            width = []
            for j in range(wid):
                if(i < 2 or i > (hei - 3) or j < 4 or j > (wid - 5)):
                    width.append('#')
                else:
                    if(i % 4 < 2 and j % 8 < 4):
                        width.append('#')
                    else:
                        width.append(" ")
                        if(i % 2 is 0 and j % 4 is 0):
                            free.append((i, j))
            board.append(width)

        temp_free[:] = free
        self.allocate_bricks()

    def board_print(self):
        for i in range(self.hei):
            for j in range(self.wid):
                if(board[i][j] == '#'):
                    print("\033[92m{}\033[00m".format(
                        str(board[i][j])), end='')
                elif(board[i][j] == '/'):
                    print("\033[93m{}\033[00m".format(
                        str(board[i][j])), end='')
                elif(board[i][j] == 'E'):
                    print("\033[91m{}\033[00m".format(
                        str(board[i][j])), end='')
                elif(not type(board[i][j]) is int):
                    print("\033[34m{}\033[00m".format(
                        str(board[i][j])), end='')
                else:
                    print(board[i][j], end='')
            print('\n', end='')

    def free_board(self):
        return free

    def allocate_bricks(self):
        N = randint(20, 80)
        for num in range(N):
            x = randint(1, len(temp_free) - 3)
            if((temp_free[x] != (4, 4)) and (temp_free != (2, 8))):
                bricks.append(temp_free[x])
                temp_free.remove(temp_free[x])
        for x in bricks:
            board[x[0]][x[1]] = '/'
            board[x[0] + 1][x[1]] = '/'
            board[x[0]][x[1]] = board[x[0]][x[1]] = '/'
            board[x[0]][x[1] + 1] = board[x[0] + 1][x[1] + 1] = '/'
            board[x[0]][x[1] + 2] = board[x[0] + 1][x[1] + 2] = '/'
            board[x[0]][x[1] + 3] = board[x[0] + 1][x[1] + 3] = '/'

    def refresh(self):
        os.system('clear')
        self.board_print()

    def reset_board(self):
        temp_free[:] = free
        os.system('clear')
        self.board_print()
