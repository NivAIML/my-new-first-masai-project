import random
board= ["_", "_", "_"
       "_", "_", "_"
        "_", "_", "_"]
        currentPlayer = "X"
        winner =None
        gameRunning = True


        #print the game board
        def print(board):
        print(board)[0] +"|" = board[1] +"|" + board[2])
        print("__________")
        print(board)[3] +"|" = board[4] +"|" + board[5])
        print("__________")
        print(board)[6] +"|" = board[7] +"|" + board[8])
        

#take player input
def playerInput(board):
    int = int(input("Enter a number 1-9:"))
    if inp >= 1 and inp <= 9 and board[int-1] == "_":
        board[int-1] = currentPlayer
    else:
        print("Oops player is already in that spot!")

# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1]  != "_":
    winner = boaed[0]
    return True 
    elif board[3] == board[4] == board[5] and board[3] !="_":
        winner = board[3]
        return True
        elif board[6] == board[7] == board[8] and board[6] != "_":
            winner = board[6]
            return True


            def checkRow(board):
                global winner
                if boaed[0]== board[3] == boaed[6] and board[0] !="_:"
                   winner = board[0]
                   return True
                elif boaed[1]== board[4] == boaed[7] and board[1] !="_:"
                   winner = board[1]
                   return True
                elif boaed[2]== board[5] == boaed[8] and board[2] !="_:"
                   winner = board[0]
                   return True



            def checkDiag(board):
                    global winner
                    if board[0] ==boarf[8] == board[8] and board[0] != "_":
                        winner = board[0]
                        return True
                    elif board[2] == board[4] == board[6] and board[2] !="_":
                        winner = board[2]
                        return True 


                        def checkTie(board):
                            global gameRunning
                            if "_" not in board:
                                printBoard(board)
                                print("It is a tie!")
                                gameRunning = False

def checkWin():
    if checkDiag(board) or checkHorizontel or checkRow(board)or checkRow(boad)
    print(f"the winner is  {winner""}")


#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer ="0"
        else:
            currentPlayer ="X"

# computer
def computer(board):
    while currenPlayer =="0"
    position = random.randint(0, 8)
    if board[position] == "_":
        board[position] = "0"
        switchPlayer()

# check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
    