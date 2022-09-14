import unittest
import matplotlib.pyplot as plt
import numpy as np
from numpy.testing import assert_allclose

from mplshared.step import StepFunctionLine


class TestStepFunction(unittest.TestCase):

    def setUp(self):
        plt.cla()
        plt.clf()

    def test_one_step_function(self):
        x = [0, 1, 2, 3, 4]
        y = [0.5, 1, 4, 9, 16]

        sf = StepFunctionLine(x, y, linewidth=3)
        plt.gca().add_line(sf)

        assert_allclose(
            plt.gca().lines[-1].get_data(),
            ([-0.5, -0.5, 0.5, 0.5, 1.5, 1.5, 2.5, 2.5, 3.5, 3.5, 4.5, 4.5],
             [0, 0.5, 0.5, 1, 1, 4, 4, 9, 9, 16, 16, 0])
        )

        plt.grid()
        # plt.show()

    def test_multiply_stepfunction(self):
        x = [0, 1, 2, 3, 4]
        y = [0.5, 1, 4, 9, 16]

        plt.plot(x, y, 'o')
        # plt.step(x, y) # this is not what I want

        sf = StepFunctionLine(x, y, linewidth=3)
        plt.gca().add_line(sf)

        sf2 = 2 * sf
        assert_allclose(sf2.y, [1, 2, 8, 18, 32])
        assert_allclose(sf.y, [0.5, 1, 4, 9, 16])

        sf3 = sf * 3
        assert_allclose(sf3.y, [1.5, 3, 12, 27, 48])
        assert_allclose(sf.y, [0.5, 1, 4, 9, 16])

        plt.grid()
        # plt.show()

    def test_add_to_stepfunction(self):
        x = [0, 1, 2, 3, 4]
        y = [0.5, 1, 4, 9, 16]

        plt.plot(x, y, 'o')
        # plt.step(x, y) # this is not what I want

        sf = StepFunctionLine(x, y, linewidth=3)
        plt.gca().add_line(sf)

        sf2 = 2 + sf
        assert_allclose(sf2.y, [2.5, 3, 6, 11, 18])
        assert_allclose(sf.y, [0.5, 1, 4, 9, 16])


        sf3 = sf + 3
        assert_allclose(sf3.y, [3.5, 4, 7, 12, 19])
        assert_allclose(sf.y, [0.5, 1, 4, 9, 16])

        plt.grid()
        # plt.show()

    def test_add_two_stepfunctions(self):
        x = [0, 1, 2, 3, 4]
        y = [0.5, 1, 4, 9, 16]
        sf = StepFunctionLine(x, y)

        x2 = [0, 1.5, 2, 3, 4]
        y2 = [0.5, 1, 4, 9, 16]
        sf2 = StepFunctionLine(x2, y2)

        actual = sf + sf2
        plt.gca().add_line(actual)

