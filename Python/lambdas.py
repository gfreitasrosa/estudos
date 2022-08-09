"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplismente Lambdas, são funcções sem nome, ou seja, Funções Anônimas.

# Função Python

def soma(a, b):
    return a + b

# Função em Python

def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Expressão Lambda


lambda x: 3 * x + 1

# Como utilizar a espressão lambda?

calc = lambda x: 3 * x + 1 # Não é a forma ideal

print(calc(4))

# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
                        # entrada         # retorno

print(nome_completo('  gabriel', ' rosa'))

# Em Lambda podemos ter nenhum ou n parâmetros de entrada

# Normalmente usada para fazer filtragens e ordenação de dados
"""

