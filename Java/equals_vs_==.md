## .equals() vs ==

Durante a programação em java surge a necessidade de fazer comparações de igualdade entre variáveis, e existem duas maneiras distintas de realizar isso. 

### ==

O operador ```==``` é utilizado quando necessitamos realizar a comparação entre tipos primitivos:  ```byte, short, int, long, boolean, char, float, double```..

Exemplo:

```java
  int num1 = 5;
  int num2 = 5;
  
  if (num1 == num2) {
    System.out.print("True");
  }
  else {
    System.out.print("False");
  }
```
``` No exemplo acima está sendo comparado (utilizando "==" ) o valor de duas variáveis do tipo primitivo "int"```.

### .equals()

Quando se trata de comparar dois objetos ao utilizar o operador ```==``` o java não realiza o mesmo tipo de comparação, ao fazer isso a linguagem compara o local da mémmoria no qual o objeto está armazenado e não os valores de seus atributos, por isso implementamos o método .equals() na classe.

Exemplo da estrutura do método .equals():

```java
@Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Aluno other = (Aluno) obj;
        if (id == null) {
            if (other.id != null)
                return false;
        } else if (!id.equals(other.id))
            return false;
        return true;
    }
```

``` Implemmentando o método .equals() podemos escolher quais atributos seram comparados e quais não.```

[<img width="30" src="https://cdn-icons-png.flaticon.com/512/137/137518.png" alt="" title="" class="loaded">](/README.md) 
