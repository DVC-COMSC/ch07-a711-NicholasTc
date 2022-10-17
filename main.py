import numpy as np
import matplotlib.pyplot as plt

Math = [100, 90]
English = [90, 80]
Physics = [80, 80]
Computer = [80, 90]
x = np.arange(2) 
width = 0.15
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']

# ******************************
# Make your code
# ******************************

x = np.arange(2)
fig,ax = plt.subplots()
rect1 = ax.bar(x-width/2, Math, width)
rect2 = ax.bar(x+width/2, English, width)
rect3 = ax.bar(x+(3*width)/2, Physics, width)
rect4 = ax.bar(x+(5*width)/2, Computer, width)

ax.legend(labels)
ax.set_title("Grouped graph for scores")
ax.set_xticks(x, names)
ax.bar_label(rect1, padding=3)
ax.bar_label(rect2, padding=3)
ax.bar_label(rect3, padding=3)
ax.bar_label(rect4, padding=3)

plt.show()
fig.savefig('A11.png')
