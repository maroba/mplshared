import matplotlib as mpl


class SlopeLine(mpl.lines.Line2D):

    def __init__(self, slope, through, domain, scale='linear', style=None):

        style = style or {
            'color': '#505050', 'dashes': (5, 2, 5, 2)
        }

        x0, y0 = through
        x_from, x_to = domain

        if scale == 'loglog':
            if x0 == 0 or y0 == 0 or x_from == 0 or x_to == 0:
                raise ValueError('0 encountered for loglog plot')

        func = self.slope_function(scale, slope, x0, y0)

        super().__init__(
            [x_from, x_to],
            [func(x_from), func(x_to)],
            **style)

    def slope_function(self, scale, slope, x0, y0):
        if scale == 'linear':
            def func(x):
                return slope * (x - x0) + y0
        elif scale == 'loglog':
            def func(x):
                return y0 * (x / x0) ** slope
        else:
            raise NotImplementedError('Invalid scale parameter: %s' % scale)
        return func


