import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
y_pos = np.arange(len(labels))

ax.barh(y_pos, men_means, height=0.4, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(labels)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Men means')
ax.set_title('scores by gender?')

plt.savefig("HorizontalBar.png",dpi=600)
plt.show()