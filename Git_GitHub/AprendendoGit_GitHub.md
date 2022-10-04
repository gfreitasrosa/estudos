## GIT 

Ferramenta de versionamento e gerenciamento de código, a qual possibilita ao desenvolvedor salvar, editar e excluir diferentes versões do seu código, alem de facilitar o trabalho de diversos programadores em um mesmo projeto.

## GIT HUB

Plataforma online que acabou se tornando uma rede social, na qual é possível armazenar seus projetos, auxiliar em projétos *open source*, seguir outros desenvolvedores e relizar revisões de código, dentre outras inumeras funções. 

 ## Principais conceitos GIT

   - Branch -> São *ramificações* criadas durante o processo de desenvolvimento, para que as alterações futuras não atrapalhem o funcionamento do código.
   - Commit -> É a ação de salvar as mudanças feitas no código.
   - Push -> Atualiza seu repositório remoto (Git Hub) com as mudanças salvas no ultimo *Commit*.
   - Pull -> Atualiza seu código local com o reposótório remoto. 
   - Merge -> Cria um novo commit na branch escolhida para juntar os commits, a linha temporal do commmits é mantida.
   - Rebase -> Junta os commits na branch escolhida, porém sem precisar de um novo commit. O commits continuam linear, porém a linha temporal não é mantida.
   - Stash -> Guarda modificações (WIP) para continuar trabalhar nela em outro momento
   - Tags -> Cria tags com nome e anotações do estado atual do projeto
   - Revert -> Apaga modificações de um commit quando necessária, não perde do histórico as mudanças feitas
   
## Principais comandos GIT

```Clone um repositório remoto para a sua máquina:```
```bash
   git clone <url do repositório>
```
``` Inicializa um repositório git vazio: ```
```bash
    git init 
```
``` Adiciona os arquivos modificados para a área de "espera", para realizar um commit: ```
``` bash 
   git add <nome do arquivo>
```
``` Mostra as modificações pendentes:  ```
``` bash 
   git status
```
``` Salva as alterações feitas: ```
``` bash 
   git commit -m "título do commit"
```
``` Modifica o nome da branch atual: ```
``` bash 
   git branch -m "novo nome"
```
``` conecta o git local com seu repositório do Git Hub: ```
``` bash 
   git remote add origin <link do repositório do git hub>
```
``` Envia as mudanças para o repositório remoto: ```
``` bash 
   git push origin main
```
``` Cria uma nova Branch e ""entra nela"": ```
``` bash 
   git checkout -b "nome da branch"
```
``` Navega para a Branch selecionada: ```
``` bash 
   git checkout "nome da branch"
```
``` Realiza o merge entre a branch que o usuário está com a branch escolhida:```
```bash 
   git merge <nome da branch>
```
``` Realiza o rebase entre a branch que o usuário está e branch escolhida```
```bash
  git rebase <nome da branch>
```
``` Cria atalho para os comandos ```
```bash
git config --global alias.<atalho> <comando>
```
``` Cria um tag ```
``` bash
git tag -a 1.0.0 -m "Versão 1 finalizada"
```
``` Faz um revert ```
```bash
git revert <hash do commit>
```
```Apaga tags ou branchs```
```bash
git push origin main :<nome da tag ou da branch>
```
``` Restaura um arquivo que está na fase de Modified, antes da área de Staged ```
``` bash
git restore <nome_do_arquivo>
```
``` Restaura um arquivo que está na fase de Staged para a fase de Modified ```
``` bash
git restore --staged <nome_do_arquivo
```
[<img width="30" src="https://cdn-icons-png.flaticon.com/512/137/137518.png" alt="" title="" class="loaded">](/README.md)
