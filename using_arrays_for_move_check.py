import pygame, sys, os
import tkinter as tk
from pygame.locals import *

##pygame.init()
##screen = pygame.display.set_mode((640, 400))
### you only need to call the following once,so pull them out of the  while loop.
####bird = pygame.image.load(os.path.join('interface.bmp'))
####clock = pygame.time.Clock()
##
####size = width, height = 750, 750
####speed = [2, 2]
####black = 0, 0, 0
##
####screen = pygame.display.set_mode(size)
##
##background=pygame.image.load("interface.bmp")

global counter1,counter2
counter1 = 0
counter2 = 0
def pepe_dame():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    board_array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    board_array[0] = [2, 4, 5]
    board_array[1] = [1, 3, 5]
    board_array[2] = [2, 6, 5]
    board_array[3] = [1, 7, 5]
    board_array[4] = [1, 2, 3, 4, 6, 7, 8, 9]
    board_array[5] = [3, 9, 5]
    board_array[6] = [4, 8, 5]
    board_array[7] = [7, 9, 5]
    board_array[8] = [6, 9, 5]
    end = False
    win_combis = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def valid_move1(current, new):
        if new in board_array[current]:
            board[current] = current + 1
            new_position = choice(new)
            global counter1
            counter1 = counter1 - 1
            player1(new_position)


    def valid_move2(current, new):
        if new in board_array[current]:
            board[current] = current + 1
            new_position = choice(new)
            global counter2
            counter2 = counter2 - 1
            player2(new_position)
        
    def draw():
        print("\n", board[0], "  ", board[1], "  ", board[2])
        print("\n", board[3], "  ", board[4], "  ", board[5])
        print("\n", board[6], "  ", board[7], "  ", board[8])
        print()


    def choice(message):
        while True:
            while True:
                s = input(message)
                try:
                    s = int(s)
                    s = s - 1
                    if s in range(0, 9):
                        return s
                    else:
                        print("Ad3n, w'ani afra? Choose from the board.")
                        continue
                except ValueError:
                    print("\nFine... Choose a number!")
                    continue

    def player1(n):
        print("Counter1 = " + str(counter1))
        end = check_board()
        
        if  board[n] == "O" or board[n] == "X" and counter1 < 3:
            print("\n Sorry, That position is unavailable")
            new_choice = choice("Choose a different position")
            player1(new_choice)


        elif counter1 >= 3:
            if board[n] == "X":
                t = input("\nWhere do you want to move it to? ")
                valid_move1(n, t)
                
                
##Check if move is allowed                
                

            elif board[n] == "O":
                print("\n Sorry, That position is unavailable")
                new_choice = choice("Choose a position with an 'X': ")
                player1(new_choice)
                

            else:
                print("You are an idiot... You can't add more than three pieces")
                new_choice = choice("Choose any of your old marbles to move it: ")
                #global counter1
                #counter1 = counter1 - 1
                player1(new_choice)
                

        else:
            board[n] = "X"
            global counter1
            counter1 = counter1 + 1
        
        if end: print(end)
            

    def player2(n):
        print("Counter2 = " + str(counter2))
        end = check_board()
        
        if  board[n] == "X" or board[n] == "O" and counter2 != 3:
            print("\n Sorry, That position is unavailable")
            new_choice = choice("Choose a different position")
            player2(new_choice)

        elif counter2 == 3:
            if board[n] == "O":
                t = input("\nWhere do you want to move it to? ")
                valid_move2(n, t)


            elif board[n] == "X":
                print("\n Sorry, That position is unavailable")
                new_choice = choice("Choose a position with an 'O': ")
                player2(new_choice)
                

            else:
                print("You are an idiot... You can't add more than three pieces")
                new_choice = choice("Choose any of your old marbles to move it: ")
                #global counter2
                #counter2 = counter2 - 1
                player2(new_choice)
                

        else:
            board[n] = "O"
            global counter2
            counter2 = counter2 + 1
            
        if end: print(end)


    def check_board():
        count = 0
        for s in win_combis:
            if board[s[0]] == board[s[1]] == board[s[2]] == "X":
                print("Hurraaayyy!!!! \n Player 1 Wins!\n")
                return True

            if board[s[0]] == board[s[1]] == board[s[2]] == "O":
                print("Hurraaayyy!!!! \n Player 2 Wins!\n")
                return True

        return False
##        for s in range(9):
##            if board[s] == "X" or board[s] == "O":
##                count = count + 1
##
##            if count == 5:
##                pygame.init()


##            running = True
##            while running:
##                event = pygame.event.poll()
##                if event.type == pygame.QUIT:
##                    running = False
                

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        n = choice("Player 1 make a choice: ")

        player1(n)
        print()
        draw()
        end = check_board()

        if end == True:
            break
        n = choice("Player 2 make a choice: ")
        player2(n)
        print()

    if input("Play again (y/n)\n") == "y":
        #print()
        global counter1, counter2
        counter1 = 0
        counter2 = 0
        pepe_dame()


##    pygame.display.update() 
##    print("Ab) ano")
##    return True

    

pepe_dame()
