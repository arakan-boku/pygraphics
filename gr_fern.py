import random


class Fern():

    def __init__(self):
        self.tx = [0]
        self.ty = [0]

    def tran_1(self, p):
        x = p[0]
        y = p[1]
        x1 = 0.85 * x + 0.04 * y
        y1 = -0.04 * x + 0.85 * y + 1.6
        return x1, y1

    def tran_2(self, p):
        x = p[0]
        y = p[1]
        x1 = 0.2 * x - 0.26 * y
        y1 = 0.23 * x + 0.22 * y + 1.6
        return x1, y1

    def tran_3(self, p):
        x = p[0]
        y = p[1]
        x1 = -0.15 * x + 0.28 * y
        y1 = 0.26 * x + 0.24 * y + 0.44
        return x1, y1

    def tran_4(self, p):
        x = p[0]
        y = p[1]
        x1 = 0
        y1 = 0.16 * y
        return x1, y1

    def get_index(self):
        prob = [0.85, 0.07, 0.07, 0.01]
        r = random.random()
        c = 0
        sump = []
        for p in prob:
            c += p
            sump.append(c)
        for item, sp in enumerate(sump):
            if(r <= sp):
                return item
        return len(prob) - 1

    def tran(self, p):
        trans = [self.tran_1, self.tran_2, self.tran_3, self.tran_4]
        tindex = self.get_index()
        t = trans[tindex]
        x, y = t(p)
        return x, y

    def draw(self, n=10000):
        x1 = 0
        y1 = 0
        for i in range(n):
            x1, y1 = self.tran((x1, y1))
            self.tx.append(x1)
            self.ty.append(y1)
        return self.tx, self.ty
