import sympy as sp

x, y = sp.symbols('x y', integer=True)

hint = (6, 7, 8)

for z in range(10):
    equations = [
        sp.Eq(x + y + z, 15),
        sp.Eq(x**2 + y**2 + z**2, 77)
    ]

    solutions = sp.solve(equations, [x, y], dict=True)

    for solution in solutions:
        X, Y = solution[x], solution[y]
        
        if not (X.is_integer and Y.is_integer):
            continue
        
        X, Y = int(X), int(Y)

        values = (X, Y, z)

        if len(values) == 3 \
            and all (0 <= value <= 9 for value in values) \
            and (X < Y < z or X > Y > z) \
            and any(z == h for z, h in zip(values, hint)):
                print(values)