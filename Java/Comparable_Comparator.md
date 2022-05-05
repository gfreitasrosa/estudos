Um problema recorrente idependente da linguagem de programação é o de ordenar listas ou outros iteraveis, 
no Java quando se trata de uma lista de **String** ou **Integer** esse processo fica bem simples, pois existe uma coleção que auxilia nessa ordenação.

#### EXEMPLO:

  ``` java 
  import java.util.List;
  import java.util.ArrayList;
  import java.util.Collections;
  ```
  ```Essas linhas de comando importam as classes e métodos da coleção "util" que são necessárias para o exemplo. ```
  ``` java
  List<String> list = new ArrayList<>();
  
  list.add("Ola");
  list.add("Tchau");
 
  ```
  ``` O exemplo acima instancia um objeto chamado "list" da classe List, para que possam ser adicionados valores a ela como exemplificado. ```
  
  ``` java
  Collections.sort(list);
  ```
  ``` Como a lista usada no exemplo possuí valores do tipo "String" o método ".sort" da classe "Collections" ordena essa lista em ordem alfabética como padrão. ```
  
  ``` Caso a lista possuisse valores o tipo "Integer" ela seria ordenada em ordem crescente. ```
  
  
  #### Mas e se eu criar uma lista instanciando um Objeto a partir de uma Classe criada por mim ? Consigo ordena-la? Sim, mas com alguns ajustes. Para isso existe o **Comparable** o **Comparator**!
  
  ## Comparable
  
  *Comparable* é uma interface utilizada para definir o padrão de ordenação do "Collections.sort". 
  A classe "String" e "Integer" já implementam essa interface como padrão no java.
  
  #### EXEMPLO
  
  ``` java
  public Conta implements Comparable {
  
  private int numero;
  private String titular;
  ```
  ``` O código acima cria uma Classe chamada "Conta" com dois atributos "numero" e "titular" e implementa nela a interface "Comparable" ```
  ```java 
  public int compareTo(Conta outraConta){
    if (this.numero < outraConta.numero){
      return -1;
    }
    if (this.numero > outraConta.numero){
      return 1;
    }
    return 0;
  }
  ```
  ``` O método acima é da interface "Comparable", ele faz com que o "Collections.sort()" agora realize essa lógica e ordene a lista pelo atributo "numero", então agora podemos chamar o método "Collections.sort()" que o programa será compilado sem erro. ``` 
  
  Mas e se eu quiser ordenar pelo nome do titular da conta? Nesse caso utilizamos o **Comparator**!
  
  ## Comparator
 
  A interface "Comparator" possuí um método que recebe dois objetos do mesmo tipo e compara eles.
  
  ```java 
  int compare(T o1, T o2);
  ```
  Instanciaremos então um objeto como no exemplo abaixo:
  
  ```bash
   Comparator<Conta> com = new Comparator<Conta>() {
    public int compare(Conta o1, Conta o2) {
      return o1.getNome().compareTo(o2.getNome());
      }
   };
  ```
  
  ``` O método acima utiliza o método "CompareTo" da classe "String" e então compara os valores passamos como parâmetro para ele.```
  
  Após isso instanciamos um objeto da Classe que acabamos de criar e chamamos o método Collections.sort denovo.
  
  ```java
  Collections.sort(lista, com);
  ```
  ``` O código acima compara os valores da lista e retorna pra gente os objetos com nome do titular em ordem crescente.```
  
  ## CONCLUSÃO
  
  Após estudar um pouco sobre **Comparable** e **Comparator** eu concluo que a interface "Comparable" é melhor utilizada quando precisa-se ordenar por atributos numericos e de maneira natural, ja que a lógica é padrão, já o "Comparator" não precisa nem ser implementado para funcionar, e é melhor utilizado quando precisamos ordenar Strings ou criar lógicas própias de ordenação.
  
  
