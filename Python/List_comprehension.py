"""

List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe:

    [ dados for dado in iteraável ]

# EXEMPLOS

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

>> 10, 20, 30, 40, 50

Nós podemos adicionar estruturas condicionais lógicas ás nossas List Comprehensions

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

print([numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros])
"""

# Exemplos

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

print([numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros])

