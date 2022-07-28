"""
Entendendo o **kwargs

Poderíamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs
Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em um tupla,
o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário

# Exemplo


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# Obs: nem os parâmetros *args e **kwargs não são obrigatórios

cores_favoritas()

cores_favoritas(gabriel="azul")

# Exemplo mais complexo


def comprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é'


print(comprimento_especial(geek="Python"))

print(comprimento_especial(geek="oi"))

# Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs

# Importande manter a ordem dos parâmetros na declaração

# def mostrar_info(parametros_obrigatorios, *args, parametros default, **kwargs):

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'gabriel', 'sobrenome': 'rosa'}

print(mostra_nomes(**nomes)) -> Desempacota o dicionário nomes

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'gabriel', 'sobrenome': 'rosa'}

print(mostra_nomes(**nomes))

# OBS: Os nomes das chaves no dicionário devem ser o mesmo dos parâmetros da função IMPORTANTE
"""


