import matplotlib.pyplot as plt
import gr_snow as snow

sp1 = snow.Snow()
tx1, ty1 = sp1.draw()
plt.plot(tx1, ty1)

sp2 = snow.Snow()
tx2, ty2 = sp2.draw(r0=700.0)
plt.plot(tx2, ty2)

sp3 = snow.Snow()
tx3, ty3 = sp3.draw(r0=400.0)
plt.plot(tx3, ty3)

plt.title('Draw a snowflake with the Koch curve')
plt.show()
