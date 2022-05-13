## List

"List" é um interface do java que permite a criação de uma lista, para manipular valores nela.

```java 
  List<Integer> numbers;
```
No entanto para instanciar uma "List" é preciso utilizar uma das classes que a implementam, como: ```ArrayList<>()``` ou ```LinkedList<>()```. como no  exemplo abaixo:

```java 
  numbers = new ArrayList<>();
  
  numbers = new LinkedList<>();
```
A "ArrayList" é uma lista de tamanho infinito que possui rapido retorno caso necessite pesquisar um valor na lista, porém é lento caso necessite inserir um valor no início da lista, pois todos os elementos da lista serão deslocado um casa para direita. Já a "LinkedList" utiliza um conceito chamado lista ligada, o que faz com que inserir e remover valores dela seja consideravelmente mais rapido do que ja "ArrayList", porém pesquisar um valor nela é lento, já que é preciso percorrer toda a lista.

Alguns dos principais métodos das listas são:

```.add()``` -> Utilizado para adicionar valores na lista, podendo também adicionar o indice da onde sera adicionado o valor (.add(10,"Gabriel")).

```.sort()``` -> Ordena a lista de forma alfabética ou crescente.

  *Para o método ".sort()" funcionar com listas de objetos, necessitamos utilizar as interfaces [Comparable](/Java/Comparable_Comparator.md) ou [Comparator](/Java/Comparable_Comparator.md).*

```.clear()``` -> Limpa a lista.

```.remove()``` -> Recebe como parâmetro um valor que corresponde ao indíce da posição que deseja excluir.

```.contains()``` -> Verifica se a lista possui o valor passado como parâmetro.

```.get()``` -> Retorna o valor que está no índice passado como parâmetro.

Para iterar sobre uma lista o melhor método é utilizar o "foreach", como no exemplo abaixo:

```java 
  for(Integer number : numbers){
    System.out.print(number);
  }
```

## Set

"Set" é uma interface parecida com a "List" porém **NÃO ARMAZENA VALOR REPETIDOS**.

```java
  Set<Integer> numbers;
  
  numbers = new TreeSet<>();
```
O exemplo acima mostra como se implementa uma variável do tipo Set, utilizando a classe "TreeSet" assim como a List o Set é uma interface, não podendo então instanciar um objeto, o que gera a necessidade de utilizar o "TreeSet", "HashSet" ou "LinkedHashSet".

"TreeSet" -> Fornecem ordenação natural, os elementos usados como paramêtro necessitam implementar a interface "Comparable" e não aceita valores do tipo nulo.

"HashSet" -> Não tem ordenação no armazenando de dados, velocidade alta de escrita e leitura de valores e aceita valores do tipo nulo.

"LinkedHashSet" -> Mesmas características que a interfade "HashSet" porém utiliza lista ligada, que retorna os valores por ordem de inserção.

## Map

Relação de chave-valor entre os dados, um valor pode conter apenas uma chave.

```java
  Map<int, String=""> names = new TreeMap<>();
```

O exemplo acima mostra como incializar uma variavel do tipo "Map" e instaciar um objeto implementando a interface "TreeSet".


  
