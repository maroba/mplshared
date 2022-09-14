import numpy as np
import matplotlib


class StepFunction(matplotlib.lines.Line2D):

    def __init__(self, x, y, **kwargs):
        baseline = kwargs.get('baseline', 0)
        xdata, ydata = self._convert_data(x, y, baseline)
        super(StepFunction, self).__init__(xdata, ydata, **kwargs)
        self.baseline = baseline
        self._x_input = np.array(x)
        self._y_input = np.array(y)
        self._kwargs = kwargs

    @property
    def x(self):
        return self._x_input

    @property
    def y(self):
        return self._y_input

    def _convert_data(self, x, y, baseline):
        xdata = []
        ydata = []

        idx = 0
        first_idx = 0
        last_idx = len(x) - 1
        for x_, y_ in zip(x, y):
            if idx == first_idx:
                dx = x[1] - x[0]
                xdata.append(x[0] - dx / 2)
                ydata.append(baseline)
                xdata.append(x[0] - dx / 2)
                ydata.append(y[0])
                xdata.append(x[0] + dx / 2)
                ydata.append(y[0])
            elif idx == last_idx:
                dx = x[-1] - x[-2]
                xdata.append(x[-1] - dx / 2)
                ydata.append(y[-1])
                xdata.append(x[-1] + dx / 2)
                ydata.append(y[-1])
                xdata.append(x[-1] + dx / 2)
                ydata.append(baseline)
            else:
                x_left = x[idx - 1] + 0.5 * (x[idx] - x[idx - 1])
                x_right = x[idx] + 0.5 * (x[idx + 1] - x[idx])
                xdata.append(x_left)
                xdata.append(x_right)
                ydata.append(y[idx])
                ydata.append(y[idx])

            idx += 1

        return xdata, ydata

    def __mul__(self, other):
        if isinstance(other, StepFunction):
            raise NotImplementedError('TODO')
        else:
            xdata, ydata = self._x_input, self._y_input
            ydata = ydata.copy()
            for i in range(len(ydata)):
                ydata[i] *= other
            return StepFunction(self._x_input, ydata, **self._kwargs)

    def __rmul__(self, other):
        return self.__mul__(other)