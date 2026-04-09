# Lambda

# Son como una función, van a ser unas funciones anonimas- no tienen nombre

suma_two_values = lambda first_value, second_value: first_value + second_value
print(suma_two_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))


