import sympy as sp

v1, v2, v3, i1, i2, i3, r = sp.symbols('v1 v2 v3 i1 i2 i3 r')

equations = [
    sp.Eq(v1 - 6 * r * i1 + 4 * r * (i2 - i1), 0),
    sp.Eq(v2 + 2 * r * (i3 - i2) - 3 * r * i2 - 4 * r * (i2 - i1), 0),
    sp.Eq(-v3 - r * i3 - 2 * r * (i3 - i2), 0)
]

solutions = sp.solve(equations, [i1, i2, i3], dict=True)

print(solutions)