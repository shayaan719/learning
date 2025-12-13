board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
currentplayer = "x"
winner = None
gamerunning = True

#printing the game board
def printboard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# take player input
def playerinput(board):
    global currentplayer
    position = int(input("Enter position (1-9): "))
    if 1 <= position <= 9 and board[position-1] == "-":
        board[position-1] = currentplayer
    else:
        print("Invalid move")

# check horizontal win
def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    if board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    if board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

# check vertical win
def checkvertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

# check diagonal win
def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# check tie
def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("It is a tie!")
        gamerunning = False

# check win
def checkwin():
    global gamerunning
    if checkhorizontal(board) or checkvertical(board) or checkdiagonal(board):
        printboard(board)
        print(f"The winner is {winner}")
        gamerunning = False

# switch player
def switchplayer():
    global currentplayer
    if currentplayer == "x":
        currentplayer = "o"
    else:
        currentplayer = "x"

# main game loop
while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()