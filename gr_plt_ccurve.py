import matplotlib.pyplot as plt
import numpy as np

tx = [1.0]
ty = [2.0]


def move(lpx, lpy, dx, dy):
    tx.append(lpx + dx)
    ty.append(lpy + dy)


def draw_c(st_len=10.0, lpx=0.0, lpy=0.0, dx=2.0, dy=0.0):
    leng = st_len
    if(leng <= 0.0):
        move(lpx, lpy, dx, dy)
    else:
        draw_c(leng - 1.0, tx[-1], ty[-1], (dx + dy) / 2, (dy - dx) / 2)
        draw_c(leng - 1.0, tx[-1], ty[-1], (dx - dy) / 2, (dy + dx) / 2)
    return tx, ty


x, y = draw_c()
plt.plot(x, y)
plt.title('C曲線')
plt.show()
