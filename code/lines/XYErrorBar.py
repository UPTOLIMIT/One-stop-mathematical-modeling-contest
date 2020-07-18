import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
x = np.arange(10) / 10
y = (x + 0.1)**2

upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5

plt.errorbar(x, y, xerr=0.1, xlolims=True, label='xlolims=True')
y = (x + 0.1)**3

plt.errorbar(x + 0.6, y, xerr=0.1, xuplims=upperlimits, xlolims=lowerlimits,
             label='subsets of xuplims and xlolims')

y = (x + 0.1)**4
plt.errorbar(x + 1.2, y, xerr=0.1, xuplims=True, label='xuplims=True')

plt.legend()
plt.savefig("./XYErrorBar.png",dpi=600)
plt.show()
