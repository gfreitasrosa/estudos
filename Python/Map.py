"""
Map

Não confundir com Dict ( Dicionário )

Com map, fazemos mapeamento de valores para função.

import math

def area(r):
    ''' Calcula a área de um círculo com raio r '''
    return math.pi * (r ** 2)

raios = [2, 5, 7.1, 0.3, 10, 44]

areas = map(area, raios)

# Map é uma função que recebe dois parâmetros; O primeiro a função, o segundo um iterável

print(areas)
>> <map object at 0x000002BAF6371FA0>
print(type(areas))
>> <class 'map'>
print(list(areas)) # Convertendo para lista
[12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]

# Forma mais usada, com a utilização de lambda:

    print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.

"""

cidades = [("Berlim", 29), ('Cairo', 366), ('Buenos Aires', 19), ('Los Angeles', 26)]

print(list(map(lambda dado: f"A temperatura de {dado[0]} em Fahrenheit é {dado[1] * 1.8 + 32}", cidades)))