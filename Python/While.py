"""

Loop while

Forma geral

while expressao_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 1

num > 5 -> False
num < 2 -> True


# OBS: Em um loop while, a variavel precisa ser inicializada antes
# OBS: Em um loop while, é importante que cuidemos do critério de parada.

# do while (C OU Java

    do {
        //execução
    }while(expressão):

"""

numero = 1

while numero <= 10:
    print(numero, end='')
    numero = numero + 1

