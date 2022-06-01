"""
Tuplas (tuple)

Tuplas são abstante parecidas com listas

Existem basicamente duas diferemças básicas:

1 - As tuplas são representadas por parêncteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla

CUIDADO 1 - As tuplas são representadas por (), mas podem ser escritas sem parenteses.

CUIDADO 2 - Tuplas com 1 elemento

tupla = (4) - Isso não é uma tupla

tupla = (4,) - Isso é uma tupla

Tuplas são definidas pela vírgula e não pelo uso do parênteses

Podemos gerar uma tupla dinamicamente com range(incio, fim, passo)

    tupla = tuple(range(1, 11, 3))

# DESEMPACOTAMENTO

tupla = ("Geek university", "Escola")

curso, escola = tupla

print(curso)
print(escola)

# OBS: Gera erro se colocar um número diferente de elementos para desempacotar

# OBS: Métodos para adição e remoção de elementos nas tuplas não existem, por elas semrem imutáveis

# Possui método para : soma (int ou real), valor máximo(int ou real, valor mínimo(int ou real) e tamanho

# Concatenação de Tuplas

    tupla1 = (1,2,3)
    tupla2 = (4,5,6)

    print(tupla1 + tupla2)

# OBS: PODEMOS SOBRESCREVER OS VALORES DE UMA TUPLA (NÃO É UMA CONSTANTE)

# verificar se determinado elemento está contido na tupla

    tupla = (1,2,3)

    print(2 in tupla)
    >> True

# Iterar uma tupla

    tupla = (1,2,3)

    for indice, valor in enumerate(tupla):
        print(indice,valor)

# Dicas na utilização de tuplas:

    devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
    Exemplo: meses do ano

# O acesso de elementos de uma tupla é semelhante a de uma lista

    tupla = (1,2,3)

    print(tupla[1])

# Iterar com while

    i = 0

    while i < len(tupla):
    print(tupla[1])
    i = i + 1

# Slicing

    print(tupla[inicio:fim:passo])

# Por quê utilizar tuplas?

    # - TUPLAS DEIXAM SEU CÓDIGO MAIS SEGURO (IMUTABILIDADE)
    # - TUPLAS SÃO MAIS RÁPIDAS DO QUE LISTAS
"""




