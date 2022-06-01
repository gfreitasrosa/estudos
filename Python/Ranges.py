"""
Ranges

- Precisamos conhecer o loop for para usar pos ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (Início padrão 0, e passo de 1 em 1)

    for num in range(11):
        print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (Início especificado pelo usuário , e passo de 1 em 1)

    for num in range(5,11):
        print(num)

# Forma 3

range(valor_de_incio, valor_de_parada, metodo)

OBS: valor_de_parada não inclusive (Inicio especificado pelo usuário, e passo específicado pelo usuário

    for num in range(1, 11, 2):
        print(num)

# Forma 4 (Inversa)

range(valor_de_final, valor_de_parada, metodo)

OBS: valor_de_parada não inclusive (Inicio especificado pelo usuário, e passo específicado pelo usuário

    for num in range(10, -1, -2)
        print(num)
"""

