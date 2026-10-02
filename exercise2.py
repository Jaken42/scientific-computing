import sympy as sp

from utils import print_numeric_results, print_seperator

x = sp.symbols('x')

solutions = sp.solve(sp.Eq(sp.exp(x**2), 2), x, dict=True)

print_numeric_results(solutions)

print_seperator()

solutions = sp.solve(sp.Eq(x * sp.exp(x**2), 2), x, dict=True)

print_numeric_results(solutions)