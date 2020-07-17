import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
y = np.sin(x)

fig, ax = plt.subplots()

# Using set_dashes() to modify dashing of an existing line
line1, = ax.plot(x, y, label='Using set_dashes()')
line1.set_dashes([2, 2, 10, 2])  # 空间长度：2个点线长，2个点分隔，10个点线长，2个点分隔

# Using plot(..., dashes=...) to set the dashing when creating a line
line2, = ax.plot(x, y - 0.2, dashes=[6, 2, 2, 4], #空间长度：6个点线长，2个点分隔,2个点线长,4个点分隔
                 label='Using the dashes parameter')

ax.legend()
plt.savefig("./CustomizeLineStyle.png",dpi=600)
plt.show()