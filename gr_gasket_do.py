import matplotlib.pyplot as plt
import gr_gasket as gt

f = gt.Gasket()
x, y = f.draw()
plt.plot(x, y, '.')
plt.title('Sherpinski\'s Gasket')
plt.show()
