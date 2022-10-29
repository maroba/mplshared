import unittest
import matplotlib.pyplot as plt
from mplshared import Drawing, Point, LineSegment, Vector, Shape, AngleMarker, RightAngleMarker


class TestGeometry(unittest.TestCase):

    def test_drawing_with_two_points_and_linesegment(self):
        d = Drawing()
        point_1 = Point(0.2, 0.2)
        d.add(point_1)
        point_2 = Point(0.3, 0.3)
        d.add(point_2)
        d.add(LineSegment(point_1, point_2, linestyle='--'))
        plt.show()

    def test_two_vectors(self):
        d = Drawing()
        Shape.linewidth *= 2
        start = Point(0, 0)
        end = Point(1, 1)
        v1 = Vector(start, end)
        v2 = Vector(v1.end, Point(0, 2))
        d.add(v1)
        d.add(v2)
        plt.show()

    def test_labeling(self):
        d = Drawing()
        origin = Point(0, 0)
        a = Vector(origin, Point(0.3, 0.2))
        a.annotate(r'$\vec a$', 0.03, a.right)
        b = Vector(origin, Point(0.2, 0.4))
        b.annotate(r'$\vec b$', 0.03, b.left)
        d.add(a)
        d.add(b)
        plt.show()

    def test_projection(self):
        d = Drawing()
        origin = Point(0, 0)
        b = Vector(origin, Point(0.3, 0.2))
        a = Vector(origin, Point(0.2, 0.4))

        perp = LineSegment.perpendicular(b.end, a, linestyle='--')
        d.add(a)
        d.add(b)
        d.add(perp)
        plt.show()

    def test_projection_with_labelled_marker(self):
        d = Drawing()
        Shape.fontsize = 16
        origin = Point(0, 0)
        b = Vector(origin, Point(0.3, 0.2))
        a = Vector(origin, Point(0.2, 0.4))

        a.annotate(r'$\vec b$', 0.03, a.left)
        b.annotate(r'$\vec a$', 0.03, b.right)

        perp = LineSegment.perpendicular(b.end, a, linestyle='--')
        angle = AngleMarker(perp.end, 0.09, -perp, a)
        angle.annotate(r'$\alpha$', 0.016)
        d.add(a)
        d.add(b)
        d.add(perp)
        d.add(angle)
        plt.show()

    def test_projection_with_marker(self):
        d = Drawing()
        Shape.fontsize = 16
        origin = Point(0, 0)
        b = Vector(origin, Point(0.3, 0.2))
        a = Vector(origin, Point(0.2, 0.4))

        a.annotate(r'$\vec b$', 0.03, a.left)
        b.annotate(r'$\vec a$', 0.03, b.right)

        perp = LineSegment.perpendicular(b.end, a, linestyle='--')
        angle = RightAngleMarker(perp.end, 0.04, -perp, a)

        d.add(a)
        d.add(b)
        d.add(perp)
        d.add(angle)
        plt.show()