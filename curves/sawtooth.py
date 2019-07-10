import numpy as np

def get_coeffs(n):
    c0 = 0
    coeffs_pos = [1j * ((-1) ** n) / (2 * n * np.pi) for n in range(1, n)]
    coeffs_neg = [x.conjugate() for x in coeffs_pos[::-1]]
    coeffs_pos = coeffs_neg + [c0] + coeffs_pos
    return coeffs_pos, -n + 1