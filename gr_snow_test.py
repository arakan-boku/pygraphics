import matplotlib.pyplot as plt
import numpy as np


tx = []
ty = []


def move(leng, lpx, lpy, angle):
    x = lpx + leng * np.cos(angle * np.pi / 180.0)
    y = lpy - leng * np.sin(angle * np.pi / 180.0)
    tx.append(x)
    ty.append(y)
    return x, y


def turn(angle, chg_angle):
    ang = angle + chg_angle
    ang2 = ang - ang + ang % 360.0
    return ang2


def koch(leng, lpx, lpy, angle):
    leng_t = 0.0
    px = lpx
    py = lpy
    ang = angle
    if(leng <= 60.0):
        px, py = move(leng, px, py, ang)
    else:
        leng_t = leng / 3.0
        px, py = koch(leng_t, px, py, ang)
        ang = turn(ang, 60.0)
        px, py = koch(leng_t, px, py, ang)
        ang = turn(ang, -120.0)
        px, py = koch(leng_t, px, py, ang)
        ang = turn(ang, 60.0)
        px, py = koch(leng_t, px, py, ang)
    return px, py


def snow(r0=1000.0):
    x0 = 0.0
    y0 = 0.0
    sx = x0 - r0 * np.sqrt(3.0) / 2
    sy = y0 - r0 / 2
    tx.append(sx)
    ty.append(sy)
    leng = r0 * np.sqrt(3.0)
    angle = 0.0
    for i in range(3):
        sx, sy = koch(leng, sx, sy, angle)
        angle = turn(angle, -120.0)


snow()

plt.plot(tx, ty)
plt.title('コッホ関数')
plt.show()
