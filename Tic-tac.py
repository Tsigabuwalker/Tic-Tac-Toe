def print_board(board):
    """Prints the current state of the board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board):
    """Checks for a winner in the current board state."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    """Checks if the board is full (draw condition)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize an empty board
    player = "X"  # Start with player X

    while True:
        print_board(board)  # Display the board
        print(f"Player {player}'s turn. Enter row and column (0, 1, or 2) separated by space:")
        
        # Input handling
        try:
            row, col = map(int, input().strip().split())
            if board[row][col] != " ":
                print("This position is already taken. Choose another.")
                continue
            board[row][col] = player  # Place the player's mark
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers (0, 1, or 2).")
            continue

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()