import unittest

import matplotlib.pyplot as plt
import numpy as np
from numpy.testing import assert_array_almost_equal, assert_allclose

from mplshared.slopes import SlopeLine


def noisify(arr, amplitude=1):
    np.random.seed(42)
    noise = (np.random.rand(*arr.shape) - 0.5) * amplitude
    return arr + noise


class TestSlopeLine(unittest.TestCase):

    def setUp(self):
        plt.cla()
        plt.clf()

    def test_linear_scale_plot_from_slope_and_through(self):
        x = np.linspace(0, 10, 100)
        y = noisify(2 * x + 3)

        slope_line = SlopeLine(slope=2, through=(x[5], y[5]), domain=(0, 10))

        plt.plot(x, y)
        plt.gca().add_line(slope_line)
        plt.grid()
        actual_line = plt.gca().lines[1]
        assert isinstance(actual_line, SlopeLine)
        xdata, ydata = actual_line.get_data()
        assert [0, 10] == xdata
        assert_array_almost_equal([2.656, 22.656], ydata, decimal=3)
        #plt.show()

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

        actual_line = plt.gca().lines[1]
        assert isinstance(actual_line, SlopeLine)
        xdata, ydata = actual_line.get_data()
        assert_array_almost_equal([1, 100], xdata)
        assert_allclose([9.909e-01, 9.909e+03], ydata, rtol=1.E-4)
        #plt.show()
