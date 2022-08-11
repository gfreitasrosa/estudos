"""
Filter

filter() -> serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos

import statistics


# Dados coletados de algum sensor
valores = 1, 2, 3, 4, 5, 6

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(valores)

# OBS: Asssim como a função map(), a filter(), recebe dois parâmetros, sendo uma função e um iterável.

res = filter(lambda x: x > media, valores)

print(media)

print(list(res))

# OBS: O valor só fica na mémoria até SER UTILIZADO UMA VEZ, assim como o map().

# Retorna um objetivo do tipo filter.object um iterável, assim como em map() que retorna um map.object

# Exemplos:

paises = ['', 'Brasil', 'Argentina', '']


paises_remove = filter(None, paises)
# None, filtra todo dado vazio

print(list(paises_remove))

# A diferença entre map() e filter() é:

# map() - > Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função.

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolo, eu adoro pizza']},
    {'username': 'gabriel', 'tweets': ['Eu adoro cachorro']},
    {'username': 'sandra', 'tweets': []}
]

# filtrar os usuários que estão inativos no twitter

filtro_inativos = list(filter(lambda user: user.get('tweets') == [], usuarios))

print(filtro_inativos)

# Como combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'sua instrutura é' + nome, desde que cada nome tenha menos de 5 caracteres.

lista_instrutoras = list(map(lambda nome: f'sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista_instrutoras)

"""




