# 📌 TPC1 - Somador On/Off

📅 **Data:** 2025-02-12
👤 **Autor:** José Matos - A100612
![Foto do Autor](../foto.JPG)

---

## 🏝️ Resumo

Neste TPC foi desenvolvido um programa em Python que processa um texto e soma todas as sequências de dígitos encontradas, seguindo regras de ativação e desativação baseadas nas palavras "On" e "Off". O resultado é impresso ao encontrar o caractere "=".

Os principais objetivos foram:

- ✅ Implementar a soma condicional de sequências de dígitos dentro de um texto.
- ✅ Desenvolver a lógica de ativar/desativar a soma ao encontrar "On" e "Off".
- ✅ Exibir a soma ao detectar o caractere "=" no texto.
- ✅ Estruturar o programa segundo a pipeline de análise lexica e semântica.

## 📁 Resultados

Os ficheiros resultantes deste TPC são os seguintes:

- 📝 [Código Fonte](./on_off_adder.py)

## 🔍 Estrutura do Programa

O programa foi estruturado seguindo a abordagem ensinada em aula, dividindo o processamento em duas fases:

### 1️⃣ **Análise Léxica**

Nesta fase, o programa percorre o texto e converte-o em uma lista de tokens. Os tokens podem representar:

- **ON**: Ativa a soma dos números subsequentes.
- **OFF**: Desativa a soma dos números subsequentes.
- **EQUALS**: Indica que o resultado da soma deve ser impresso.
- **NUMBER**: Representa uma sequência de dígitos convertida em um valor inteiro.

Para isso, foi utilizada uma função de tokenização que percorre o texto e agrupa caracteres de forma a identificar corretamente cada token.

### 2️⃣ **Análise Semântica**

Depois de realizada a análise léxica, a lista de tokens é processada para aplicar as regras do somador:

- Se o estado estiver **ativado (ON)**, os valores numéricos encontrados são somados.
- Se o estado estiver **desativado (OFF)**, os valores numéricos são ignorados.
- Quando um token **EQUALS** é encontrado, a soma é impressa.

## 📃 Notas Adicionais

- A implementação garante que a análise léxica gera tokens corretos, que depois são interpretados na fase semântica.
- A divisão em fases facilita futuras melhorias, como a adição de novos comandos ou modificações nas regras de funcionamento.
- Caso não haja o caractere "=", o programa encerra sem imprimir resultados.

---

> Universidade do Minho - 2025
