from sympy import symbols

def print_numeric_results(solutions):
    print("Solution count: ", len(solutions))
    
    x = symbols("x")

    for i, solution in enumerate(solutions): 
        print("Solution " + str(i + 1) + ": " + str(solution[x].evalf()))

def print_seperator():
    print("\n----------------------------------------------\n")