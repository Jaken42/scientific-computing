import sympy as sp

from utils import print_seperator

x = sp.symbols('x')

f = sp.Lambda(x, sp.exp(-x))

integral = sp.integrate(f(x), (x, 0, sp.oo))

print(integral)

print_seperator()

y = sp.symbols('y')

f = sp.Lambda((x,y), sp.exp(-x**2 - y**2))

# Integration:
solution = sp.integrate(f(x, y), (x, 0, 1), (y, 0, 1))
print(solution)

# Numerisch:
print(solution.evalf())
