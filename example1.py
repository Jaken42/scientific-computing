import numpy as np

from utils import print_seperator

print("Numeric Computing")

print_seperator()

result = 2 + 3

print("The result of 2 + 3 is:", result)

print_seperator()

x = np.sqrt(2)
y = 2.01

if (x**2 == y):
    print("the square root of 2 is equal to 2")

else:
    print("the square root of 2 is not equal to 2")

print_seperator()

# Fehlertoleranz!
print("Is squaring the square root of 2 equal to 2 with a tolerance of 1e-6?")
print(np.isclose(x**2, y, atol = 1e-6))