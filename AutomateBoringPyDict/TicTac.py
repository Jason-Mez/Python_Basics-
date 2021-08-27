#The board
#This is just a very simple tic-tac toes games

theBoard = {"top-L": '',
            "top-M": "",
            "top-R": "",
            "mid-L": "",
            "mid-M": "",
            "mid-R": "",
            "low-L": "",
            "low-M": "",
            "low-R": ""
            }

def printBoard(board):
    print(board["top-L"] +  "|"+ board['top-M'] + "|" + board["top-R"]) #Printing the correspornding values in the dictionary
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" +board["low-R"])

print(printBoard(theBoard))

turn = "X"

for i in range(9):
    print(printBoard(theBoard))
    print(f"Turn for {turn}. Move on which space ? ")
    move = input()
    theBoard[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X "
    printBoard(theBoard)