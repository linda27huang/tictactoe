# This is the file contains the Command Line Interface(CLI) for the game
import unittest
import logic

class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['x', None, 'o'],
            ['x', None, None],
            ['x', 'o', 'x']
        ]
        
        self.assertEqual(logic.get_winner(board),'x')

    def test_make_empty_board(self):
        board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
        ]
        self.assertEqual(logic.make_empty_board(),board)     

    def test_announce_winner(self):
        winner = 'x'
        winner = 'o'
        self.assertEqual(logic.announce_winner(winner),'O win!')  
        #self.assertEqual(logic.announce_winner(winner),print('O win!'))          
    # TODO: test all functions from logic.py

if __name__ == '__main__':
    unittest.main()