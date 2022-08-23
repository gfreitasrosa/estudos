"""
POO - Objetos

Objetos -> instâncias da classe, ou seja, após o mapeamento do objeto no mundo real para sua representação
computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos / instâncias de uma
classe como variáveis do tipo definido na classe.






"""


class Lampada:
    def __init__(self, voltagem):
        self.__voltagem = voltagem
        self.__ligada = False

    def ligarLampada(self):
        if self.__ligada:
            print('A lampada já está ligada!')
        else:
            self.__ligada = True

    @property
    def getVoltagem(self):
        return self.__voltagem

    def checarLampada(self):
        if self.__ligada:
            print("A lampada está ligada")
        else:
            print("A lampada está desligada")


if __name__ == '__main__':

    l1 = Lampada(127)

    l1.checarLampada()

    l1.ligarLampada()

    l1.checarLampada()

