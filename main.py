import math

# Constants for players and empty spots
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Initialize the board
board = [EMPTY] * 9

# Function to print the board
def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('|'.join(row))
        print('-' * 5)

# Function to check for a win
def check_win(board, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for positions in win_positions:
        if all(board[pos] == player for pos in positions):
            return True
    return False

# Function to check if the board is full (draw)
def is_draw(board):
    return all(spot != EMPTY for spot in board)

# Function to get available moves
def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == EMPTY]

# Minimax function
def minimax(board, depth, is_maximizing):
    if check_win(board, PLAYER_X):
        return -1
    if check_win(board, PLAYER_O):
        return 1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = PLAYER_O
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = PLAYER_X
            score = minimax(board, depth + 1, True)
            board[move] = EMPTY
            best_score = min(score, best_score)
        return best_score

# Function to find the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in available_moves(board):
        board[i] = PLAYER_O
        score = minimax(board, 0, False)
        board[i] = EMPTY
        if score > best_score:
            best_score = score
            move = i
    return move

# Function to play the game
def play_game():
    current_player = PLAYER_X
    while True:
        print_board(board)
        if current_player == PLAYER_X:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == EMPTY:
                board[move] = PLAYER_X
                if check_win(board, PLAYER_X):
                    print_board(board)
                    print("Congrats You have won!")
                    break
                if is_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                current_player = PLAYER_O
            else:
                print("Invalid move. Try again.")
        else:
            move = best_move(board)
            board[move] = PLAYER_O
            if check_win(board, PLAYER_O):
                print_board(board)
                print("AI wins!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = PLAYER_X

# Start the game
play_game()
