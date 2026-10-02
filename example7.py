import sympy as sp

x, y = sp.symbols('x y')

solutions = sp.solve([sp.Eq(x**2, 2), sp.Eq(y, 0)], [x, y], dict=True)
print(solutions)



# Beispiel
"""
solutions = sp.solve([sp.Eq(x**2, y), sp.Eq(y, 2 * x)], [x, y], dict=True)
print(solutions)
"""