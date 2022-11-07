#This is where game logic lives. No input

def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

def get_winner(board):
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2] == 'x':  # check rows x
            return 'x'
        elif board[x][0] == board[x][1] == board[x][2] == 'o': # check rows o
            return 'o'
        elif board[0][x] == board[1][x] == board[2][x] == 'x':  # check cols x
            return 'x'
        elif board[0][x] == board[1][x] == board[2][x] == 'o':  # check cols o
            return 'o'
    if board[0][0] == board[1][1] == board[2][2] == 'x':    # check diagonals x 
        return 'x'
    elif board[0][2] == board[1][1] == board[2][0] == 'x':
        return 'x'
    if board[0][0] == board[1][1] == board[2][2] == 'o':    # check diagonals o
        return 'o'
    elif board[0][2] == board[1][1] == board[2][0] == 'o':
        return 'o'
    else:
        return None 

def announce_winner(winner):
    res = ""
    if winner == 'x':
        res = 'X win!'
    elif winner == 'o':
        res = 'O win!'
    else:
        res = 'draw'
    print(res)
    return res

def other_player(player):
    return '0' # FIXME

