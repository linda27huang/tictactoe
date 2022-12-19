from flask import Flask
from flask import render_template
from flask import request
from logic_1218 import Game
import time
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/play")
def play():
    print("Initializing game...")
    global game, last_time
    game = Game
    last_time = time.time()
    if request.args.get('playmode') == 'humanhuman':
        game = Game(game_mode=request.args.get('playmode'), start_first=True, player_names=[request.args.get('player1'), request.args.get('player2')])
        return render_template('play.html', player1=request.args.get('player1'), player2=request.args.get('player2'))
    elif request.args.get('playmode') == 'humanbot':
        game = Game(game_mode=request.args.get('playmode'), bot_type=request.args.get('botmode2'), start_first=True, player_names=[request.args.get('player1')])
        return render_template('play.html', player1=request.args.get('player1'), player2=request.args.get('botmode2') + 'Bot')
    
if __name__ == '__main__':
    app.run(debug=True)