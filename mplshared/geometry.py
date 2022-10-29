import matplotlib as mpl
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np
from IPython.core.display_functions import display
from matplotlib.artist import Artist
from matplotlib.patches import Arrow, FancyArrow, Arc, Rectangle
from numpy import pi

ORIGIN = np.zeros(2)
UP = np.array([0, 1])
DOWN = -UP
RIGHT = np.array([1, 0])
LEFT = -RIGHT


class Drawing:

    def __init__(self):
        self.fig = plt.figure(figsize=(12, 12))
        ax = plt.axes()
        ax.plot()
        ax.set_axis_off()
        ax.set_aspect('equal')
        self.ax = ax

    def add(self, *shapes, plane=1):
        for shape in shapes:
            shape.add_to_axes(self.ax, plane)

    def remove(self, *shapes):
        for shape in shapes:
            try:
                shape.remove()
            except:
                pass  # already removed

    def show(self):
        return display(self.fig)


class Group:

    def __init__(self, *shapes):
        self.shapes = list(shapes)

    def add(self, *shapes):
        self.shapes.extend(list(shapes))

    def add_to_axes(self, ax, plane=1):
        for shape in self.shapes:
            shape.add_to_axes(ax, plane)

    def remove(self):
        for shape in self.shapes:
            shape.remove()


class PatchMixin:

    def add_to_axes(self, ax, plane=1):
        self.patch.set_zorder = plane
        ax.add_patch(self.patch)

    def remove(self):
        self.patch.remove()


class TextMixin:

    def add_to_axes(self, ax, plane=1):
        self.patch = ax.text(*self.xy, self.text, **self.kwargs)
        self.patch.set_zorder = plane

    def remove(self):
        Artist.remove(self.patch)


class Shape:
    linewidth = 0.001


class Point(Shape, PatchMixin):
    size = 0.03
    color = 'k'

    def __init__(self, xy, **kwargs):
        self.xy = np.array(xy)
        if 'color' not in kwargs:
            kwargs['color'] = Point.color
        self.kwargs = kwargs
        self.patch = mpl.patches.Circle(self.xy, Point.size, **self.kwargs)


class Circle(Shape, PatchMixin):

    def __init__(self, xy, radius=1):
        super().__init__()
        self.xy = xy
        self.radius = radius
        self.patch = mpl.patches.Circle(self.xy, self.radius, fill=False, color='k')


class Line(Shape, PatchMixin):

    def __init__(self, start, end, **kwargs):
        self.kwargs = kwargs
        self.start = start
        self.end = end
        self.patch = self._make_patch()

    def _make_patch(self):
        Path = mpath.Path
        path_data = [
            (Path.MOVETO, self.start),
            (Path.LINETO, self.end),
        ]
        codes, verts = zip(*path_data)
        path = mpath.Path(verts, codes)
        return mpl.patches.PathPatch(path, **self.kwargs)


class Vector(Shape, PatchMixin):
    linewidth = 0.005
    head_width = 0.035
    head_length = 0.075
    color = 'k'

    def __init__(self, start, end, **kwargs):

        self.start = start
        self.end = end
        dxy = self.end - self.start
        if 'width' not in kwargs:
            kwargs['width'] = Vector.linewidth
        if 'color' not in kwargs:
            kwargs['color'] = Vector.color
        # kwargs['mutation_scale'] = 100
        kwargs['length_includes_head'] = True
        kwargs['head_width'] = Vector.head_width
        kwargs['head_length'] = Vector.head_length
        self.kwargs = kwargs

        self.patch = FancyArrow(*self.start, *dxy, **kwargs)


class Text(Shape, TextMixin):
    fontsize = 14

    def __init__(self, text, xy, **kwargs):
        self.text = text
        self.xy = xy
        if 'fontsize' not in kwargs:
            kwargs['fontsize'] = Text.fontsize
        if 'horizontalalignment' not in kwargs:
            kwargs['horizontalalignment'] = 'center'
        if 'verticalalignment' not in kwargs:
            kwargs['verticalalignment'] = 'center'
        self.kwargs = kwargs


class AngleMarker(Shape, PatchMixin):

    def __init__(self, xy, radius, angles=None, between=None, **kwargs):
        if angles:
            start_angle_deg, end_angle_deg = angles
        elif between:
            v1, v2 = between
            angle = angle_between(v1, v2)
            start_angle_deg = get_polar(v1)
            end_angle_deg = start_angle_deg + angle
        self.patch = Arc(
            xy, 2 * radius, 2 * radius, theta1=start_angle_deg, theta2=end_angle_deg,
            **kwargs
        )


class RightAngleMarker(Shape, PatchMixin):
    def __init__(self, xy, size, angle, **kwargs):
        self.patch = Rectangle(xy, size, size, angle, fill=False, **kwargs)


def rotate(xy, angle):
    a = deg2rad(angle)
    return np.array([
        np.cos(a) * xy[0] - np.sin(a) * xy[1],
        np.sin(a) * xy[0] + np.cos(a) * xy[1]
    ])


def rad2deg(*rads):
    degs = [rad / pi * 180 for rad in rads]
    if len(degs) == 1:
        return degs[0]
    return tuple(degs)


def deg2rad(*degs):
    rads = [deg * pi / 180. for deg in degs]
    if len(rads) == 1:
        return rads[0]
    return tuple(rads)


def dot(a, b):
    return np.dot(a, b)


def norm(a):
    return np.sqrt(dot(a, a))


def normalize(a):
    return a / norm(a)


def angle_between(v1, v2):
    angle = np.arccos(dot(v1, v2) / norm(v1) / norm(v2))
    if get_polar(v1) > get_polar(v2):
        angle = 2 * pi - angle
    return rad2deg(angle)


def polar(deg=None, rad=None, r=1):
    if deg is not None and rad is not None:
        raise ValueError('Either rad or deg must be given, not both.')
    if deg is None and rad is None:
        raise ValueError('Either rad or deg must be given.')
    if deg is not None:
        rad = deg2rad(deg)
    return r * np.array([np.cos(rad), np.sin(rad)])


def get_polar(v):
    x, y = v
    if x == 0:
        if y > 0:
            angle = pi / 2
        else:
            angle = 3 * pi / 2
    else:
        angle = np.arctan(abs(y / x))
        if x < 0 and y >= 0:
            angle = pi - angle
        elif x < 0 and y < 0:
            angle += pi
        elif x > 0 and y < 0:
            angle = 2 * pi - angle
    return rad2deg(angle)
