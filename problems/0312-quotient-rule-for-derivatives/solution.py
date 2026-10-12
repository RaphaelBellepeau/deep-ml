import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    def derivative(f):
        results = []
        for i in range(len(f) - 1):
            results.append(f[i]*(len(f)-i -1))
        return results
    gd_coeffs = derivative(g_coeffs)
    hd_coeffs = derivative(h_coeffs)
    def to_poly(f,y):
        results = 0
        for i,c in enumerate(f):
            results += c*(x**(len(f)- i -1 ))
        return results
    g_poly = to_poly(g_coeffs,x)
    h_poly = to_poly(h_coeffs,x)
    gd_poly = to_poly(gd_coeffs,x)
    hd_poly = to_poly(hd_coeffs,x)

    return (gd_poly*h_poly - hd_poly*g_poly)/h_poly**2