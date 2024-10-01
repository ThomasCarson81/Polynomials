def polynomial(x: int | float, coeffs: list[int | float]) -> float:
    ans = 0
    for i, coeff in enumerate(coeffs):
        ans += coeff * x**i
    return ans

def f_prime(x: int | float, coeffs):
    h = 1e-10 # use small h value for lim (h->0)
    return (polynomial(x + h, coeffs) - polynomial(x, coeffs)) / h
def newtons_method(x, coeffs, depth):
    if depth == 0:
        return 1
    prevx = newtons_method(x, coeffs, depth - 1)
    return prevx - polynomial(prevx, coeffs) / f_prime(prevx, coeffs)

equation = input("Enter the coefficients in the order a + bx + cx^2 + dx^3 + ...:\n")
equation = equation.split()
coeffs = [float(i) for i in equation]
print(newtons_method(1, coeffs, 50))
