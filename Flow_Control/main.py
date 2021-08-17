#This is a Rock, Paper and Scissor games.
#This is copied code and it is just used for learning and evaluation purposes.

import random, sys

#These variable keeps track of the number of wins, losses and ties.
wins = 0
losses = 0
ties = 0

while True:
    print("%s Wins, %s Losses,%s TiesSs"%(wins, losses, ties))
    while True: #The input loop
        print("Enters your move\n(r)ock\n(p)aper,\nscissors\n(q)uit")
        playerMove = input("Input your move ? ")
        if playerMove == "q":
            sys.exit() #this will quit the program
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break #Break out of the player input loop
        print("Type one of r, p, s or q")

    #Display what the player chose.
    if playerMove == "r":
        print("ROCK versus ...")
    elif playerMove == "p":
        print("PAPER versus ...")
    elif playerMove == "s":
        print("Scissor versus ...")

    #Display what the computer chose
    randomNumber = random.randint(1,3)

    if randomNumber == 1:
        computerMove = "r"
        print("Rock")
    elif randomNumber == 2:
        computerMove = "p"
        print("Paper")
    elif randomNumber == 3:
        computerMove = "s"
        print("Scissors")

    #Display and record the Wins / losses and ties
    if playerMove == computerMove:
        print("its a tie")
        ties += 1
    elif playerMove == "r" and computerMove == "s" :
        print("You win!")
        wins += 1
    elif playerMove == "p" and computerMove == "r":
        print("You win")
        wins +=1
    elif playerMove == "s" and computerMove == "p":
        print("you win")
        wins +=1
    elif playerMove == "r" and computerMove == "p":
        print("You lose")
        losses += 1
    elif playerMove =="p" and computerMove == "s":
        print("You lose !")
        losses += 1
    elif playerMove == "s" and computerMove == "r":
        print("You lose")
        losses += 1
