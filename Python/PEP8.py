"""
PEP8 - Python Enhancement Proposal

(1) - Utilize Camel Case para nomes de classes;


class Calculadora:
      pass


class CalculadoraCientifica:
      pass

(2) - Utilize nomes em minúsculo separados por underline para funções ou vareáveis;


def soma():
    pass


def soma_dois():
    pass

numero = 4

numero_impar = 5


(3) - Utilize 4 espaços para indentação!


if 'a' in 'banana':  ERRADO
print('teM')


if 'a' in 'banana':   CERTO
    print('teM')


(4) - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

(5) - Imports

- Imports devem ser sempre feitos em linhas separadas;

imports sys, os      ERRADO

import sys          CERTO
import os

- Não problemas em ulitizar:

from types import StringType, ListType

- Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

- Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes de cosntantes ou vairáveis globais.

(6) - Espaçoes em expressões e instruções

 # Não faça:

  funcao( algo[ 1 ], { outro: 2 } )

 # Faça:

  funcao(algo[1], {outro: 2})

  # Não faça:

  algo (1)

  # Faça:

  algo(1)

(7) Termine sempre uma instrução com uma nova linha:
"""


