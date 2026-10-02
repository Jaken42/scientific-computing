import sympy as sp

x = sp.symbols('x')
f = sp.Lambda(x, x**2) # Symbolische Funktion für x^2

print(f(1))
print(f(2))
print(f(3))
print(f(4))

first_derivation = sp.diff(f(x), x)
second_derivation = sp.diff(f(x), x, x)

print(first_derivation)
print(second_derivation)

"""
f = sp.Lambda(x, sp.exp(x**2))

first_derivation = sp.diff(f(x), x)
second_derivation = sp.diff(f(x), x, x)

print(first_derivation)
print(second_derivation)
"""