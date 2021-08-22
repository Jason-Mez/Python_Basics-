#Conways Games of life
import random
import time
import copy

WIDTH = 60
HEIGHT = 60

#Create a list of list for the cells
nextCells = []
for i in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#")
        else:
            column.append("") #Add a dead cell
        nextCells.append(column)

    while True:
        print()
