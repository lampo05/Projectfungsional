import random


def create_board(width, character_fn=lambda i, j: ' '):
    return [[character_fn(i, j) for j in range(width)] for i in range(width)]



def print_board(board, player_pos, goal_pos):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i, j) == player_pos:
                print('A', end=' ')
            elif (i, j) == goal_pos:
                print('O', end=' ')

            else:
                print(board[i][j], end=' ')
        print()


def is_valid_move(move, player_pos, board):
    x, y = player_pos
    new_x, new_y = x, y

    if move == 'w':
        new_x = x - 1
    elif move == 's':
        new_x = x + 1
    elif move == 'a':
        new_y = y - 1
    elif move == 'd':
        new_y = y + 1

    return 0 <= new_x < len(board) and 0 <= new_y < len(board) and board[new_x][new_y] != 'O'


def play_game(width):
    board = create_board(width)
    player_pos = (random.randint(0, width - 1), random.randint(0, width - 1))
    goal_pos = (random.randint(0, width - 1), random.randint(0, width - 1))

    while player_pos != goal_pos:
        print_board(board, player_pos, goal_pos)
        move = input("Enter move (w/a/s/d): ").lower()

        if move in ['w', 'a', 's', 'd']:
            if is_valid_move(move, player_pos, board):
                x, y = player_pos
                board[x][y] = ' '

                if move == 'w':
                    player_pos = (x - 1, y)
                elif move == 's':
                    player_pos = (x + 1, y)
                elif move == 'a':
                    player_pos = (x, y - 1)
                elif move == 'd':
                    player_pos = (x, y + 1)

                board[player_pos[0]][player_pos[1]] = 'A'
            else:
                print("Invalid move. Try again.")
        else:
            print("Invalid input. Use 'w', 'a', 's', or 'd'.")

    print_board(board, player_pos, goal_pos)
    print("You win!")


if __name__ == '__main__':
    try:
        width = int(input("Enter the width of the board: "))
        play_game(width)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the board width.")
