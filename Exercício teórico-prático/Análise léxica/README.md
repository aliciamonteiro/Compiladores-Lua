# Analisador Léxico para valores monetários

**Exercicio teórico-prático — Análise Léxica — 2ª Avaliação**

Este programa implementa um analisador léxico capaz de reconhecer e validar valores monetários em diferentes formatos, utilizando expressões regulares.

**Autores:** Alicia Monteiro, Eduardo Couto, Kleiton Josivan, João Vitor Fernandes e Robert Danilo  
**Data:** 30/11/2025

---

## Funcionalidades

O analisador é capaz de:

- **Validar valores monetários** no formato brasileiro  
- Suportar símbolos como `R$`, `$`, `USD$`, `BRL$`  
- Reconhecer **sinal negativo após o símbolo** (ex.: `R$-500,50`)  
- Aceitar valores negativos entre **parênteses** (ex.: `(R$500,50)`)  
- Detectar erros como:
  - zeros à esquerda  
  - ausência de símbolo monetário  
  - separadores incorretos  
  - formato decimal inválido  

---

## Estrutura do arquivo

O arquivo **exemplos_teste.txt** contém valores utilizados para teste.

**Exemplos:**
- `BRL1.234,56`
- `usd9.999,99`
- `(Peso12.345,67)`
- `$0,50`

## Como executar o código

```bash

1. Executar lendo um arquivo de entrada
- Processa cada linha de um arquivo texto:

`py analisador_lexico.py exemplos_teste.txt`

2. Executar usando os testes internos (`--teste`)
- Roda casos de teste embutidos no código:

`py analisador_lexico.py --teste`

3. Exibir o regex utilizado (--regex)
- Mostra no terminal a expressão regular completa usada pelo analisador:

`py analisador_lexico.py --regex`
