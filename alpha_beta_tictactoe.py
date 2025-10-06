import math

# ----------- Step 1: Representing the board -----------
board = [" " for _ in range(9)]

# ----------- Step 2: Helper Functions -----------

def print_board():
    """Display the board in a 3x3 format."""
    for i in range(0, 9, 3):
        row = board[i:i+3]
        print(f"| {row[0]} | {row[1]} | {row[2]} |")

def check_winner(brd):
    """Check if there is a winner or if it's a tie."""
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for pattern in win_patterns:
        if brd[pattern[0]] == brd[pattern[1]] == brd[pattern[2]] != " ":
            return brd[pattern[0]]
    if " " not in brd:
        return "Tie"
    return None

def available_moves(brd):
    """Return a list of available cell indices."""
    return [i for i in range(9) if brd[i] == " "]

# ----------- Step 3: Minimax with Alpha-Beta + Debug -----------

def minimax_alpha_beta(brd, is_maximizing, alpha, beta, depth=0):
    """Recursive minimax algorithm with alpha-beta pruning and debug info."""
    result = check_winner(brd)
    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Tie":
        return 0

    indent = "  " * depth  # indentation for readability

    if is_maximizing:
        max_eval = -math.inf
        for move in available_moves(brd):
            brd[move] = "O"
            print(f"{indent}Maximizer trying move {move} | alpha={alpha}, beta={beta}")
            eval = minimax_alpha_beta(brd, False, alpha, beta, depth+1)
            brd[move] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            print(f"{indent}→ Updated alpha={alpha}, beta={beta}, eval={eval}")

            if beta <= alpha:
                print(f"{indent}❌ Pruned at move {move} (beta <= alpha)")
                break
        return max_eval

    else:
        min_eval = math.inf
        for move in available_moves(brd):
            brd[move] = "X"
            print(f"{indent}Minimizer trying move {move} | alpha={alpha}, beta={beta}")
            eval = minimax_alpha_beta(brd, True, alpha, beta, depth+1)
            brd[move] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            print(f"{indent}→ Updated alpha={alpha}, beta={beta}, eval={eval}")

            if beta <= alpha:
                print(f"{indent}❌ Pruned at move {move} (beta <= alpha)")
                break
        return min_eval

# ----------- Step 4: AI Move Selection -----------

def best_move_alpha_beta():
    """Find the best move for AI using alpha-beta pruning."""
    best_score = -math.inf
    move_chosen = None
    alpha, beta = -math.inf, math.inf

    print("\n--- AI is thinking... ---")
    for move in available_moves(board):
        board[move] = "O"
        print(f"\nEvaluating move {move}:")
        score = minimax_alpha_beta(board, False, alpha, beta)
        board[move] = " "
        print(f"Move {move} resulted in score {score}\n")

        if score > best_score:
            best_score = score
            move_chosen = move

    print(f"AI chose move {move_chosen} with score {best_score}")
    return move_chosen

# ----------- Step 5: Main Game Loop -----------

def play_game():
    print("Welcome to Tic Tac Toe (Alpha-Beta Debug Mode)!")
    print_board()

    while True:
        # Human turn
        move = int(input("Enter your move (0-8): "))
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue
        board[move] = "X"

        if check_winner(board):
            print_board()
            print(f"Game Over! Result: {check_winner(board)}")
            break

        # AI turn
        ai_move = best_move_alpha_beta()
        board[ai_move] = "O"

        print("\nAI made its move:")
        print_board()

        if check_winner(board):
            print(f"Game Over! Result: {check_winner(board)}")
            break

# ----------- Run the game -----------
play_game()
