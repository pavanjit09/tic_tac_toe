def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    for _ in range(9):
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                return
            turn += 1
        else:
            print("Cell already taken, try again.")
    
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    main()

