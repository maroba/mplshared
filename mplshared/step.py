import numbers

import matplotlib
import numpy as np


class StepFunction:
    """Represents a step function.

       Can be added and multiplied.
    """

    def __init__(self, x, y):
        self._x = np.array(x)
        self._y = np.array(y)
        self.bins = self._get_bins(x)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __call__(self, x):
        """Returns the value of the step function at x.

        Parameters
        ----------
        x : float
            where to evaluate the function.
        Returns
        -------
        out: float
            the function value at x.
        """
        for bin, y in zip(self.bins, self._y):
            x_from, x_to = bin
            if x_from <= x <= x_to:
                return y
        raise ValueError("Value %s not in domain of StepFunction instance." % x)

    def __add__(self, other):
        if isinstance(other, numbers.Real):
            return StepFunction(self.x, self.y + other)
        elif isinstance(other, StepFunction):
            sf_left = self.expand_partition(other.x)
            sf_right = other.expand_partition(self.x)
            return StepFunction(sf_left.x, sf_left.y + sf_right.y)
        else:
            raise TypeError('Cannot add type %s to StepFunction' % other.__class__.__name__)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return StepFunction(self.x, self.y * other)
        elif isinstance(other, StepFunction):
            sf_left = self.expand_partition(other.x)
            sf_right = other.expand_partition(self.x)
            return StepFunction(sf_left.x, sf_left.y * sf_right.y)
        else:
            raise TypeError('Cannot multiply type %s to StepFunction' % other.__class__.__name__)

    def expand_partition(self, x_additional):
        merged_x = set(self.x)
        merged_x.update(x_additional)
        new_x = []
        new_y = []
        for x in sorted(list(merged_x)):
            new_x.append(x)
            new_y.append(self(x))
        return StepFunction(new_x, new_y)

    def _get_bins(self, x):
        dx = x[1] - x[0]
        bins = []
        first_bin = (x[0] - dx / 2, x[0] + dx / 2)
        bins.append(first_bin)
        for i in range(1, len(x)-1):
            x_from = x[i] -  0.5*(x[i] - x[i-1])
            x_to = x[i] + 0.5 * (x[i+1] - x[i])
            bins.append((x_from, x_to))
        dx = x[-1] - x[-2]
        last_bin = (x[-1] - dx/2, x[-1] + dx/2)
        bins.append(last_bin)
        return bins


class StepFunctionLine(matplotlib.lines.Line2D):
    """A matplotlib line representing a piecewise constant function.
       Can take part in arithmetic operations like multiplication and addition.
    """

    def __init__(self, x, y, **kwargs):
        """Constructor

        Parameters
        ----------
        x : arraylike (1D)
            The grid values (bin centers for the horizontal axis).
        y : arraylike (1D)
            The values for the vertical axis.
        kwargs
            Keyword arguments. Same as for matplotlib.lines.Lines2D
        """
        baseline = kwargs.get('baseline', 0)
        stepfunc = StepFunction(x, y)
        # Add additional points to correctly plot a step function:
        xdata, ydata = self._convert_data(stepfunc, baseline)
        super(StepFunctionLine, self).__init__(xdata, ydata, **kwargs)
        self.baseline = baseline
        self.stepfunc = stepfunc
        self._kwargs = kwargs

    @property
    def x(self):
        """Returns the x-data (centers of bins)."""
        return self.stepfunc.x

    @property
    def y(self):
        """Return the y-data for each bin."""
        return self.stepfunc.y

    def __call__(self, x):
        return self.stepfunc(x)

    def autolims(self, plt):
        if not self.axes:
            return
        self.axes.relim()
        self.axes.autoscale_view()
        plt.draw()

    def setp(self, **kwargs):
        matplotlib.artist.setp(self, **kwargs)
        self._kwargs = kwargs

    def _convert_data(self, stepfunc, baseline):
        xdata = []
        ydata = []

        idx = 0
        first_idx = 0
        last_idx = len(stepfunc.x) - 1
        for x_, y_, bin_ in zip(stepfunc.x, stepfunc.y, stepfunc.bins):
            if idx == first_idx:
                xdata.append(bin_[0])
                ydata.append(baseline)
                xdata.append(bin_[0])
                ydata.append(y_)
                xdata.append(bin_[1])
                ydata.append(y_)
            elif idx == last_idx:
                xdata.append(bin_[0])
                ydata.append(y_)
                xdata.append(bin_[1])
                ydata.append(y_)
                xdata.append(bin_[1])
                ydata.append(baseline)
            else:
                xdata.append(bin_[0])
                xdata.append(bin_[1])
                ydata.append(y_)
                ydata.append(y_)
            idx += 1

        return xdata, ydata

    def __mul__(self, other):
        if isinstance(other, StepFunctionLine):
            new_stepfunc = self.stepfunc.__mul__(other.stepfunc)
        else:
            new_stepfunc = self.stepfunc.__mul__(other)
        return StepFunctionLine(new_stepfunc.x, new_stepfunc.y, **self._kwargs)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if isinstance(other, StepFunctionLine):
            new_stepfunc = self.stepfunc.__add__(other.stepfunc)
        else:
            new_stepfunc = self.stepfunc.__add__(other)
        return StepFunctionLine(new_stepfunc.x, new_stepfunc.y, **self._kwargs)

    def __radd__(self, other):
        return self.__add__(other)
