# build board game
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
board_log = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # Board cells aren't occupied

print("Welcome to Tic-Tac-Toe with numbers game!")
print("Game rule: Player 1 should enter odd numbers only while Player 2 should enter even numbers only")
print("The number values that are available are from 0 to 9")
print("Cell numbering starts from 1 to 9 and moves from left to right")


def display_board():
    # display board game
    print("-------------------")
    print("| ", board[0], " | ", board[1], " | ", board[2], " | ")
    print("-------------------")
    print("| ", board[3], " | ", board[4], " | ", board[5], " | ")
    print("-------------------")
    print("| ", board[6], " | ", board[7], " | ", board[8], " | ")
    print("-------------------")


def get_player_action(player):
    # get the cell number which the player wants to play in
    message = "Player " + str(player) + ": " + "Please enter the cell number you'd like to play in\n"
    is_valid = False
    while not is_valid:
        action = input(message)
        if not action.isdigit():
            continue
        else:
            is_valid = True
            action = int(action)
            is_valid = is_valid and int(action) > 0 and int(action) <= 9

    # check if the cell isn't already occupied
    while board[int(action) - 1] != "-":
        print("Already occupied!")
        action = input(message)

    return action


player1 = []
player2 = []


def get_player_value(player):
    # get the value that the player wants to enter in the cell
    value = int(input("Please enter the number value you'd like to put:\n"))
    if player == 1:
        # check if the value is odd or isn't -ve nor > 9 for player 1
        while value % 2 == 0 or value < 0 or value > 9:
            value = int(input("Please enter an odd number from 0 and 9:\n"))
        player1.append(value)
    else:
        # check if the value is even or isn't -ve nor > 9 for player 2
        while value % 2 != 0 or value < 0 or value > 9:
            value = int(input("Please enter an even number from 0 to 9:\n"))
        player2.append(value)
    return value


# checks if the number is already chosen or not
def check_repeat(value, player):
    if player == 1:
        while player1.count(value) >= 2 or value % 2 == 0:  # checks if player 1 entered an even num by mistake
            value = int(input("Please enter an odd number that isn't chosen before:\n"))
            player1.append(value)
    elif player == 2:
        while player2.count(value) >= 2 or value % 2 != 0:  # checks if player 2 entered an odd num by mistake
            value = int(input("Please enter an even number that isn't chosen before:\n"))
            player2.append(value)
    return value


def update_game_board(action, value):
    # update the board game with the user input
    board[int(action) - 1] = value
    # update the board log to "1" = (occupied)
    board_log[int(action) - 1] = 1
    display_board()


def is_winner():
    if(board_log[0] + board_log[4] + board_log[8]) == 3:     # diagonal 1
        if board[0] + board[4] + board[8] == 15:
            return True
    if (board_log[2] + board_log[4] + board_log[6]) == 3:    # diagonal 2
        if board[2] + board[4] + board[6] == 15:
            return True
    if (board_log[0] + board_log[1] + board_log[2]) == 3:    # row 1
        if board[0] + board[1] + board[2] == 15:
            return True
    if (board_log[3] + board_log[4] + board_log[5]) == 3:    # row 2
        if board[3] + board[4] + board[5] == 15:
            return True
    if (board_log[6] + board_log[7] + board_log[8]) == 3:    # row 3
        if board[6] + board[7] + board[8] == 15:
            return True
    if (board_log[0] + board_log[3] + board_log[6]) == 3:    # coloumn 1
        if board[0] + board[3] + board[6] == 15:
            return True
    if (board_log[1] + board_log[4] + board_log[7]) == 3:    # coloumn 2
        if board[1] + board[4] + board[7] == 15:
            return True
    if (board_log[2] + board_log[5] + board_log[8]) == 3:    # coloumn 3
        if board[2] + board[5] + board[8] == 15:
            return True
    else:
        return False


def play_game():
    display_board()
    n_actions = 0
    while n_actions != 9:
        action = get_player_action(1)
        value = get_player_value(1)
        valid_value = check_repeat(value, 1)
        update_game_board(action, valid_value)
        if is_winner():
            print("Player 1 won!")
            break
        n_actions += 1

        if n_actions == 9:
            break

        action = get_player_action(2)
        value = get_player_value(2)
        valid_value = check_repeat(value, 2)
        update_game_board(action, valid_value)
        if is_winner():
            print("Player 2 won!")
            break
        n_actions += 1

    if not is_winner():
        print("Draw! Play again")


play_game()