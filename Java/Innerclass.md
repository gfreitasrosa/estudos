## Inner Class

Inner Class em Java nada mais é do que uma classe dentro de outra classe, mas como assim?

### Exemplos:

``` java
public class Teste {

  String name;
  
  public void teste(){
  
    System.out.println("Teste");
  
    public class InnerClassTeste{

      public void testeInner(){

        System.out.println("Teste Inner Class");

     }
     
     InnerClassTeste inner = new InnerClassTeste();
     
     inner.testeInner();
   }
}
```

``` No exemplo acima criamos uma Inner Class dentro do método 'teste' da classe 'Teste', e criamos uma objeto a partir dessa Inner Classe para executar um método seu```

``` Ao isntanciar um objeto da classe Teste e executar seu método 'Teste' além de printar a string "Teste" ele tambem criara a inner classe, instanciara o objeto e executara o método chamado pelo objeto```

``` A saída no sistema ficaria assim:```

```bash

Teste
Teste Inner Class

```
