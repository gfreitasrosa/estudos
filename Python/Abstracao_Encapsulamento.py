"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular -> cápsula


                Classe
--------------------------------------
\                                     \
\         atributos e métodos         \
\                                     \
\_____________________________________\


# Relembrando Atributos/Métodos em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo
privado chamado __nome e um método privado chamado __falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas Python não bloqueia este acesso
fora da classe. Com Python acontece um fenômeno chamado Name Mangling. que faz uma alteração na forma de se
acessar os elementos privados, conforme:

_Classe__elemento

exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome

instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.


Exemplo utilizando atributos privados:

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

if __name__ == '__main__':

    conta1 = Conta('gabriel', 1200, 1000)

    print(conta1.__dict__)

    conta1.depositar(1000)

    conta1.extrato()

    conta1.sacar(1000)

    print(conta1.__dict__)


"""

