"""
Módulo collections - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dicionário,
contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrencias dessse elemento.

# Utilizando o Counter

    from collections import Counter

    # Exemplo 1

        from collections import Counter

        list = [1, 2, 3, 4, 5, 1, 1, 2, 2]

        test_counter = Counter(list)

        print(test_counter)
        print(type(test_counter))

        # veja que para cada elemento da lista o Counter criou uma cahve e colocou como valor a quantidade de ocorrencias.

        from collections import Counter

    Exemplo 2

        print(Counter("Gabriel de Freitas Rosa"))
        ## >> Counter({'a': 3, 'e': 3, ' ': 3, 'r': 2, 'i': 2, 's': 2, 'G': 1, 'b': 1, 'l': 1, 'd': 1, 'F': 1, 't': 1, 'R': 1, 'o': 1})

    Exemplo 3

        text = '''
        Lorem Ipsum is simply dummy text of the printing and typesetting industry.
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        It has survived not only five centuries, but also the leap into electronic typesetting,
        remaining essentially unchanged. It was popularised in the 1960s with the release of
        Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software
        like Aldus PageMaker including versions of Lorem Ipsum.'''

        words = text.split()

        res = Counter(words)

        print(res)

        print(res.most_common(5)) # Encontrando as cinco palavras com mais ocorrências no texto.

"""

"""
Módulo collections - Default Dict

dic = {'curso': 'Programação em Python'}

print(dic)

print(dic['curso'])

print(dic['outro']) # KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default, 
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um valor definido.


OBS: Lambdas são funcoes sem nome, que podem ou nao receber parametros de entrada e retornar valores

from collections import defaultdict

dicionario = defaultdict(lambda: 0) -> Caso a chave não exista durante a pesquisa ela é criada com um valor default de 0

dicionario['curso'] = 'python'

print(dicionario['outro']) # Key Error no dicionario comum, mas aqui não

print(dicionario)


"""
"""
Módulo collections - Ordened Dict

É um dicionário que nos garante a ordem de inserção dos elementos

# Exemplificando a diferença entre Dict e Ordered Dict

    # Dict
    
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 2, 'a': 1}
        
        print(dict1 == dict2) >> True
    
    # Ordened Dict
    
        dict1 = OrderedDict({'a': 1, 'b':2})
        dict2 = OrderedDict({'b': 2, 'a':1})
        
        print(dict1 == dict2) >> False -> A ordem faz diferença
"""
"""
Módulo collections - Named Tuple

# Recap Tupla
tupla = (1, 2, 3)

print(tupla[1])

Named Tuplas -> São tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros

# Importanto
    
    from collections import namedtuple

# Precisamos definir o nome e parâmetros

    # Forma 1 - Declaração Named Tuple
    
    cachorro = namedtuple('cachorro', 'idade raca nome')
    
    # Forma 2 - Declaração Named Tuple
    
    cachorro = namedtuple('cachorro', 'idade, raca, nome')
    
    # Forma 3 - Declaração Named Tuple
    
    cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

    ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
    
    print(ray)

# Acessando os dados

    # Forma 1
    
    print(ray[0])
    print(ray[1])
    print(ray[2])
    
    # Forma 2 -> Melhor maneira
    
    print(ray.idade)
    print(ray.raca)
    print(ray.nome)



"""


