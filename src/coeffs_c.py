import numpy as np
from scipy.integrate import quad


def f(t, n, p):
    c = np.cos(t)
    s = np.sin(t)

    c2 = np.sqrt(2) * c / (s * s + 1) + 1j * np.sqrt(2) * c * s / (s*s+1)
    c3 = np.exp(-2 * np.pi * n * t * 1j / p)

    return c2 * c3


def f1(t, n, p):
    return np.real(f(t, n, p))


def f2(t, n, p):
    return np.imag(f(t, n, p))


def main():
    p = 2 * np.pi
    l = []
    s = -60

    for n in range(s, -s):
        r = quad(f1, 0, p, args=(n, p))[0] * (1 / p)
        i = quad(f2, 0, p, args=(n, p))[0] * (1 / p)
        l.append(complex(round(r, 6), round(i, 6)))

    while l and np.isclose(np.abs(l[0]), 0) and np.isclose(np.abs(l[-1]), 0):
        l = l[1:-1]
        s += 1

    print(l)
    print(s)


if __name__ == '__main__':
    main()
