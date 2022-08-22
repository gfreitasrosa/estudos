"""
Atributos representam as características do objeto

em Python, dividímos os atributos em 3 grupos:

    - Atríbutos de instância;
    - Atríbuto e Classe;
    - Atributos Dinâmicos;

# Atríbutos de instância: São atributos declarados dentro do método construtor

# OBS: Método construtor é um método especial utilizado para a construção do objeto

# Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é publico, caso queiramos demonstrar
que determinado atributo deve ser tratado como privado, utiliza-se __ dublo underscore no inìcio de seu nome.

Isso é conhecido também como Name MangLíng
"""


class Lampada:

    def __init__(self, voltagem, cor):  # Constructor
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, limite, saldo):
        self.limite = limite
        self.saldo = saldo


# Atributos publícos e privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha


# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai empdir que façamos
# acesso aos atributos sinalizados como privados fora da classe

user = Acesso('user@gmail.com', '12345')

print(user.email)

# print(user.__senha)  Atribute error

print(dir(user))

print(user._Acesso__senha)  # Temos acesso, mas não devemos fazer acesso dessa forma. (Name Manglíng)


# O que significa atributos de instância?

# Significa, que ao criarmos instâncias/objetos d euma classe, todas as instaâncias terâo estes atributos.

# Atributos de Classe

# Atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja,
# fora do construtor. Geralmente já inicializamos um valor e este valor é compartilhado entre
# todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios
# valores como é o caso dos atributos de instâcia, com os atributos de classe todas as instâncias
# terão o mesmo valor para este atributo.


class Produto:
    imposto = 1.05  # Atributo de classe

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

# OBS: Em java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos;

# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou

p1 = Produto('ps4','video game', 1200)

p1.peso = '12kg'  # Atributo dinâmico
print(p1.peso)

del p1.peso # Remover atributos, tanto dinâmicos como de instância

print(p1.__dict__) 