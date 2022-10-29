import pytest
from matplotlib import pyplot as plt

from mplshared import Drawing, ORIGIN, Point, Circle, Text, Line, RIGHT, UP, Vector, Group, AngleMarker, DOWN, LEFT, \
    rotate, polar, angle_between, get_polar


def test_raindrop():
    d = Drawing()
    Point.size = 0.02

    phi_A = 70
    phi_B = 200
    beta_A = 20

    circle = Circle(ORIGIN, 1)
    A = polar(deg=phi_A)
    point_A = Point(A)
    label_A = Text('A', xy=A + 0.1 * polar(75))
    origin = Point(ORIGIN)
    lbl_origin = Text('O', ORIGIN + 0.1 * polar(270))

    coord_sys = Group(
        Vector(ORIGIN, 1.2 * UP, color='darkgray'),
        Vector(ORIGIN, 1.2 * RIGHT, color='darkgray'),
        Text('x', 1.2 * RIGHT + 0.1 * DOWN, color='darkgray'),
        Text('y', 1.2 * UP + 0.1 * LEFT, color='darkgray')
    )

    phi_A_group = Group(
        Line(ORIGIN, A, linestyle='dashed'),
        AngleMarker(ORIGIN, 0.3, angles=(0, phi_A)),
        Text(r'$\varphi_A$', ORIGIN + 0.2 * polar(30))
    )

    d.add(coord_sys)
    d.add(phi_A_group)
    d.add(circle, point_A, label_A, origin, lbl_origin)

    sun_rays = Group(
        *tuple(
            Vector(A + 1.7 * polar(beta_A) + off, A + 1.2 * polar(beta_A) + off, color='blue')
            for off in map(lambda o: o * rotate(polar(beta_A), 90), [-0.2, -0.1, 0, 0.1, 0.2])
        ),
        Text('Sun', A + 2*polar(beta_A))
    )
    d.add(sun_rays)

    B = ORIGIN + polar(phi_B)
    point_B = Group(
        Point(B),
        Text('B', B + 0.1 * polar(phi_B))
    )

    light_beam = Group(
        Line(A + polar(beta_A), A, color='blue'),
        Line(A, B, color='blue')
    )

    phi_B_group = Group(
        Line(ORIGIN, B, linestyle='dashed'),
        AngleMarker(ORIGIN, 0.32, angles=(0, phi_B)),
        Text(r'$\varphi_B$', ORIGIN + 0.15 * polar(135))
    )

    theta_A_group = Group(
        Line(A, 1.7 * A, ls='dashed'),
        AngleMarker(A, 0.5, angles=(beta_A, phi_A)),
        Text(r'$\theta_A$', A + 0.25 * polar(45))
    )

    d.add(theta_A_group)

    thetap_A_group = Group(
        AngleMarker(A, 0.6, between=(B-A, -A)),
        Text(r'$\theta^\prime_A$', A + polar(238) * 0.45)
    )
    d.add(thetap_A_group)

#    theta_B_group = Group(
#        AngleMarker(B, 0.6, phi_B - 180, angle_between(A - B, RIGHT)),
#        Text(r'$\theta^\prime_A$', B + 0.48 * polar(32))
#    )
#    d.add(theta_B_group)

    theta_B = phi_B - 180 - angle_between(A - B, RIGHT)
    thetap_B_group = Group(
        AngleMarker(B, 0.65, phi_B - 180 + theta_B, phi_B - 180),
        Text(r'$\theta^\prime_A$', B + 0.48 * polar(5))
    )
    d.add(thetap_B_group)

    v = rotate(A, 90)
    line_OA_perp = Line(A - v, A + v, linestyle='dashed')
    d.add(line_OA_perp)
    d.add(point_B, light_beam, phi_B_group)

    #plt.show()


def test_angle_between():

    a = angle_between(RIGHT, UP)
    assert 90 == pytest.approx(a, 0.001)

    a = angle_between(UP, RIGHT)
    assert 270 == pytest.approx(a, 0.001)


def test_get_polar():

    vs = [UP+RIGHT, UP+LEFT, LEFT+DOWN, DOWN+RIGHT]
    expected = [45, 135, 225, 315]

    for v, e in zip(vs, expected):
        assert e == pytest.approx(get_polar(v), 0.001)

    for v, e in zip(vs, expected):
        v = rotate(v, 10)
        assert e+10 == pytest.approx(get_polar(v), 0.001)

