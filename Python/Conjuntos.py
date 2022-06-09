"""
Conjuntos 

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à teoria dos Conjuntos da MATEMÁTICA.

- Aqui no Python, os Conjntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos sao bons para se utilizar quando precisamos armazenar elementos mas nao nos importamos com a ordenacao deles.
quando nao precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) sao referenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto

    # Forma 1

        s = set({1, 2, 3, 4, 5, 5, 4})

        print(s)
        print(type(s))

        # OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erros
        # e não fará parte do conjunto

    # Forma 2 = Mais comum

        s = {1, 2, 3, 4, 5, 5, 4}

# Assim como todo outro conjunto Python podemos colocar topos de dados misturados em Sets

    s = {1, "dois", 1.2, True, 'a'}

# Podemos iterar em um Set normalmente

    for valor in s:
        print(valor)

# Usos interassantes com sets

    # Imagine que fizzemos um formulário de cadastro de visitantes em uma feira ouy museu e os visitantes
    # Informar manualmente a cidade de onde vieram.

    # Nós adicionamos cada cidade em uma lista Python, já que em uma lsita podemos adicionar novos elementos e ter repetição

    cidades = ["São Paulo", "Campinas", "São Paulo"]

    print(cidades)
    print(len(cidades))

    # Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

    cidades_unicas = set(cidades) # Transformando a lista de cidades em um set de cidades, que elimina as repitidas.

    print(cidades_unicas)

    print(len(cidades_unicas))

# Conjuntos são mutáveis, podendo adicionar valores a ele como fazemos na lista

    conjunto.add(valor)

    # Duplicidade não gera erro apenas é ignorado e não é adicionado

    # Removendo valores

        # Forma 1

        s = {1, 2, 3}

        s.remove(3) (Valor não encontrado GERA um KeyError)

        # Forma 2

        s.discard(2) (NÃO GERA erro caso nao encontre o valor)

# Copiando um conjunto para outro...

    s = {1, 2, 3}

    # Forma 1 - Deep Copy (Cria um novo conjunto a partir do primeio)

        novo = s.copy()

    # Forma 2 - Shallow Copy (Ambos os conjuntos são modificado, as váriaveis possuem o msm espaço em memória

        novo = s

        novo.add(4)

        print(novo)
        print(s)

# Métodos matemáticos


# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um contendo estudantes do curso de Java

    estudantes_python = {'marcos', 'patricia', 'gabriel'}

    estudantes_java = {'gabriel', 'felipe', 'joao', 'roberto'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos

    # Forma 1 - Utilizando union (União de conjuntos em Python) -> MAIS USUAL

        unicos1 = estudantes_python.union(estudantes_java)

        # >> {'felipe', 'joao', 'gabriel', 'marcos', 'roberto', 'patricia'}

    # Forma 2 - Utilizando o caractere pipe |

        unicos2 = estudantes_python | estudantes_java

        # >> {'felipe', 'gabriel', 'joao', 'patricia', 'marcos', 'roberto'}

# Precisamos gerar um conjunto com os nomes de estudantes que fazem os dois cursos

    # Forma 1 - Utilizando intersection

        ambos1 = estudante_python.intersection(estudantes_java)

        # >> {'gabriel'}

    # Forma 2 - Utilizando &

        ambos2 = estudantes_python & estudantes_java

        # >> {'gabriel'}

# Gerar um conjunto de estudante que não estão no outro curso

    so_python = estudantes_python.difference(estudantes_java)

    so_java = estudantes_java.difference(estudantes_python
                                         )
    print(so_python)
    print(so_java)

# Soma*, Valor máximo*, valor Mínimo*, Tamanho
# sum         max           min          len
# * Se os valores forem reais

"""




