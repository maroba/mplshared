mplshared
=========

Some tools for matplotlib.

|PyPI version fury.io| |PyPI license|

.. |PyPI version fury.io| image:: https://badge.fury.io/py/mplshared.svg
   :target: https://pypi.python.org/pypi/mplshared/

.. |PyPI license| image:: https://img.shields.io/pypi/l/mplshared.svg
   :target: https://pypi.python.org/pypi/mplshared/



Usage
-----

.. code-block::

    pip install --upgrade mplshared


Slope Lines
:::::::::::

In plots with linearly scaling axes:


.. code-block:: ipython

    import matplotlib.pyplot as plt
    from mplshared import SlopeLine

    # Get some random data:
    x = np.linspace(0, 10, 100)
    y = noisify(2 * x + 3)

    # Plot it:
    plt.plot(x, y)

    # Add a slope line:

    slope_line = SlopeLine(slope=2, through=(x[5], y[5]), domain=(0, 10))
    plt.gca().add_line(slope_line)
    plt.show()


.. image:: docs/pyplots/slopeline_linear.png
    :width: 600
    :align: center


If you have a loglog plot, just change the scale argument:

.. code-block:: ipython

    slope_line = SlopeLine(slope=2,
                       through=(x[40], y[40]),
                       domain=(1, 100),
                       scale='loglog',
                       style={'color': 'red'}
                       )


.. image:: docs/pyplots/slopeline_loglog.png
    :width: 600
    :align: center


StepFunctionLine
----------------

.. code-block:: ipython

    import numpy as np
    import matplotlib.pyplot as plt

    from mplshared import StepFunctionLine

    x = np.linspace(-3, 3, 20)
    y = np.sin(x)

    sf1 = StepFunctionLine(x, y, linewidth=3, color='red')
    plt.gca().add_line(sf1)
    sf1.autolims(plt)
    plt.show()


.. image:: docs/pyplots/stepfunction_1.png
    :width: 600
    :align: center
