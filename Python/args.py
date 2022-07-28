"""
Entendendo o *args

- O *args é um parâmetro como outro qualquer: Isso significa que você poderá chamar de qualquer coisa,
desde qe começe com asterisco

Exemplo:

*xis

Mas por convenção, utilizamos o *args para definí-lo

Mas o que é o *args?

O parâmetro *args utilziado em uma função, coloca os valores extras informados como entrada em uma tupla.
Então desde jpa lembre-se que tuplas são imutáveis

# Exemplos:


def soma_todos_numeros(num1=2, num2=4, num3=1):
    return num1 + num2 + num3


# Entendendo o *args


def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
>> 0

print(soma_todos_numeros(1))
>> 1

print(soma_todos_numeros(2,3))
>> 5

print(soma_todos_numeros(3,4,5))
>> 12

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza quem você é'


print(verifica_info())

print(verifica_info("Geek", "University"))

print(verifica_info(1, 2, 3, 4, "University"))

# Obs: Não consegue fazer uma operação recebendo uma lista como parâmetro da função sem o desempacotador

nomes = ['gabriel', 'Geek', 'University', 'felipe']

print(verifica_info(*nomes))

# Obs: O asterisco serve para que informemos ao Python que estamos
Passando como argumento uma coleção de dados. Desta forma, ele saberá que precisará antes desempacotar os dados

"""


