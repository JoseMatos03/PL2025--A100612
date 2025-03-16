# 📌 TPC6 - Calculadora Aritmética Recursiva

📅 **Data:** 2025-03-16
👤 **Autor:** José Matos - A100612
![Foto do Autor](../foto.JPG)

---

## 🏝️ Resumo

Neste TPC foi desenvolvido um parser recursivo para expressões aritméticas utilizando **Python** com as bibliotecas **PLY** (ply.lex e ply.yacc). O projeto permite analisar expressões como `2+3x2` ou `2x7-5x3`, realizando o cálculo dos resultados durante o processo de parsing.

- ✅ **Tokenização:** Identificação de números e operadores (`+`, `-`, `x`) através de expressões regulares.
- ✅ **Análise Recursiva:** Definição de regras gramaticais que garantem a correta precedência dos operadores.
- ✅ **Cálculo Integrado:** Cada regra retorna o resultado parcial, permitindo o cálculo completo da expressão.
- ✅ **Interatividade:** Testes com expressões pré-definidas e um modo interativo para avaliação via linha de comando.

## 📁 Resultados

Os ficheiros resultantes deste TPC são os seguintes:

- 📝 [Código Fonte - parser.py](./parser.py)
- 📝 _Ficheiros gerados automaticamente pela biblioteca PLY:_ `parser.out` e `parsetab.py`

## 🔍 Estrutura do Programa

O programa foi organizado de forma modular, com as seguintes fases principais:

### 1️⃣ **Análise Léxica**

- **Definição dos Tokens:**
  Utilizou-se a biblioteca **PLY** para definir os tokens que representam números (`NUMBER`) e os operadores de adição (`PLUS`), subtração (`MINUS`) e multiplicação (`MULT`, representado por `x`).

- **Expressões Regulares e Tratamento de Espaços:**
  Foram usadas expressões regulares para identificar os tokens, ignorando espaços e tabs, garantindo que apenas os elementos relevantes sejam processados.

### 2️⃣ **Análise Sintática e Cálculo**

- **Gramática Recursiva:**
  As regras gramaticais foram definidas para `expression`, `term` e `factor`, de forma a respeitar a precedência dos operadores (multiplicação com maior prioridade que adição e subtração).

- **Cálculo Durante o Parsing:**
  Cada regra gramatical realiza a operação correspondente (adição, subtração ou multiplicação) e retorna o valor parcial, permitindo obter o resultado final da expressão de forma recursiva.

- **Tratamento de Erros:**
  Mecanismos de tratamento de erros foram implementados para identificar e tratar erros de sintaxe durante a análise.

### 3️⃣ **Interatividade e Testes**

- **Exemplos de Expressões:**
  Foram testadas expressões como `2+3x2` (resultado esperado: 8) e `2x7-5x3` (resultado esperado: -1), demonstrando a eficácia do parser.

- **Interface Interativa:**
  O programa permite que o utilizador insira expressões via linha de comando, avaliando-as em tempo real e mostrando os resultados.

---

> Universidade do Minho - 2025
