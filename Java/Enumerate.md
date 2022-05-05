## ENUMERATE

Enums são usados quando você possui um conjunto de valores que nao mudam, como os dias da semana.

O exemplo abaixo mostra como declarar um enumerate:

```java 
public enum DaysOfTheWeek {
  SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY;
}
```
No exemplo abaixo é armazenado um dos valores do enum dentro da varias days:

``` java
  public class TestEnums {
    public static void main(String[] args) {

        DaysOfTheWeek days = DaysOfTheWeek.FRIDAY;
  }
```

Alem disso, o enum pode receber atributos, métodos e contrutor como por exemplo o atributo *"happines"*, que mede a felicidade nos dias da semana:

```java 
public enum DaysOfTheWeek {
  SUNDAY(5), MONDAY(3), TUESDAY(4), WEDNESDAY(6), THURSDAY(7), FRIDAY(8), SATURDAY(10);
  
  int happiness;
  
  DaysOfTheWeek(int happiness){
    this.happiness = happiness;
  }
}
```
Ao colocar atributos nele, é preciso especificar seu constructor e o valor do atributo, como no exemplo acima.

Após estruturar o enum, você precisa armazenar seu valor dentro de uma variável:

```java
public class TestEnums {
    public static void main(String[] args) {

        DaysOfTheWeek days = DaysOfTheWeek.FRIDAY;

        System.out.println(days.happines);
    }
}
```
A variável **"days"** recebe o valor **"FRIDAY"** e consequentemente o valor do atributo **"happiness"**.

### Conclusão:

O enum é muito importante dentro da programação em Java pois é utilizado para armazenar ***valores que não seram mudados ao longo da aplicação***, como dias da semana, estações do ano e meses do ano. No entanto esse fato também pode vir a ser um problema, pois deve-se pensar muito bem que tipo de dado sera armazenado no enum, para que futuramente não seja necessário alteração no código fonte apenas para alterar um enum que não deveria ser constante. 

#### Algumas vantagens do uso do enum:

  - Deixar o código mais limpo, facilitando sua manutenção e leitura.
  - Proteger seu código, para que o usuário não possa alterar os valores definidos.
  - Permite o uso de atributos, construtores e métodos.
 



