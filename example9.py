import sympy as sp

x, y = sp.symbols('x y')

f = sp.Lambda((x, y), 1 + x**2 + y**2)

first_derivation = sp.diff(f(x, y), x)
second_derivation_for_x = sp.diff(f(x, y), x, 2)
second_derivation_for_y = sp.diff(f(x, y), x, y)

print(first_derivation)
print(second_derivation_for_x)
print(second_derivation_for_y)