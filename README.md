# Jogo da Velha em Python

Projeto desenvolvido como teste de consolidação dos conhecimentos adquiridos durante meus estudos introdutórios de programação e lógica de programação.

O objetivo principal não foi apenas desenvolver um Jogo da Velha funcional, mas utilizar o projeto como uma avaliação prática da minha capacidade de transformar um problema em uma solução computacional, estruturando a lógica, decompondo o problema em etapas e implementando a solução utilizando Python.

Este projeto marca uma etapa importante do meu processo de aprendizagem: sair da resolução de exercícios isolados e aplicar os conceitos estudados na construção de um programa completo.

---

## 🎯 Objetivo do Projeto

O projeto foi proposto por mim mesmo como um teste final da etapa de **Introdução à Programação** e **Lógica de Programação**.

Ao longo dos estudos, foram trabalhados conceitos fundamentais como:

* Algoritmos
* Variáveis e constantes
* Tipos de dados
* Operadores aritméticos, relacionais e lógicos
* Estruturas condicionais
* Estruturas de repetição
* Funções
* Parâmetros e argumentos
* Retorno de funções
* Listas e estruturas de dados
* Manipulação de strings
* Modularização
* Validação de entrada
* Controle de fluxo
* Raciocínio lógico
* Teste de mesa
* Depuração e identificação de erros
* Git e GitHub

O Jogo da Velha foi utilizado para verificar a capacidade de aplicar esses conceitos de forma integrada em um problema que exige diversas decisões lógicas.

---

## 🎮 Sobre o Jogo

O programa implementa uma versão do clássico Jogo da Velha executada diretamente no terminal.

Dois jogadores alternam suas jogadas utilizando os símbolos **X** e **O**. A cada rodada, o programa apresenta o tabuleiro, solicita a posição desejada e verifica se a jogada é válida.

O jogo termina quando:
1. Um dos jogadores consegue formar uma linha com três símbolos;
2. Todas as posições são preenchidas sem que exista um vencedor (empate).

---

## ✨ Funcionalidades

* Exibição do tabuleiro no terminal;
* Alternância entre jogadores;
* Validação das jogadas;
* Impedimento de ocupar uma posição já utilizada;
* Verificação das possibilidades de vitória;
* Identificação de empate;
* Encerramento da partida quando existe um vencedor;
* Destaque visual do resultado utilizando a biblioteca **Rich**.

---

## 🧠 Conhecimentos Aplicados

### Variáveis e Tipos de Dados
O projeto utiliza variáveis para representar informações como:
* Jogador atual;
* Posição escolhida;
* Estado das posições do tabuleiro;
* Resultado da partida.

Esses dados são manipulados de acordo com o fluxo de execução do programa.

### Estruturas Condicionais
As estruturas condicionais são utilizadas para tomar decisões durante a execução, como:
* Verificar se uma posição é válida;
* Verificar se uma posição já está ocupada;
* Identificar uma condição de vitória;
* Identificar um empate;
* Determinar qual jogador deve realizar a próxima jogada.

### Estruturas de Repetição
Os laços de repetição permitem manter a partida em execução enquanto nenhuma condição de encerramento foi atingida.

Esse foi um dos pontos importantes do projeto, pois exigiu compreender não apenas como repetir uma operação, mas qual deve ser a condição responsável por interromper a repetição.

### Funções
O projeto utiliza funções para dividir o problema em responsabilidades menores.

Essa abordagem permite evitar que toda a lógica fique concentrada em um único bloco de código e facilita a leitura, manutenção e depuração do programa.

### Estruturas de Dados
O tabuleiro é representado utilizando uma estrutura de dados capaz de armazenar e modificar as posições da partida.

A escolha dessa representação também foi um exercício de raciocínio lógico: era necessário determinar como uma posição visual do tabuleiro poderia ser relacionada a uma posição dentro da estrutura utilizada pelo programa.

### Validação de Entrada
O programa precisa lidar com entradas que não podem ser aceitas pela lógica do jogo.

Por isso, antes de realizar uma jogada, é necessário verificar se a entrada fornecida pelo jogador corresponde a uma posição válida e disponível.

Esse processo reforça um conceito importante de programação: **não devemos assumir que a entrada fornecida pelo usuário está correta.**

---

## 🚀 O que este projeto representa no meu aprendizado

Este projeto possui uma finalidade diferente dos exercícios realizados durante os estudos.

Nos exercícios, normalmente o problema já apresenta uma estrutura relativamente definida: calcular um valor, percorrer uma sequência, criar uma função ou implementar determinada operação.

No Jogo da Velha, o problema é mais aberto. Antes de escrever o código, foi necessário pensar em perguntas como:

* Como representar o tabuleiro?
* Como representar o estado de cada posição?
* Como determinar a vez de cada jogador?
* Como validar uma jogada?
* Como identificar todas as possibilidades de vitória?
* Como detectar um empate?
* Quando o programa deve continuar executando?
* Quando a partida deve terminar?
* Como dividir o programa em funções?
* Como evitar que uma alteração em determinada parte prejudique outra parte do programa?

Essa característica torna o projeto um exercício mais próximo do desenvolvimento de software do que da simples resolução de exercícios de sintaxe.
