"""
Definindo funções

- Funções são pequenos trechos de código que realizam tarefa específicas;
- Pode ou não receber entradas de dados e retornar um saida de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escreve uma função que realzia varias tarefas dentro dela, é bom fazer uma verificação
para que a função seja simplificada

# DRY -> Don´t Repeat Yourself / Não repita seu código

nome_da_funcao -> SEMPRE, com letrar minusculas e se for nome composto, separado por underline (Snake Case)
parametros_de_entrada -> Opcionais, podendo ser mais de um ou não
bloco_da_funcao -> Pode ter retorno ou não

Exemplo:

    def exemplo_funcao:
        bloco_de_codigo

OBS: Em Python quando uma função não retorna nenhum valor o retorno é None

Return ->

    1 - Ela finaliza a função
    2 - Podemos ter mais de um return na função
    3 - Podemos em uma função retornar qualquer tipo de dado e até mesmo multiplos valores

Funções com parâmetro:

    - Funções podem ter N parâmetros de entrada, de diferentes tipos e separados por vírgula separados por vírgula
         Exemplo: def soma(a, b):
                    return a + b

# Argumentos Nomeados (Keywords Arguments)

def nome_completo(nome, sobrenome):

    return nome + " " + sobrenome

print(nome_completo(nome="Gabriel", sobrenome="Rosa"))

* Funcões com Parâmetro Padrâo (Default Paramters)

- funcões onde  passagem de parâmetro seja opcional;

Exemplos:

    def exponencial(numero, potencia=2):
        return numero ** potencia

    print(exponencial(2))

    print(exponencial(2,3))


# Os parâmetros default SEMPRE serão colocados por ultimos, exemplo:

    def exponencial(numero=2, potencia): -> ERRADO

    def exponencial(numero, potencia=2): -> CERTO

# OBS: Se tivermos uma variável global e uma local, a preferência será para a variável local.

# Atenção com variáveis globais (Se puder evitar, evite!)

"""





