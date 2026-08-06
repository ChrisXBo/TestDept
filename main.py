def print_board(board):
    print()
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print()


def check_win(board, marker):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    return any(board[a] == board[b] == board[c] == marker for a, b, c in winning_combinations)


def board_full(board):
    return all(space != ' ' for space in board)


def get_player_move(player, board):
    while True:
        choice = input(f"Player {player} ({'X' if player == 1 else 'O'}), choose a position 1-9: ").strip()
        if not choice.isdigit():
            print('Please enter a number between 1 and 9.')
            continue
        position = int(choice) - 1
        if position < 0 or position > 8:
            print('That position is out of range. Try again.')
            continue
        if board[position] != ' ':
            print('That space is already taken. Choose another one.')
            continue
        return position


def play_game():
    board = [' '] * 9
    current_player = 1
    markers = {1: 'X', 2: 'O'}

    print('Welcome to Tic Tac Toe!')
    print('Positions are numbered 1 through 9 like this:')
    print(' 1 | 2 | 3 ')
    print('---+---+---')
    print(' 4 | 5 | 6 ')
    print('---+---+---')
    print(' 7 | 8 | 9 ')

    while True:
        print_board(board)
        position = get_player_move(current_player, board)
        board[position] = markers[current_player]

        if check_win(board, markers[current_player]):
            print_board(board)
            print(f'Player {current_player} ({markers[current_player]}) wins!')
            break

        if board_full(board):
            print_board(board)
            print('The game is a draw.')
            break

        current_player = 2 if current_player == 1 else 1


def main():
    while True:
        play_game()
        again = input('Play again? (y/n): ').strip().lower()
        if again != 'y':
            print('Thanks for playing Tic Tac Toe!')
            break


if __name__ == '__main__':
    main()