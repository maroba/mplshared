import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
from numpy import pi


def start_figure():
    plt.plot()
    fig = plt.gcf()
    ax = plt.gca()
    ax.set_axis_off()
    ax.set_aspect('equal')
    return fig, ax

