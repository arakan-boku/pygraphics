import numpy as np


class Snow():

    def __init__(self):
        self.tx = []
        self.ty = []

    def move(self, leng, lpx, lpy, angle):
        x = lpx + leng * np.cos(angle * np.pi / 180.0)
        y = lpy - leng * np.sin(angle * np.pi / 180.0)
        self.tx.append(x)
        self.ty.append(y)
        return x, y

    def turn(self, angle, chg_angle):
        ang = angle + chg_angle
        ang2 = ang - ang + ang % 360.0
        return ang2

    def koch(self, leng, lpx, lpy, angle):
        leng_t = 0.0
        px = lpx
        py = lpy
        ang = angle
        if(leng <= 60.0):
            px, py = self.move(leng, px, py, ang)
        else:
            leng_t = leng / 3.0
            px, py = self.koch(leng_t, px, py, ang)
            ang = self.turn(ang, 60.0)
            px, py = self.koch(leng_t, px, py, ang)
            ang = self.turn(ang, -120.0)
            px, py = self.koch(leng_t, px, py, ang)
            ang = self.turn(ang, 60.0)
            px, py = self.koch(leng_t, px, py, ang)
        return px, py

    def draw(self, r0=1000.0):
        x0 = 0.0
        y0 = 0.0
        sx = x0 - r0 * np.sqrt(3.0) / 2
        sy = y0 - r0 / 2
        self.tx.append(sx)
        self.ty.append(sy)
        leng = r0 * np.sqrt(3.0)
        angle = 0.0
        for i in range(3):
            sx, sy = self.koch(leng, sx, sy, angle)
            angle = self.turn(angle, -120.0)
        return self.tx, self.ty
