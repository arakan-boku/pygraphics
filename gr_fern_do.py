import matplotlib.pyplot as plt
import gr_fern as fn

f = fn.Fern()
x, y = f.draw()
plt.plot(x, y, '.')
plt.title('Bernstein Fern')
plt.show()
