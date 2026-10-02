import sympy as sp

x = sp.symbols('x')

f = sp.Lambda(x, x**2)

unbestimmtes_integral = sp.integrate(f(x), x)

print(unbestimmtes_integral)

bestimmtes_integral = sp.integrate(f(x), (x, 0, 1))

print(bestimmtes_integral)

unendliches_integral = sp.integrate(f(x), (x, 0, sp.oo))

print(unendliches_integral)