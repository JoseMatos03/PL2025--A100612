# 📌 TPC2 - Parser de CSV

📅 **Data:** 2025-02-20
👤 **Autor:** José Matos - A100612
![Foto do Autor](../foto.JPG)

---

## 🏝️ Resumo

Neste TPC foi desenvolvido um programa em Python que processa ficheiros CSV sem recorrer à biblioteca nativa do Python. O parser foi implementado seguindo uma pipeline de três fases: análise léxica, análise sintática e análise semântica. O programa é capaz de ler ficheiros CSV com um delimitador (que pode ser definido manualmente) e de lidar com campos entre aspas (incluindo aspas duplas escapadas).

Os principais objetivos foram:

- ✅ Implementar a tokenização do ficheiro CSV utilizando expressões regulares.
- ✅ Processar os tokens para construir uma estrutura de dados representando as linhas e os campos.
- ✅ Extrair e organizar os dados semânticos: uma lista de compositores ordenada alfabeticamente, a distribuição de obras por período, e um dicionário que associa cada período aos títulos das peças musicais.
- ✅ Seguir a pipeline de análise (léxica, sintática e semântica) estudada nas aulas teóricas.

## 📁 Resultados

Os ficheiros resultantes deste TPC são os seguintes:

- 📝 [Código Fonte](./csv_parser.py)

## 🔍 Estrutura do Programa

O programa foi estruturado em três fases:

### 1️⃣ **Análise Léxica**

Nesta fase, o programa:

- Remove caracteres de controlo (como o carriage return).
- Utiliza uma expressão regular para identificar tokens, que incluem:
  - **DELIMITER**: Representa o delimitador ";".
  - **NEWLINE**: Indica a quebra de linha.
  - **QUOTE**: Identifica as aspas que delimitam os campos.
  - **CHAR**: Agrupa sequências de caracteres que não são delimitadores, novas linhas ou aspas.

### 2️⃣ **Análise Sintática**

Nesta fase, os tokens são processados para construir uma estrutura de dados (lista de listas) que representa as linhas e os campos do ficheiro CSV. A implementação:

- Gerencia corretamente campos entre aspas, inclusive aqueles que contêm aspas duplas escapadas.
- Separa os campos utilizando o delimitador ";".
- Reconhece e trata as quebras de linha para finalizar as linhas.

### 3️⃣ **Análise Semântica**

Após a construção da estrutura de dados, a fase semântica extrai as informações relevantes:

- **Lista de Compositores:** Uma lista ordenada alfabeticamente, obtida a partir dos campos correspondentes.
- **Distribuição de Obras por Período:** Um dicionário que conta o número de obras em cada período.
- **Títulos por Período:** Um dicionário que associa cada período aos títulos das peças musicais.

## 📃 Notas Adicionais

- O parser está preparado para processar ficheiros CSV que contenham campos com aspas e múltiplas linhas, respeitando as regras de formatação do CSV.
- Caso o ficheiro não esteja no formato esperado, linhas incompletas podem ser ignoradas para manter a consistência dos dados.

---

> Universidade do Minho - 2025
