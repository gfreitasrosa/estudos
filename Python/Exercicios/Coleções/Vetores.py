"""
Geek University - seção 7 - parte 1

Ex 1:

    A = [1, 0, 5, -2, -5, 7]

    soma = A[0] + A[1] + A[5]

    print(soma)

    A[4] = 100

    for valor in A:
        print(valor)

Ex 3:

    vetor1 = [np.random.randint(10, size=(10))]

    print(vetor1)

    vetor2 =[]

    for valor in vetor1:
        vetor2.append(valor ** 2)

    print(vetor2)

Ex 4:

    vetor1 = np.random.randint(10, size=(8))

    print(vetor1)

    x = vetor1[4]

    y = vetor1[7]

    soma = x + y

    print(soma)

Ex 5:

    vetor1 = np.random.randint(10, size=10)

    print(vetor1)

    cont = 0

    for valor in vetor1:
        if valor % 2 == 0:
            cont += 1


    print(f"O vetor possuí {cont} valores pares")

Ex 6:

    vetor1 = np.random.randint(10, size=10)

    maior = 0

    menor = 0

    for valor in vetor1:
        if valor > maior:
            maior = valor
        elif valor <= menor:
            menor = valor

    print(maior)
    print(menor)

    print(vetor1)

Ex 30:

    vetor1 = np.random.randint(20, size=10)
    vetor2 = np.random.randint(20, size=10)

    vetor3 = []

    for valor_vet1 in vetor1:
        for valor_vet2 in vetor2:
            if valor_vet1 == valor_vet2 and valor_vet1 not in vetor3:
                vetor3.append(valor_vet1)

    print(vetor1)
    print(vetor2)
    print(vetor3)

Ex 31:

    vetor1 = np.random.randint(20, size=10)
    vetor2 = np.random.randint(20, size=10)

    vetor3 = []

    for valor1 in vetor1:
        for valor2 in vetor2:
            if valor1 in vetor2 and valor1 not in vetor3 and valor2 in vetor1 and valor2 not in vetor3:
                vetor3.append(valor2)

    print(vetor1)
    print(vetor2)

    print(vetor3)

"""


