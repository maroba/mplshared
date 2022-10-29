import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle

fig = plt.figure()
ax = plt.axes()
ax.plot()
ax.set_axis_off()
ax.set_aspect('equal')

ps = 0.02
phi_C_deg = 60
phi_D_deg = 130

phi_C = phi_C_deg / 180 * np.pi
phi_D = phi_D_deg / 180 * np.pi

A, B, C, D, orig = [
    np.array((-1, 0)),
    np.array((1, 0)),
    np.array((np.cos(phi_C), np.sin(phi_C))),
    np.array((np.cos(phi_D), np.sin(phi_D))),
    np.array((0, 0))
]

right, left = np.array((1, 0)), np.array((-1, 0))
down, up = np.array((0, -1)), np.array((0, 1))

ax.add_patch(Circle(orig, 1, fill=False))
ax.add_patch(Polygon([A, B, C], fill=False))

for point in A, B, C, orig:
    ax.add_patch(Circle(point, radius=ps, facecolor='k'))

BC = B - C
rot_angle = -90 + 180 / np.pi * np.arctan(BC[1] / BC[0])

ax.add_patch(Rectangle(C, 0.15, 0.15, fill=False, angle=rot_angle))

ax.annotate('A', A, xytext=A+0.1*left)
ax.annotate('B', B, xytext=B+0.05*right)
ax.annotate('C', C, xytext=C+0.05*right+0.02*up)
ax.annotate('O', orig, xytext=orig+0.1*down)

plt.show()

