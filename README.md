# Bomberman
* Introduction:
    >Bomberman is a very popular game which have been played during our childhood.
    >This is a python program that simulates a basic version of Bomberman with different set of rules.
    >This program has to be run in any linux environment.
    >The requirements for running the program are in 'requirements.txt' and can be installed by the command 'pip3 install -r requirements.txt'.
    >If u r not familiar with the game you can look it up at 'https://en.wikipedia.org/wiki/Bomberman'.

* About the code:
    >The code contains the follow classes:
        1.Board
        2.Brick
        3.Person
            |__Bomberman
            |__Enemy
        4.Bomb
        5.Game
     >The Person class is being inherited by  Bomberman and Enemy  classes.
     >The Game class imports all the classes and the creates an instance of the e.
     >The files alarmexception and getchunix are used to take synchronous input from the user.	

* Controls:
    > The controls for the program are as follows
        'a'  -   move left
        's'  -   move down
        'd'  -   move right
        'w'  -   move up
        'b'  -   place a bomb
        'q'  -   quit the game

* Representation:
        [^^]   _   Bomberman
         ][

         EEEE  _   Enemy
          EE

         XXXX  _  (where x is any number) Bomb
         XXXX

         ####  _   Wall
         ####

         ////  _   Brick
         ////
* Game:
	>Your goal is to destroy all the enemies and the bricks.
	>Score-
		enemy  - 100
		bricks - 20
	>You are given 180s to complete the game.
	>You are also given 5 lives to complete the game.
	>The bomb explodes after 3s of placement.	

* Directory Structure:
    Assignment1_20161038.zip
    |--Assignment1_20161038
        |--game.py
        |--board.py
        |--person.py
        |--bomb.py
        |--alarmexception.py
        |--getchunix.py
        |--enemy.py
        |--README.tex
        |--requirements.txt
* Execution:
The game can be played executing the command 'python3 game.py' in Assignment1_20161038 directory.
