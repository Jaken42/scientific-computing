import sympy as sp

# Vereinfache (5 / (b - 1)) - (6 * b / (b**2 - 1)) - ((1 - 2 * b) / (b + b**2))

b = sp.symbols('b')

expression = (5 / (b - 1)) - (6 * b / (b**2 - 1)) - ((1 - 2 * b) / (b + b**2))

simplified_expression = sp.simplify(expression)

print(simplified_expression)