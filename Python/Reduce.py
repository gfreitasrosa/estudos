"""
Entendendo o Reduce

OBS: A partir do Python3+ a fuinção reduce() não é mais uma função integrada (built-in). Agora temos que importar
e utilizar esta função a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela.
Em todo caso, 99% das vezes um loop for é mais legível

Para entender o reduce()

# Imagine que você tem uma coleção de dados:

dados = [a1, a1, a3, ..., an]

# E você tem uma função que recebe dois parâmetros:

def funcao(x ,y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável.

reduce(funcao,dados)

A função reduce(), funciona da seuinte forma:
    Passo1: res1 = f(a1,a2) # Aplica a funçao nos dois primeiros elementos da coleção e gaurda o resultado
    Passo 2: res2 = f(res1,a3) # Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda o res.

    Isso é repitido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resm, an)


Ou seja, emc ada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente, poderíamos ver a função reduce() como:

funcao(funcao(funcao(a1,a2),a3),a4), ...), an)

"""