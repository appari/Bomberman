from person import *
from bomb import *
import time
import sys
import getch
from enemy import *
from getchunix import *
from alarmexception import *
from random import randint
getch = GetchUnix()


def alarmHandler(signum, frame):
    raise AlarmException


def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        (" ")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


M = 200


class Game:
    def __init__(self):
        self.pre_board = Board()
        self.pre_free = free
        self.brick_p = bricks
        self.bomber = Bomberman()
        self.bomb = [0] * M
        self.no_enemy = N = 7
        self.score = 0
        self.enemy = [0] * N
        self.lives = 4
        for r in range(N):
            rand = randint(4, len(temp_free) - 3)
            self.enemy[r] = Enemy(temp_free[rand][0], temp_free[rand][1])
        self.start_time = time.time()

    def begin(self):
        for r in range(self.no_enemy):
            self.enemy[r].spawn()
        self.bomber.spawn()
        count = time.time() + 2
        bomb_c = [False] * M
        start = [0] * M
        c = M - 1
        while True:
            x = input_to()
            ar = ['a', 'w', 'd', 's']
            if(x is 'a'):
                if(not self.bomber.move(0, -4)):
                    if(self.lives == 0):
                        print('GAME OVER')
                        exit()
                    else:
                        self.lives -= 1
                        self.bomber.move(2 - self.bomber.x, 4 - self.bomber.y)
            elif(x is's'):
                if(not self.bomber.move(2, 0)):
                    if(self.lives == 0):
                        print('GAME OVER')
                        exit()
                    else:
                        self.lives -= 1
                        self.bomber.move(2 - self.bomber.x, 4 - self.bomber.y)
            elif(x is 'd'):
                if(not self.bomber.move(0, 4)):
                    if(self.lives == 0):
                        print('GAME OVER')
                        exit()
                    else:
                        self.lives -= 1
                        self.bomber.move(2 - self.bomber.x, 4 - self.bomber.y)
            elif(x is 'w'):
                if(not self.bomber.move(-2, 0)):
                    if(self.lives == 0):
                        exit()
                        print('GAME OVER')
                    else:
                        self.lives -= 1
                        self.bomber.move(2 - self.bomber.x, 4 - self.bomber.y)
            elif(x is 'b' and c >= 0):
                self.bomb[c] = Bomb(self.bomber.x, self.bomber.y)
                bomb_c[c] = True
                start[c] = time.time()
                self.bomb[c].populate(self.bomber.x, self.bomber.y, 2)
                c -= 1
            elif(x is 'q'):
                print("USER EXITED")
                exit()
            if(time.time() >= count):
                count = time.time() + 1
                for r in range(M):
                    if(bomb_c[r] and (time.time() - start[r]) > 3):
                        self.score = self.bomb[r].explode(self.score)
                        self.pre_board.board_print()
                        e = self.bomb[r].depopulate()
                        if((not e) or (self.bomb[r].x == self.bomber.x
                                       and self.bomb[r].y == self.bomber.y)):
                            if(self.lives == 0):
                                print('GAME OVER')
                                exit()
                            else:
                                self.lives -= 1
                                self.bomber.move(
                                    2 - self.bomber.x, 4 - self.bomber.y)
                        self.bomb[r]._del_()
                        bomb_c[r] = False
                    if(bomb_c[r] and time.time() - start[r] < 3):
                        self.bomb[r].populate(
                            self.bomb[r].x, self.bomb[r].y, int(
                                3 - time.time() + start[r]))

                for r in range(self.no_enemy):
                    xu = self.enemy[r].x
                    yu = self.enemy[r].y
                    ra = randint(0, 3)
                    if(board[xu][yu] == 'E'):
                        if(not self.enemy[r].movement(ar[ra], xu, yu)):
                            if(self.lives == 0):
                                print('GAME OVER')
                            else:
                                self.lives -= 1
                                self.bomber.populate(2, 4)
            os.system('clear')
            self.pre_board.board_print()
            print("TIME:", int(183 - count + self.start_time))
            print("TOTAL_SCORE:", self.score)
            print('LIVES:', self.lives)
            if(int(183 - count + self.start_time) == 0):
                print('TIME OUT')
                exit()
            if(len(temp_free) == len(free)):
                print("COMPLETED")
                exit()


if __name__ == "__main__":
    g = Game()
    g.begin()
