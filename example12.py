import sympy as sp

x = sp.symbols('x')

f = sp.Lambda(x, 1 / (1 + x**2))

limit = sp.limit(f(x), x, sp.oo)

print(limit)