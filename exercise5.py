import sympy as sp

from utils import print_seperator

x = sp.symbols('x')

f = sp.Lambda(x, sp.exp(-x**2))

integral = sp.integrate(f(x), (x, 0, 1))

print(integral)

print(integral.evalf())

print_seperator()

integral = sp.integrate(f(x), (x, -sp.oo, sp.oo))

print(integral)

print(integral.evalf())