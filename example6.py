import sympy as sp

x, y = sp.symbols('x y')

solutions = sp.solve([sp.Eq(x**2, 2), sp.Eq(y, 0)], [x, y], dict=True)
print(solutions)

























# Beispiele:
"""
solutions = sp.solve(sp.Eq(sp.E**(2 * x), y), x, dict=True)
print(solutions)

equations = [
    sp.Eq(x**3 + x**2 + x + 1, 0),
    sp.Eq(x**3 + x**2 + x - 1, 0),
    sp.Eq(sp.sqrt(6 * x - 2) + 5 - 3 * x, 0)
]

for i, equation in enumerate(equations):
    solutions = sp.solve(equation, x, dict=True)
    print("Solutions for equation " + str(i + 1) + ": " + str(solutions))
"""