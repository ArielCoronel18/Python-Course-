# calcular el factorial de un número dado

import re


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

# calcular el factorial de un número dado

total = 0

for elemento in [1, 2, 3, 4, 5]:
    total += elemento
    print(total)
    