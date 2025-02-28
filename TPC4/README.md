# 📌 TPC4 - Analisador Léxico SPARQL com PLY

📅 **Data:** 2025-02-28
👤 **Autor:** José Matos - A100612
![Foto do Autor](../foto.JPG)

---

## 🏝️ Resumo

Neste TPC foi desenvolvido um analisador léxico para a linguagem de consultas **SPARQL**, implementado em **Python** utilizando a biblioteca **PLY**. O objetivo foi reconhecer os principais tokens de uma query SPARQL, incluindo variáveis, prefixos, strings, chaves, pontos, etc.

Os principais objetivos foram:

- ✅ **Identificar** tokens como `SELECT`, `WHERE`, `LIMIT`, variáveis SPARQL, prefixos, strings e números.
- ✅ **Ignorar** comentários que começam com `#`.
- ✅ **Implementar** tratamento de erros para caracteres inválidos.
- ✅ **Demonstrar** o uso do analisador com um exemplo.

## 📁 Resultados

Os ficheiros resultantes deste TPC são os seguintes:

- 📝 [Código Fonte](./lexer_sparql.py)

## 🔍 Estrutura do Programa

O programa foi estruturado em **uma fase principal** (Análise Léxica), mas pode ser integrado numa pipeline maior caso se deseje fazer análise sintática e semântica posteriormente.

### 1️⃣ **Análise Léxica**

Nesta fase, o programa:

- Lê o conteúdo de uma query SPARQL.
- **Tokeniza** o conteúdo, reconhecendo:
  - Palavras-chave: `SELECT`, `WHERE`, `LIMIT`, `a` (rdf:type).
  - Variáveis SPARQL (p. ex., `?s`, `?nome`).
  - Prefixos (p. ex., `dbo:MusicalArtist`, `foaf:name`).
  - Strings entre aspas duplas.
  - Tag de linguagem (p. ex., `@en`).
  - Pontos, chaves (`{`, `}`) e números.
- **Ignora** comentários que começam com `#`.
- **Regista** caracteres inválidos, avançando o analisador para não interromper a leitura.

## 📃 Notas Adicionais

- O analisador pode ser facilmente estendido para reconhecer mais construtos da linguagem SPARQL (por exemplo, `FILTER`, `OPTIONAL`, `GROUP BY` etc.).

---

> Universidade do Minho - 2025
