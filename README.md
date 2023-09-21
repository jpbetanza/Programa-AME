# Programa AME

Esse é um projeto juntando o Departamento de Saúde Coletiva da UFRN e o laboratório TEAM. Trata-se de um site local, que adiquirá diversas informações sobre hábitos alimentares e físicos de alunos do ensino fundamental nas escolas da cidade.

## Começando

Essas instruções farão com que você consiga ter uma cópia funcional desse projeto na sua máquina, para ver como ele funciona.

### Pre-requisitos

O que você precisará para fazer o servidor local funcionar

```
[Python](https://www.python.org/) - Linguagem de programação
```

### Instalando

Primeiro, baixe o [Python](https://www.python.org/) do seu site oficial e instale-o em sua máquina (SELECIONE A CAIXA "ADD TO PATH" NO COMEÇO DA INSTALAÇÃO, CASO CONTRÁRIO NÃO FUNCIONARÁ).

Após a instalação do Python, é necessário realizar o download dos arquivos do repositório. Baixando o arquivo .zip, você pode extrair a pasta em um local de seu agrado.

Inicie o programa batch "StartApp.bat" e aguarde até que todos os comandos sejam executados e apareça um endereço para acesso do site.

Acesse o site por qualquer navegador pelo ip/porta

## O site

O site possui uma página inicial, com informações gerais sobre o programa assim como links que acessarão os testes.
Cada aluno teria um código pré-definido ao inicio dos testes, e eles usariam esses códigos para armazenar suas respostas num banco de dados.
O primeiro deles é um formulário bem grande que, na verdade está disponível no google forms e é acessado por um iframe no site.
O segundo é um questionário que, deveria estar dentro do primeiro formulário mas, não foi possível re-escrever as perguntas dentro do google forms, então foi necessario um espaço dedicado à ele.
Por último, há um 'jogo' chamado 'Stroop test', ele brinca com cores e palavras a fim de testas as capacidades cognitivas dos alunos.

## Feito com

* [Python](https://www.python.org/) - Linguagem de programação
* [Django](https://www.djangoproject.com/) - O framework Web
* [Bootstrap](https://getbootstrap.com/) - Toolkit para CSS, HTML e JS

## Autores

* **João Pedro Betanza** - [jpbetanza](https://github.com/jpbetanza)
