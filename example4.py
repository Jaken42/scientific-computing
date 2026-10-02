import sympy as sp

x = sp.symbols('x')
p = x**2 - 1
print("Expression: ", p)

print("Substituting x with 1: ", p.subs(x, 1))
print("Substituting x with the square root of 2: ", p.subs(x, sp.sqrt(2)))