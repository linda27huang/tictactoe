#This is where game logic lives. No input
import random

class Game: 
    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])   
    
#class Human:  #definite human move

    def get_human_move(self):
        while True:
            move_1 = input("which row (choose 1,2,3)")
            if int(move_1) == 1 or int(move_1) == 2 or int(move_1) == 3:
                break
        while True:
            move_2 = input("which colunm (choose 1,2,3)")
            if int(move_2) == 1 or int(move_2) == 2 or int(move_2) == 3:
                break
        #self.board[int(move_x_1) - 1][int(move_x_2) - 1] = 'x'
        return [int(move_1) - 1, int(move_2) - 1]

#class Bot:   #definie robot move    

    def get_computer_move(self):
        move_1 = random.randint(0,2)
        move_2 = random.randint(0,2)
        return [move_1, move_2]   

#class Game:
    #def __init__(self):
        #self.board = Board()
        #self.players = []


    def get_winner(self,win_char):
        board = self.board
        for x in range(3):
            if board[x][0] == board[x][1] == board[x][2] == win_char:  # check rows x
                return win_char
            elif board[0][x] == board[1][x] == board[2][x] == win_char:  # check cols x
                return win_char
        if board[0][0] == board[1][1] == board[2][2] == win_char:    # check diagonals x 
            return win_char
        elif board[0][2] == board[1][1] == board[2][0] == win_char:
            return win_char
        else:
            return None 

    def play_human_human(self):
        winner = None
        number = 0
        while winner == None and number < 9:
            print("X turn!")
            self.print_board()
            x,y = self.get_human_move()
            if self.board[x][y] != None:
                continue
            self.board[x][y] = 'x'


            if self.get_winner('x'):
                print('cool! player X win')
                break

            print("O turn!")
            self.print_board()                         
            x,y = self.get_human_move()
            if self.board[x][y] != None:
                continue                      
            self.board[x][y] = 'o'
            if self.get_winner('o'):
                print('cool! player O wins')
                break

            number = number + 2

            if winner != None:
                break  
            if number > 8:
                print('draw') 


    def play_human_computer(self):
        winner = None
        number = 0
        while winner == None and number < 9:
            print("X turn!")
            self.print_board()
            x,y = self.get_human_move()
            if self.board[x][y] != None:
                continue    
            self.board[x][y] = 'x'
            if self.get_winner('x'):
                print('cool! your win')
                break
            x,y = self.get_computer_move()
            print("O turn!")
            if self.board[x][y] != None:
                continue             
            self.board[x][y] = 'o'
            if self.get_winner('o'):
                print('sorry! computer wins')
                break
            number = number + 2
            if number > 8:
                print('draw') 
       
            