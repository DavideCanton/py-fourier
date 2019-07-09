import numpy as np
from scipy.integrate import quad


def f(t, n, p):
    c2 = 2 * (1 - np.cos(t)) * np.exp(1j * t)
    c3 = np.exp(-2 * np.pi * n * t * 1j / p)

    return c2 * c3


def f1(t, n, p):
    return np.real(f(t, n, p))


def f2(t, n, p):
    return np.imag(f(t, n, p))


P = 2 * np.pi

for n in range(0, 100):
    r = quad(f1, 0, P, args=(n, P))[0] * (1 / P)
    i = quad(f2, 0, P, args=(n, P))[0] * (1 / P)
    if np.allclose([r, i], [0, 0]):
        break
    print(n, "->", complex(round(r, 2), round(i, 2)))
