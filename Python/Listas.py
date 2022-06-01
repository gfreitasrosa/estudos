"""

LISTAS

Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valroes.

Já em Python:

- Dinâmico: Não possuí tamanho fixo: Ou seja, podemos criar a lista e simplismente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo: Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []
"""

carrinho = []
produto = ''

while produto != "sair":
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)