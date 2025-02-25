# 📌 TPC3 - Conversor de Markdown para HTML

📅 **Data:** 2025-02-25
👤 **Autor:** José Matos - A100612
![Foto do Autor](../foto.JPG)

---

## 🏝️ Resumo

Neste TPC foi desenvolvido um conversor de Markdown para HTML em Python, implementado seguindo uma pipeline de três fases: análise léxica, análise sintática e análise semântica. O programa lê um ficheiro de entrada contendo o conteúdo em Markdown e gera um ficheiro de saída com o HTML resultante.

Os principais objetivos foram:

- ✅ Implementar a tokenização do ficheiro Markdown, identificando cabeçalhos, itens de lista e parágrafos.
- ✅ Processar os tokens para construir uma estrutura sintática que organiza os elementos do documento.
- ✅ Realizar a análise semântica para converter a estrutura sintática em HTML, aplicando transformações inline para elementos como bold, itálico, links e imagens.
- ✅ Ler o conteúdo a partir de um ficheiro de entrada e guardar o resultado num ficheiro de saída.

## 📁 Resultados

Os ficheiros resultantes deste TPC são os seguintes:

- 📝 [Código Fonte](./markdown_converter.py)
- 📝 [Markdown Teste](./test.md)
- 📝 [HTML Convertido](./test.html)

## 🔍 Estrutura do Programa

O programa foi estruturado em três fases:

### 1️⃣ **Análise Léxica**

Nesta fase, o programa:

- Lê o ficheiro de entrada e divide o conteúdo em linhas.
- Identifica tokens correspondentes a:
  - Cabeçalhos (níveis 1, 2 e 3)
  - Itens de lista numerada
  - Parágrafos e linhas vazias

### 2️⃣ **Análise Sintática**

Nesta fase, os tokens são agrupados numa estrutura sintática:

- Os itens de lista consecutivos são reunidos num bloco de lista ordenada (`<ol>`).
- Cabeçalhos e parágrafos são organizados como nós individuais da árvore sintática.

### 3️⃣ **Análise Semântica**

Após a construção da árvore sintática, a fase semântica:

- Converte cada nó da árvore em HTML.
- Aplica a conversão inline para elementos de formatação (bold, itálico, links e imagens).

## 📃 Notas Adicionais

- O programa permite especificar tanto o ficheiro de entrada quanto o ficheiro de saída, facilitando a sua integração em fluxos de trabalho automatizados.

---

> Universidade do Minho - 2025
