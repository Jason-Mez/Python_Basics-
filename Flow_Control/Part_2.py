import sys

#Looking at a base line view, their is while loop inside another while loop.
#The 1st while loop is the main loop.


import Part_1
while True:
    print("%s Wins, %s Losses, %s Ties"%(Part_1.wins, Part_1.losses, Part_1.ties))
    while True:
        playerMove = input()
        if playerMove == "q":
            sys.exit()
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break
        print("Type one of the following r, p, q, s. ")

#The second part of the loop is the most interesting.
#The 2nd part requested for an input.
#Inside the 2nd while loop..... ---->  There was an if statement.
#The 1st if statement aimed ---> Existing the program.
#The 2nd if statment wanted to get a legitimate ---> answer from the users.
#Once the request was submitted... it the broke out of the loop, it went back to the main loop.



