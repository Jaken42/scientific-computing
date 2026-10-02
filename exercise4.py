import sympy as sp

x = sp.symbols('x')
f = sp.Lambda(x, sp.cos(x) * sp.exp(x**2))

first_derivation = sp.diff(f(x), x)
second_derivation = sp.diff(f(x), x, x)

print(first_derivation)
print(second_derivation)


integral = sp.integrate(sp.exp(-x**2), x)
print(integral)