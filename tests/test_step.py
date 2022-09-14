import unittest
import matplotlib.pyplot as plt
import numpy as np

from mplshared.step import StepFunction


class TestStepFunction(unittest.TestCase):

    def test_one_step_function(self):
        x = [0, 1, 2, 3, 4]
        y = [0.5, 1, 4, 9, 16]

        plt.plot(x, y, 'o')
        #plt.step(x, y) # not what I want

        sf = StepFunction(x, y, linewidth=3)
        plt.gca().add_line(sf)

        plt.grid()
        plt.show()
