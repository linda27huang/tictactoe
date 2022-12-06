import matplotlib.pyplot as plt

win_bot = 10
win_human = 15
data = [win_bot, win_human]
labels = ['Bot', 'Human']
plt.bar(range(len(data)), data, color = 'rgb', tick_label = labels)
plt.savefig('win_times')
plt.show()




