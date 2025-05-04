import time
import math
import copy

# Constants
HUMAN = 'O'
AI = 'X'
EMPTY = ' '

# Initialize board
def init_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

# Print board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check winner
def check_winner(board):
    for player in [HUMAN, AI]:
        # Rows and Columns
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or \
               all(board[j][i] == player for j in range(3)):
                return player
        # Diagonals
        if all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3)):
            return player
    # Tie
    if all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
        return 'Tie'
    return None

# Get available moves
def get_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

# Minimax Algorithm
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == AI:
        return 1, None
    elif winner == HUMAN:
        return -1, None
    elif winner == 'Tie':
        return 0, None

    best_score = -math.inf if is_maximizing else math.inf
    best_move = None

    for move in get_moves(board):
        i, j = move
        board[i][j] = AI if is_maximizing else HUMAN
        score, _ = minimax(board, not is_maximizing)
        board[i][j] = EMPTY

        if is_maximizing:
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move

    return best_score, best_move

# Alpha-Beta Pruning
def alphabeta(board, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == AI:
        return 1, None
    elif winner == HUMAN:
        return -1, None
    elif winner == 'Tie':
        return 0, None

    best_move = None

    if is_maximizing:
        max_eval = -math.inf
        for move in get_moves(board):
            i, j = move
            board[i][j] = AI
            eval, _ = alphabeta(board, False, alpha, beta)
            board[i][j] = EMPTY
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in get_moves(board):
            i, j = move
            board[i][j] = HUMAN
            eval, _ = alphabeta(board, True, alpha, beta)
            board[i][j] = EMPTY
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

# Compare performance
def compare_algorithms():
    board = init_board()
    print("Initial board:")
    print_board(board)

    print("\nRunning Minimax...")
    start = time.time()
    _, move1 = minimax(copy.deepcopy(board), True)
    end = time.time()
    print(f"Minimax move: {move1}, Time taken: {end - start:.6f} seconds")

    print("\nRunning Alpha-Beta Pruning...")
    start = time.time()
    _, move2 = alphabeta(copy.deepcopy(board), True, -math.inf, math.inf)
    end = time.time()
    print(f"Alpha-Beta move: {move2}, Time taken: {end - start:.6f} seconds")

compare_algorithms()
