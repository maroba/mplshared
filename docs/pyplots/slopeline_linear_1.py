import numpy as np
import matplotlib.pyplot as plt

from mplshared import SlopeLine


def noisify(arr, amplitude=1):
    noise = (np.random.rand(*arr.shape) - 0.5) * amplitude
    return arr + noise


x = np.linspace(0, 10, 100)
y = noisify(2 * x + 3)

slope_line = SlopeLine(slope=2, through=(x[5], y[5]), domain=(0, 10))

plt.plot(x, y)
plt.gca().add_line(slope_line)
plt.grid()
plt.show()
