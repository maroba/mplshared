import unittest
import numpy as np
import matplotlib.pyplot as plt

from mplshared.slopes import SlopeLine

np.random.seed(42)


def noisify(arr, amplitude=1):
    noise = (np.random.rand(*arr.shape) - 0.5) * amplitude
    return arr + noise


class TestSlopeLine(unittest.TestCase):

    def test_linear_scale_plot_from_slope_and_through(self):
        x = np.linspace(0, 10, 100)
        y = noisify(2 * x + 3)

        slope_line = SlopeLine(slope=2, through=(x[5], y[5]), domain=(0, 10))

        plt.plot(x, y)
        plt.gca().add_line(slope_line)
        plt.grid()
        plt.show()

    def test_loglog_scale_plot_from_slope_and_through(self):
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
