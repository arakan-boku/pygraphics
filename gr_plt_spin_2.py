import matplotlib.pyplot as plt
import numpy as np


def draw_spin(st_len=200.0, angle=89.0, step=1.0):
    tx = [0]
    ty = [0]
    ang = 0.0
    lpx = 0.0
    lpy = 0.0
    leng = st_len
    x = 0.0
    y = 0.0
    while(leng > 10.0):
        x = lpx + leng * np.cos(ang * np.pi / 180.0)
        y = lpy - leng * np.sin(ang * np.pi / 180.0)
        tx.append(x)
        ty.append(y)
        lpx = x
        lpy = y
        ang = ang + angle
        ang = ang - ang + ang % 360.0
        leng = leng - step
    return tx, ty


x, y = draw_spin(angle=44.5)
plt.plot(x, y)
plt.title('うずまき関数')
plt.show()
