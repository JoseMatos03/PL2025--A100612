# 📌 TPC5 - Máquina de Vending

📅 **Data:** 2025-03-09
👤 **Autor:** José Matos - A100612
![Foto do Autor](../foto.JPG)

---

## 🏝️ Resumo

Neste TPC foi desenvolvida uma simulação de **Máquina de Vending** utilizando **Python** com a biblioteca **PLY** para a análise léxica dos comandos e um ficheiro **JSON** para a persistência do stock dos produtos. O objetivo foi criar um sistema interativo que:

- ✅ **Tokenize** os comandos de interação (tais como `LISTAR`, `MOEDA`, `SELECIONAR`, `ADICIONAR` e `SAIR`) utilizando PLY.
- ✅ **Gerencie** o stock de produtos, carregando e guardando os dados num ficheiro JSON.
- ✅ **Execute** operações de compra, verificação de saldo, cálculo de troco e atualização do stock.
- ✅ **Trate** cenários de erro, como produto inexistente, stock esgotado e saldo insuficiente.

## 📁 Resultados

Os ficheiros resultantes deste TPC são os seguintes:

- 📝 [Código Fonte - vending.py](./vending.py)
- 📝 [Ficheiro de Stock Inicial - stock.json](./stock.json)

## 🔍 Estrutura do Programa

O programa foi estruturado de forma modular, com as seguintes fases principais:

### 1️⃣ **Análise Léxica e Tokenização**

- **Definição dos Tokens:**
  Utilizou-se a biblioteca **PLY** para definir tokens que representam os comandos (`LISTAR`, `MOEDA`, `SELECIONAR`, `ADICIONAR`, `SAIR`), as moedas (ex.: `1e`, `20c`), os códigos dos produtos, strings e números.

- **Tratamento de Erros:**
  Caracteres inválidos são identificados e ignorados, garantindo que a análise não interrompa a execução.

### 2️⃣ **Processamento dos Comandos**

- **LISTAR:**
  Exibe o stock atual dos produtos com seus respectivos códigos, nomes, quantidades e preços.

- **MOEDA:**
  Converte e acumula as moedas inseridas pelo utilizador no saldo disponível.

- **SELECIONAR:**
  Permite a compra de um produto, verificando a existência, disponibilidade no stock e se o saldo é suficiente para a transação.

- **ADICIONAR:**
  Comando extra que possibilita a inserção ou atualização de produtos no stock, aumentando a flexibilidade do sistema.

- **SAIR:**
  Finaliza a interação, calcula e dispensa o troco, e grava o estado atualizado do stock no ficheiro JSON para persistência dos dados.

### 3️⃣ **Persistência dos Dados**

- **Carregamento Inicial:**
  O stock dos produtos é carregado a partir de um ficheiro JSON no arranque do programa.

- **Atualização Final:**
  Ao terminar a sessão (com o comando `SAIR`), o stock é salvo de volta no ficheiro JSON, mantendo a consistência dos dados entre execuções.

## 📃 Notas Adicionais

- A implementação abrange diversos cenários de erro, tais como produto inexistente, stock esgotado e saldo insuficiente, proporcionando uma experiência robusta.
- O comando extra **ADICIONAR** enriquece a funcionalidade, permitindo atualizar o stock de forma dinâmica durante a execução do programa.

---

> Universidade do Minho - 2025
