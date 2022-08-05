def triangulo(n):
    altura = 2*n-1
    largura = n
    cont = 0
    while cont < altura:
        while cont < largura:
            cont = cont + 1
            print("*" * cont)
        while cont > 0:
            cont = cont - 1
            print("*" * cont)
        return

triangulo(35)