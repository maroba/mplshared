import numpy as np
import matplotlib.pyplot as plt

from mplshared import SlopeLine


def noisify(arr, amplitude=1):
    noise = (np.random.rand(*arr.shape) - 0.5) * amplitude
    return arr + noise


x = np.logspace(0, 2, 100)
y = noisify(x ** 2, amplitude=1)

slope_line = SlopeLine(slope=2,
                       through=(x[40], y[40]),
                       domain=(1, 100),
                       scale='loglog',
                       style={'color': 'red'}
                       )

plt.loglog(x, y)
plt.gca().add_line(slope_line)
plt.grid()
plt.show()
