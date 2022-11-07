from logic import make_empty_board
from logic import get_winner
from logic import announce_winner

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    while winner == None:
        print("X turn!")
        # print(board)
        for i in range(len(board)):
            print(board[i])
        #move_x_1 = input("which row (1,2,3)")
        while True:
            move_x_1 = input("which row (1,2,3)")
            if int(move_x_1) == 1 or int(move_x_1) == 2 or int(move_x_1) == 3:
                break
        while True:
            move_x_2 = input("which colunm (1,2,3)")
            if int(move_x_2) == 1 or int(move_x_2) == 2 or int(move_x_2) == 3:
                break
        board[int(move_x_1) - 1][int(move_x_2) - 1] = 'x'
        winner = get_winner(board)
        if winner != None:
            break
        print('O turn!')
        #print(board)
        for i in range(len(board)):
            print(board[i])
        while True:
            move_o_1 = input("which row (1,2,3)")
            if int(move_o_1) == 1 or int(move_o_1) == 2 or int(move_o_1) == 3:
                break
        while True:
            move_o_2 = input("which colunm (1,2,3)")
            if int(move_o_2) == 1 or int(move_o_2) == 2 or int(move_o_2) == 3:
                break
        #move_o_1 = input("which row")
        #move_o_2 = input("which colunm")
        board[int(move_o_1) - 1][int(move_o_2) - 1] = 'o'
        winner = get_winner(board)

        #TODO: Show the board to the user.
        #TODO: Input a move from the player.
        #TODO: Update the a board.
        #TODO: Update who's turn it is.
        #winner = 'X'# FIXME
    
    announce_winner(winner)