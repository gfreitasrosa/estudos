"""
Set Comprehension






"""

# Exemplos

numeros = {num for num in range(1, 7)}

print(numeros)

numeros = {x: x ** 2 for x in range(10)}

print(numeros)
print(type(numeros))