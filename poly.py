def polynomial(x: int | float, coeffs: list[int | float]) -> float:
    ans = 0
    for i, coeff in enumerate(coeffs):
        ans += coeff * x**i
    return ans