import numpy as np
import matplotlib.pyplot as plt


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, label='Men')

ax.set_ylabel('Scores')
ax.set_title('Scores by gender')
ax.legend()
plt.savefig("./SimpleBar.png",dpi=600)
plt.show()