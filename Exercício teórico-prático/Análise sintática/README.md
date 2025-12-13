**Exercício teórico-prático — Análise Sintática — 2ª Avaliação**

Este programa implementa um **analisador sintático** com o objetivo de reconhecer e validar as diferentes formas de acesso a colunas em datasets utilizando a biblioteca Pandas da linguagem Python.

**Autores:** Alicia Monteiro, Eduardo Couto, Kleiton Josivan, João Vitor Fernandes e Robert Danilo  
**Data:** 13/12/2025

---

## Funcionalidades

O analisador é capaz de:

- **Reconhecer acessos por índice numérico**, incluindo valores positivos, negativos e zero  
- **Validar acesso por nome de coluna** (strings simples ou duplas)  
- Analisar **intervalos (*slices*) numéricos**  
- Analisar **intervalos (*slices*) por nomes de colunas**  
- Suportar **acessos encadeados**, usando o resultado de outro acesso como índice  
- Reconhecer **expressões comparativas e lógicas** aplicadas ao acesso aos dados  

---

## Estrutura do analisador

O analisador trabalha com expressões que seguem o padrão geral: Onde o **índice** pode assumir diferentes formatos, conforme as regras definidas pela gramática da atividade.

**Exemplos de acessos válidos:**

- `x[0]`
- `x['Data']`
- `x[1:5]`
- `x['Data':'State']`
- `x[y[0]]`
- `x[y['dia'] > 5]`

---

## Como executar o código

1. Salve o código em um arquivo, por exemplo: analisador_sintatico.py
2. No terminal, navegue até a pasta onde o arquivo está salvo e execute:

```bash
python analisador_sintatico.py
```

### Saída esperada (cadeia válida)

Quando a expressão está de acordo com todas as regras da gramática, o analisador finaliza com a mensagem:

```bash
✓ Cadeia válida!
```

### Saída não esperada (cadeia com erro)
Quando a expressão não atende às regras sintáticas definidas, o programa exibe:

```bash
✗ Erro de análise: <descrição do erro>
```

---

Projeto desenvolvido como parte da **3ª Avaliação** da disciplina de **Compiladores e paradigmas de programação**.
