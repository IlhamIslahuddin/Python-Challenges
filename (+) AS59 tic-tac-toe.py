import random

def print_board(board):
    for (row) in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def player_move(board):
    while True:
        try:
            row = int(input("Enter row (1, 2, or 3): ")) - 1
            col = int(input("Enter column (1, 2, or 3): ")) - 1
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("That spot is already taken!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 3.")

def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = "O"
            break

def main():
    board = [[" "]*3 for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        print("Computer's turn...")
        computer_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("Sorry, you lose!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
