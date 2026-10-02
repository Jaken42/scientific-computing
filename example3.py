import sympy as sp

x = sp.symbols('x')

p = (x**2 - 1) / (x - 1)

# Es gilt: (x**2 - 1) => (x + 1)(x - 1)
# Deshalb: (x + 1)(x - 1) / (x - 1) = (x + 1)

s = sp.simplify(p)

print(s)

# Das Übungsbeispiel ist unten, scrollen!










# Vereinfache (1 / x - y) - (1 / (y - x))

x, y = sp.symbols('x y')

expression = (1 / (x - y)) - (1 / (y - x))

simplified_expression = sp.simplify(expression)

# Uncomment this!
#print(simplified_expression)