import numpy as np
import matplotlib.pyplot as plt

from curves.infinite import get_coeffs

coeffs, start_index = get_coeffs()
p = 2 * np.pi

x = np.linspace(0, 2 * np.pi, 100)

v = np.zeros_like(x, dtype=complex)
for (n, c) in enumerate(coeffs, start=start_index):
    v += c * np.exp(2 * np.pi * 1j * x * n / p)

plt.plot(np.real(v), np.imag(v))
plt.show()
