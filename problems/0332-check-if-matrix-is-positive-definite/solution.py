import numpy as np

def check_positive_definite(matrix: list) -> dict:
    flat = [x for row in matrix for x in row]
    n = int(len(flat) ** 0.5)
    if n * n != len(flat):
        raise ValueError("Input cannot be reshaped into a square matrix")
    A = np.array(flat, dtype=float).reshape(n, n)

    if n == 2:
        trace = A[0,0] + A[1,1]
        det = A[0,0]*A[1,1] - A[0,1]*A[1,0]
        disc = trace**2 - 4*det
        sq = disc**0.5
        eigen = [round((trace - sq)/2, 4), round((trace + sq)/2, 4)]

    elif n == 3:
        a, b, c = A[0]
        d, e, f = A[1]
        g, h, i = A[2]
        c2 = a + e + i
        c1 = (a*e - b*d) + (a*i - c*g) + (e*i - f*h)
        c0 = np.linalg.det(A)
        p = c1 - c2**2/3
        q = -2*c2**3/27 + c2*c1/3 - c0
        if abs(p) < 1e-12:
            roots = [c2/3]*3
        else:
            r = 2*(-p/3)**0.5
            arg = max(-1.0, min(1.0, 3*q/(p*r)))
            phi = np.arccos(arg)/3
            roots = [r*np.cos(phi - 2*np.pi*k/3) + c2/3 for k in range(3)]
        eigen = sorted(round(x, 4) for x in roots)

    else:
        raise ValueError("Only 2x2 and 3x3 matrices are supported")

    return {'is_positive_definite': all(x > 0 for x in eigen), 'eigenvalues': eigen}