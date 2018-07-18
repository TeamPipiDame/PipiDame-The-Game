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

import random



global counter1,counter2
counter1 = 0
counter2 = 0
def pepe_dame():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_combis = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


    def chooseComputerMove():

    #This just fills a list with all the empty boxes and chooses one at random
       emptyBoxes = []
       for i in range(0, 3):
           for j in range(0, 3):
               if emptyBoxes[i][j] == 0:
                   emptyBoxes += [[i, j]]

       return emptyBoxes[random.randint(1, len(emptyBoxes) - 1)]

 # Make the computer's move
##    computerMove = chooseComputerMove()
##    boxes[computerMove[0]][computerMove[1]] = 1
##    print('\n' 'Computer\'s turn:')
##    printGrid()

    # Check if the computer's move won the game
##    victoryResult = check_board()
##    if board[s[0]] == board[s[1]] == board[s[2]] == "O":
##                print("Hurraaayyy!!!! \n Computer Wins!\n")
##                return True
##    else:
##        check_board()
##    if (victoryResult == 'O'):
##        print ('Computer wins!')
##           break


    
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
                    print("\nIdiot!!! Choose a number!")
                    continue

    def player1(n):
        print("Counter1 = " + str(counter1))
        end = check_board()
        
        if  board[n] == "O" or board[n] == "X" and counter1 < 3:
                print("\n Sorry, That position is unavailable.")
                new_choice = choice("Choose a different position with a number: ")
                player1(new_choice)


        elif counter1 >= 3:
            if board[n] == "X":

                if  n == 0:
                    r = choice("\nWhere do you want to move it to? ")
##                player1(s)
##                global counter1
##                counter1 = counter1 - 1
                
##                
                
##Check if move is allowed
##                for i in range(0,4):
##                    for j in range(0,n):
                  
                    if r == 1 or r == 3 or r == 4:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
##                        global counter1
##                        counter1 = counter1 + 1
                                
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
##                        global counter1
##                        counter1 = counter1 - 1
                        player1(t)
                        board[n] = n + 1
##                        global counter1
##                        counter1 = counter1 + 1
                        #player1(t)

                elif n == 1:
                    r = choice("\nWhere do you want to move it to? ")

                
##                for i in range(0,4):
##                    for j in range(0,n):
                        
                    if r == 0 or r == 2 or r == 4:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(s)
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter1
                        counter1 = counter1 - 1
                        player1(t)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(t)

                
##                for i in range(0,4):
##                    for j in range(0,n):
                elif n == 2:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 1 or r == 5 or r == 4:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(s)
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter1
                        counter1 = counter1 - 1
                        player1(t)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(t)


                
##                for i in range(0,4):
##                    for j in range(0,n):
                elif n == 3:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 0 or r == 6 or r == 4:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(s)
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter1
                        counter1 = counter1 - 1
                        player1(t)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(t)


                
##                for i in range(0,4):
##                    for j in range(0,n):
                elif n == 4:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 0 or r == 1 or r == 2 or r == 3 or r == 5 or r == 6 or r == 7 or r == 8:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(s)
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter1
                        counter1 = counter1 - 1
                        player1(t)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(t)


##                for i in range(0,4):
##                    for j in range(0,n):
                elif n == 5:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 2 or r == 4 or r == 8:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(s)
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter1
                        counter1 = counter1 - 1
                        player1(t)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(t)

##                for i in range(0,4):
##                    for j in range(0,n):
                elif n == 6:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 3 or r == 4 or r == 7:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(s)
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter1
                        counter1 = counter1 - 1
                        player1(t)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(t)


##                for i in range(0,4):
##                    for j in range(0,n):
                elif n == 7:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 6 or r == 4 or r == 8:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(r)
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter1
                        counter1 = counter1 - 1
                        player1(t)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(t)


                elif n == 8:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 5 or r == 4 or r == 7:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(r)
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter1
                        counter1 = counter1 - 1
                        player1(t)
                        board[n] = n + 1
                        global counter1
                        counter1 = counter1 + 1
                        #player1(t)

##            elif board[n] == "O" and counter:
##                print("\n Sorry, That position is unavailable")
##                new_choice = choice("Choose a position with an 'X': ")
##                player1(new_choice)

            
                

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

        if  board[n] == "O" or board[n] == "X" and counter2 < 3:
                print("\n Sorry, That position is unavailable.")
                new_choice = choice("Choose a different position with a number: ")
                player2(new_choice)


        elif counter2 >= 3:
            if board[n] == "O":
                
                
##                player1(s)
##                global counter1
##                counter1 = counter1 - 1
                
##                
                
##Check if move is allowed
##
                if n == 0:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 1 or r == 3 or r == 4:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
##                        global counter2
##                        counter2 = counter2 + 1
                                
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
##                        global counter2
##                        counter2 = counter2 - 1
                        player2(t)
                        board[n] = n + 1
##                        global counter2
##                        counter2 = counter2 + 1
                        #player1(t)

                elif n == 1:
                    r = choice("\nWhere do you want to move it to? ")
                    
                    if r == 0 or r == 2 or r == 4:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                                
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter2
                        counter2 = counter2 - 1
                        player2(t)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                        #player1(t)


##                k = 1
##                for i in range(0,4):
##                    for j in range(0,k):
                elif n == 2:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 1 or r == 5 or r == 4:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                                
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter2
                        counter2 = counter2 - 1
                        player2(t)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                        #player1(t)

##                k = 1
##                for i in range(0,4):
##                    for j in range(0,k):
                elif n == 3:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 0 or r == 6 or r == 4:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                                
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter2
                        counter2 = counter2 - 1
                        player2(t)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                        #player1(t)

##                k = 1
##                for i in range(0,4):
##                    for j in range(0,k):
                elif n == 4:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 0 or r == 1 or r == 2 or r == 3 or r == 5 or r == 6 or r == 7 or r == 8:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                                
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter2
                        counter2 = counter2 - 1
                        player2(t)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                        #player1(t)

##                k = 1
##                for i in range(0,4):
##                    for j in range(0,k):
                elif n == 5:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 2 or r == 4 or r == 8:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                                
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter2
                        counter2 = counter2 - 1
                        player2(t)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                        #player1(t)


##                k = 1
##                for i in range(0,4):
##                    for j in range(0,k):
                elif n == 6:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 3 or r == 4 or r == 7:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                                
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter2
                        counter2 = counter2 - 1
                        player2(t)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                        #player1(t)

##                k = 1
##                for i in range(0,4):
##                    for j in range(0,k):
                elif n == 7:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 6 or r == 4 or r == 8:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                                
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter2
                        counter2 = counter2 - 1
                        player2(t)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                        #player1(t)

##                k = 1
##                for i in range(0,4):
##                    for j in range(0,k):
                elif n == 8:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 7 or r == 5 or r == 4:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                                
                    else:
                        print("Cheat! How can you move all the way there?")
                        t = choice("\nMake another choice: ")
                        global counter2
                        counter2 = counter2 - 1
                        player2(t)
                        board[n] = n + 1
                        global counter2
                        counter2 = counter2 + 1
                        #player1(t)


##            elif board[n] == "X":
##                print("\n Sorry, That position is unavailable")
##                new_choice = choice("Choose a position with an 'O': ")
##                player2(new_choice)
                

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
        u = input("Press 'p' to play against another player and 'c' to play against the computer: ")
        if u == 'p':
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
                draw()
                end = check_board()
                

            if input("Play again (y/n)\n") == "y":
                print()
                global counter1, counter2
                counter1 = 0
                counter2 = 0
                pepe_dame()

        elif u == 'c':
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
                n = choice("Computer's turn: ")
                chooseComputerMove()
                print()
                draw()
                end = check_board()

            if input("Play again (y/n)\n") == "y":
                print()
                global counter1, counter2
                counter1 = 0
                counter2 = 0
                pepe_dame()


##    pygame.display.update() 
##    print("Ab) ano")
##    return True

    

pepe_dame()
            
                    
            
            
            
        
