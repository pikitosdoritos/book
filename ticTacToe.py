theBoard = {"top-L": ' ', "top-M": ' ', "top-R": ' ',
            "mid-L": ' ', "mid-M": ' ', "mid-R": ' ', 
            "low-L": ' ', "low-M": ' ', "low-R": ' '
            }

def print_Board(board):
    print(board["top-L"] + '|' + board["top-M"] + '|' + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + '|' + board["mid-M"] + '|' + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + '|' + board["low-M"] + '|' + board["low-R"])
    
print_Board(theBoard)

turn = 'X'

for i in range(9):
    print_Board(theBoard)
    move = input("Turn for " + turn + " Move on which space? ")
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_Board(theBoard)