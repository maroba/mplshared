mplshared
=========

Some tools for matplotlib.

Installation
------------

.. code-block::
    pip install --upgrade mplshared


Usage
-----

Slope Lines
:::::::::::

Linear Plots
------------

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


Double Logarithmic Plots
------------------------

If you have a loglog plot, just change the scale argument:

.. code-block:: ipython

    slope_line = SlopeLine(slope=2,
                       through=(x[40], y[40]),
                       domain=(1, 100),
                       scale='loglog',
                       style={'color': 'red'}
                       )


.. image:: docs/pyplots/slopeline_loglog.png
