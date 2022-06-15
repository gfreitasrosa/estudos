"""
EXERCÍCIOS DA SEÇÃO 07 - PARTE 2 DO CURSO DE PYTHON DO BÁSICO AO AVANÇADO UDEMY

Ex 1: Percorendo matriz e identificando valores:

    matriz1 = [[1, 1, 1, 1],
               [1, 1, 45, 1],
               [1, 23, 1, 1],
               [1, 100, 1, 1]]

    print(matriz1)

    soma = 0

    for i in matriz1:
        for elemento in i:
            if elemento > 10:
                soma += 1


    print(soma)

Ex 2: Declarando matriz vazia e preenchendo

    import numpy as np

    # Algoritimo para gerar matriz identidade sem utilizar numpy

    mat = np.zeros((5,5)) # Cria matriz com todos o valores 0

    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j:
                mat[i][j] = 1
            else:
                mat[i][j] = 0

    print(mat)

    # Algoritimo para gerar matriz identidade utilizando numpy

    mat2 = np.identity(5)

    print(mat2)

Ex 3: Preenchendo matriz com o produto da linha e coluna

    mat = np.zeros((4,4))

    for i in range(len(mat)+1):
        for j in range(len(mat)+1):
            mat[i-1][j-1] = i * j

    print(mat)

Ex 4: Buscando valor na matriz

    mat = np.random.randint(20, size=(4, 4))

    print(mat)

    maior = 0
    posicao_i = 0
    posicao_j = 0

    for i in range(len(mat)):
        for j in range(len(mat)):
            if maior < mat[i][j]:
                maior = mat[i][j]
                posicao_i = i
                posicao_j = j

    print(f"O maior valor: {maior}, está localizado na posição [{posicao_i+1},{posicao_j+1}] da matriz")



Ex 5: Bucando valor na matriz

    mat = np.random.randint(20, size=(5, 5))

    x = 15

    cont = 0

    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == x:
                print(f"O valor se encontra na posição [{i+1},{j+1}] da matriz")
            else:
                cont += 1

    if cont == 25:
        print("Valor nao encontrado na matriz")

    print(mat)
"""



