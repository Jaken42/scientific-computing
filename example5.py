import sympy as sp

x = sp.symbols('x')

solutions = sp.solve(sp.Eq(x**2 - 2, 0), x, dict=True)

print("Length of the solutions collection: ", len(solutions))

first_solution = solutions[0]

print("First solution: ", first_solution)
print("X from first solution: ", first_solution[x])
print("Numeric evaluation of x from first solution:", first_solution[x].evalf())
# Das Übungsbeispiel ist unten, scrollen!

















# Löse die Gleichung x**3 + 2 * x**2 + 3 * x + 1 = 0

solutions = sp.solve(sp.Eq(x**3 + 2 * x**2 + 3 * x + 1, 0), x, dict=True)

# The following printing is hereafter encapsulated in 
# print_numeric_results(solutions)

print("Length of the solutions collection: ", len(solutions))

for i, solution in enumerate(solutions): 
    print("Solution " + str(i) + ": " + str(solution[x].evalf()))