import sympy as sp

x = sp.sqrt(2)
y = 2

print (x**2 == y)


x = symbols('x')
p = x**2 - 1
print(p)

print(p.subs(x, 1))
print(p.subs(x, sqrt(2)))