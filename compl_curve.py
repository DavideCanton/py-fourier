import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 100)
v = 2 * np.exp(1j * t) - np.exp(2j * t) + 1

x = np.real(v)
y = np.imag(v)
plt.plot(x, y)

plt.legend()
plt.grid()
plt.show()
