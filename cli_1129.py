from logic_1129 import Game
from diagram_1129 import Diagram
#from logic_1129 import winner
#from logic_new_new import Game
#from logic_new_new import Human
#from logic_new_new import Bot
#from logic_new_new import 

if __name__ == '__main__':
    game = Game()
    print('lets play tictactoe!')
    player = int(input('enter 1 human_human play, enter 2 human_computer play'))
    if player == 1:
        game.play_human_human()
    elif player == 2:
        game.play_human_computer()
        
    #game.read_game()
    print(game.winner)
    game.add_game()

    diagram = Diagram()
    diagram.bar_graph()
    diagram.pie_graph()



