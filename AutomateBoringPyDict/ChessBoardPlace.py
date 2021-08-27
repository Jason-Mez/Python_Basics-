#Write a function called is caled ChessBoard
#Should take in a dictionary
#Return True or False

#A valid chess board will have exactly 1 Black King and 1 White king
# The Piece names begin with either "w or b" to represent black or white

white_pieces= {
    "a1": "wrook",
    "b1": "wknight",
    "c1": "wbishop",
    "d1": "wqueen",
    "e1": "wking",
    "f1": "wbishop",
    "g1": "wknight",
    "h1": "wrook"
}

black_pieces = {
    "a8": 'brook',
    "b8": "bknight",
    "c8": "bbishop",
    "d8": "bqueen",
    "e8": "bking",
    "f8": "bbishop",
    "g8": "bknight",
    "h8": "brook"
}

def isValidChessBoard(white_pieces: list):
    try:
        for i in range(9):
            if "wrook" == white_pieces["a1"]:
                print("True")
            if "wknight" == white_pieces["b1"]:
                print("True")
            if "wbishop" == white_pieces["c1"]:
                print("True")
            if "wqueen" == white_pieces["d1"]:
                print("True")
            if "wking" == white_pieces["e1"]:
                print("True")
            if "wbishop" == white_pieces["f1"]:
                print("True")
            if "wknight" == white_pieces["g1"]:
                print("True")
            if "wrook" == white_pieces["h1"]:
                print("Okay")
        print("All your pieces are in order")
        return True
    except Exception:
        print("Your pieces are not in the right order.")
        return False

x  = isValidChessBoard(white_pieces)
print(x)