"""
Dicionários

OBS: Em algumas linguagens de programação eles são conhecidos por Mapas, como em Java.

Dicionários são coleções do tipo cahve/valor

Dicipnários são representados por cahve {}.

# EXEMPLO:

    paises = dict(br='Brasil', eua='Estados Unidos') - EXEMPLO 1
    paises = {"br" : "Brasil", "eua": "Estados Unidos"} - EXEMPLO 2 (MAIS RECOMENDADO)

    print(paises)


OBS: Sobre dicionários
    - Chave e valor são separadfos por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Acessando elementos

# FORMA 1 - Acessando via chave

    print(paises["br"])

    print(paises.get('ru')) # RETORNA UM "KeyError"

# FORMA 2 - Acessando via get - RECOMENDADA

    print(paises.get('br'))

    print(paises.get('ru')) # Ao tratar de uma chave que não contém valor ele retorna o tipo de dado None

    pais = paises.get('br', 'Não encontrado') - Podemos informar um valor padrão para caso não seja encontrado valor na chave

# Podemos verificar se determinada chave se encontra no dicionário

    print('br' in paises) >> True
    print('Estado Unidos' in paises) >> False (Não é uma chave, sim um valor)

# Podemos utilizar qualquer tipo de dados como chave para os dicionário (listas, tuplas, strin, int, boolean, float, dicionário)

# Adicionar valores

# FORMA 1

    paises['ru'] = 'Russia' - MAIS COMUM

# FORMA 2

    paises.update({'ch': 'China'})

# Atualizar dados

# FORMA 1

    paises['br'] = 'Brasilia'

# FORMA 2

    paises.update({'br': 'Brasilia'})

# CONCLUSÃO -> EM DICIONÁRIO NÃO PODEMOS TER CHAVES REPITIDAS


"""
paises = dict(br='Brasil', eua='Estados Unidos')




