## GIT 

Ferramenta de versionamento e gerenciamento de código, a qual possibilita ao desenvolvedor salvar, editar e excluir diferentes versões do seu código, alem de facilitar o trabalho de diversos programadores em um mesmo projeto.

## GIT HUB

Plataforma online que acabou se tornando uma rede social, na qual é possível armazenar seus projetos, auxiliar em projétos *open source*, seguir outros desenvolvedores e relizar revisões de código, dentre outras inumeras funções. 

 ## Principais conceitos GIT

   - Branch -> São *ramificações* criadas durante o processo de desenvolvimento, para que as alterações futuras não atrapalhem o funcionamento do código.
   - Commit -> É a ação de salvar as mudanças feitas no código.
   - Push -> Atualiza seu repositório remoto (Git Hub) com as mudanças salvas no ultimo *Commit*.
   - Pull -> Atualiza seu código local com o reposótório remoto. 
   - Merge -> Junta as mudanças de diferentes *Branchs*.

## Principais comandos GIT

``` Inicializa um repositório git vazio. ```
```bash
    git init 
```
``` Adiciona os arquivos modificados para a área de "espera", para realizar um commit. ```
``` bash 
   git add <nome do arquivo>
```
``` Mostra as modificações pendentes.  ```
``` bash 
   git status
```
``` Salva as alterações feitas. ```
``` bash 
   git commit -m "título do commit"
```
``` Modifica o nome da branch atual. ```
``` bash 
   git branch -m "novo nome"
```
``` conecta o git local com seu repositório do Git Hub. ```
``` bash 
   git remote add origin <link do repositório do git hub>
```
``` Envia as mudanças para o repositório remoto. ```
``` bash 
   git push origin main
```
``` Cria uma nova Branch e ""entra nela"". ```
``` bash 
   git checkout -b "nome da branch"
```
``` Navega para a Branch selecionada. ```
``` bash 
   git checkout "nome da branch"
```

