"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentyos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de instância e métodos de Classe

### Métodos de Instância: ###

# O método dunder init __init__ é um método especial chamado de construtor

# OBS: todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder

# OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos

# ATENÇÃO! Por mais que possamos criar nossas própias funções dunder, não é aconselhado, por o Python
# possuir diversar funções próprias, de preferência NUNCA O FAÇA.

class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = True

    def mudar_cor(self, cor):
        self.__cor = cor

    def desligar_lampada(self):
        if self.__ligada:
            self.__ligada = False
        else:
            print("A lampada ja está dedsligada")

    def getCor(self):
        return self.__cor

    def getLigada(self):
        return self.__ligada


if __name__ == '__main__':

    l1 = Lampada(127, "azul")

    l1.mudar_cor("vermelha")

    print(l1)

    print(l1.getLigada())

    l1.desligar_lampada()

    print(l1.getLigada())

### Métodos de classe ###


class Lampada:

    contador = 0

    @classmethod
    def conta_usuarios(cls):  # Método de classe, utilizado quando precisamos fazer acesso a atributos de classe
        print(f"Temos {cls.contador} lampadas acesas ")

    def __init__(self, voltagem, cor):
        self.__num_lampada = Lampada.contador + 1
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = True
        Lampada.contador = self.__num_lampada

if __name__ == '__main__':

    l1 = Lampada(127, 'vermelha')
    l2 = Lampada(220, 'azul')

    Lampada.conta_usuarios()  # Forma correta, pois é um método de classe não de instância
    l1.conta_usuarios()  # Forma incorreta

# Métodos de classe em python são conhecidos como métodos estáticos em outras linguagens

### Métodos privados ###


class Lampada:

    def __init__(self, voltagem):
        self.__voltagem = voltagem
        print(f'lampada tem {self.__retorna_voltagem()} volts')  # Forma correta


    def __retorna_voltagem(self):
        return self.__voltagem


if __name__ == '__main__':

    l1 = Lampada(127)

    print(l1._Lampada__retorna_voltagem())  # Forma incorreta

### Métodos estáticos ###


class Lampada:

    def __init__(self, voltagem):
        self.__voltagem = voltagem

    @staticmethod
    def definicao():  # NÃO TEM ACESSO A CLASSE NEM A INSTÂNCIA
        return "12345"

    def __retorna_voltagem(self):  # Método privado
        return self.__voltagem




if __name__ == '__main__':

    l1 = Lampada(127)

    print(Lampada.definicao())

    print(l1.definicao())

"""
