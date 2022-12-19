#draw some diagrams using the game data (default data for now)
import matplotlib.pyplot as plt
import numpy as np

class Diagram:
    def bar_graph(self):
        win_bot = 10
        win_human = 15
        data = [win_bot, win_human]
        label = ['Bot', 'Human']
        plt.bar(range(len(data)), data, color = 'rgb', tick_label = label)
        plt.title("Win Times")
        plt.savefig('win_times')
        plt.show()

    def pie_graph(self):
        game_times = 25
        win_bot = 10
        win_human = 15
        percentage = np.array([win_bot/game_times, win_human/game_times])
        label = ['Bot','Human']
        plt.pie(percentage, labels = label)
        plt.title("Percentage of Winner")
        plt.savefig('win_percentage')
        plt.show()



