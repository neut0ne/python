# Tic tac toe project!
#
# Different ways of building a board with nine spaces:
# a list with nine spaces:
# board = [" ", " ", " " ... ] (ugh, that's a lot of typing and repeating... Don't we have programming for that? Yes we do!)
#
# List comprehension to the rescue! And here's our 9 space board:
board = ["   " for i in range(9)]

# But, my board should be a 3 x 3 grid..? Well let's fix that then:
def printboard():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print("")
    print(row1)
    print(row2)
    print(row3)
    print("")

def player_move(icon):
    
    if icon == " X ":
        number = 1
    elif icon == " O ":
        number = 2

    print("Your turn, player number {}:".format(number))

    choice = int(input("Enter your move (1-9): "))
    if board[choice -1] == "   ":
        board[choice -1] = icon
    else:
        print("")
        print("That place is taken!")

def is_victory(icon):
    if board[0] == icon and board[1] == icon and board[2] == icon or \
       board[3] == icon and board[4] == icon and board[5] == icon or \
       board[6] == icon and board[7] == icon and board[8] == icon or \
       board[0] == icon and board[3] == icon and board[6] == icon or \
       board[1] == icon and board[4] == icon and board[7] == icon or \
       board[2] == icon and board[5] == icon and board[8] == icon or \
       board[0] == icon and board[4] == icon and board[8] == icon or \
       board[2] == icon and board[4] == icon and board[6] == icon:
        return True
    else:
        return False

def is_draw():
    if "   " not in board:
        return True
    else:
        return False

# Let's start the game:
while True:
    printboard()
    player_move(" X ")
    printboard()
    if is_victory(" X "):
        print("Congratulation, player 1! You win!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move(" O ")
    if is_victory(" O "):
        printboard()
        print("Congratulations, player 2! You win!")
        break
    elif is_draw():
        print("It's a draw!")
        break
