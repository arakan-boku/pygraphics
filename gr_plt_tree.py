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


def draw_tree(leng=120.0, lpx=320.0, lpy=380.0, angle=90.0, scale=0.7):
    if(leng >= 4.0):
        tx.append(lpx)
        ty.append(lpy)
        lpx, lpy = move(leng, lpx, lpy, angle)
        draw_tree(leng * scale, lpx, lpy, angle + 20.0)
        draw_tree(leng * scale, lpx, lpy, angle - 20.0)
    return tx, ty


def init(lpx=320.0, lpy=380.0):
    tx.append(lpx)
    ty.append(lpy)


init()
x, y = draw_tree()
plt.plot(x, y)
plt.title('樹木曲線')
plt.show()
