import random
import matplotlib.pyplot as plt
import numpy as np


def draw_flower(a=5.0, b=2.0, n=2.0, k1=0.7, k2=0.3):
    tx = []
    ty = []
    k = 0
    if(int(b % 2.0) == 0):
        k = 1
    else:
        k = 2
    for ang in np.arange(0.0, 180.0 * k * b + 1.0, 1.0):
        s = ang * (np.pi / 180.0)
        r = ((1.0 - k1) + k1 * np.fabs(np.sin(a / b * s))) * \
            ((1.0 - k2) + k2 * np.fabs(np.sin(n * a / b * s)))
        tx.append(100.0 * r * np.cos(s))
        ty.append((100.0 * r * np.sin(s)) * -1.0)
    return tx, ty


x, y = draw_flower()
plt.plot(x, y)
plt.title('花びら関数')
plt.show()
