def polynomial(x: int | float, coeffs: list[int | float]) -> float:
    ans = 0
    for i, coeff in enumerate(coeffs):
        ans += coeff * x**i
    return ans

def f_prime(x: int | float, coeffs):
    h = 1e-10 # use small h value for lim (h->0)
    return (polynomial(x + h, coeffs) - polynomial(x, coeffs)) / h
