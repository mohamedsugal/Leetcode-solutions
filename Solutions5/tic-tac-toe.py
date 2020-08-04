test_board = ['O', 'X', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'X']


def display_board(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--- --- ---')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--- --- ---')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])


def play_game():
    display_board(test_board)
    handle_turn()



play_game()




