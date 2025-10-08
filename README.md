<div align="center">
  <img src="https://img.shields.io/badge/STATUS-COMPLETO-brightgreen?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/LANGUAGE-LUA-blue?style=for-the-badge&logo=lua" alt="Language">
  <img src="https://img.shields.io/badge/LICENSE-EDUCACIONAL-red?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/STARS-1-yellow?style=for-the-badge" alt="Stars">
</div>

<div align="center">
  <br>
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/Lua-Logo.svg" alt="Logo da Linguagem Lua" width="100">
  <h1>Linguagem Lua - Um projeto para a disciplina de <strong>Compiladores e Paradigmas da Computação</strong>.</p>
</div>

## 👩‍💻 Autores - Grupo 4

**Docente:** Sebastião Alves  
**Discentes:** Alicia Monteiro, Eduardo Couto, João Vitor Fernandes, Kleiton Josivan e Robert Danilo  

## Sobre a Linguagem Lua

Lua é uma linguagem de programação leve, rápida e poderosa, criada no Brasil em 1993. É muito utilizada em aplicações que exigem **facilidade de integração** com outras linguagens.

**Principais Características:**
- Sintaxe simples e limpa.
- Tipagem dinâmica e interpretada.
- Suporte a programação estruturada e funcional.
- Amplamente usada em jogos como **Roblox** e **World of Warcraft** (addons).
- Para mais detalhes, visite o **[site oficial da Lua](https://www.lua.org)**.

---

### Organização do repositório

O projeto está estruturado da seguinte forma, com os códigos de exemplo agora localizados dentro da pasta `Exemplos/`:

```
.
├── 📁 Slides/
│   ├── Lua - Aula 1 - Grupo 4.pdf
│   ├── Lua - Aula 2 - Grupo 4.pdf
│   └── Lua - Aula 3 - Grupo 4.pdf
│
├── 📁 Exemplos/
│   ├── Concorrencia.lua
│   ├── Declaracoes.lua
│   ├── Excecao.lua
│   ├── Fundamentos.lua
│   └── Subprogramas.lua
│
└── README.md
```

- **`/Slides`**: Contém os arquivos PDF das apresentações utilizadas no projeto.
- **`/Exemplos`**: Pasta principal que agrupa todos os scripts `.lua`. Cada arquivo demonstra um conceito específico da linguagem.
- `README.md`: Este arquivo de documentação que você está lendo.

---

## Guia de Configuração

Siga os passos abaixo para preparar seu ambiente de desenvolvimento e executar os arquivos da pasta `Exemplos`.

### Instalar o Interpretador Lua

- **Windows/macOS:** Baixe o instalador no [site oficial](https://www.lua.org/download.html) e não se esqueça de adicionar o Lua às **variáveis de ambiente** do seu sistema.

- **Linux (Debian/Ubuntu):**
  
  ```bash
  sudo apt install lua5.4
  ```

- **Verificação:** Para confirmar a instalação, abra um novo terminal e execute:
  
  ```powershell
  lua -v
  # A saída deve ser algo como: Lua 5.4.x
  ```

### Configurar o VS Code

1.  **Instale a Extensão:** Na aba de extensões (`Ctrl+Shift+X`), procure por `Lua` (ID: `sumneko.lua`) e clique em instalar.
2.  **Abra a Pasta do Projeto:** No VS Code, vá em `File > Open Folder` e selecione a pasta do seu projeto.
3.  **Execute um Exemplo:**

    - Abra o terminal integrado (`Ctrl+'`).
    - Navegue até a pasta de exemplos com o comando: `cd Exemplos`
    - Execute um dos arquivos, por exemplo:
      
      
    ```bash
    lua Fundamentos.lua
    ```

### Configurar o Geany

1.  **Instale o Geany:** Baixe em [geany.org](https://www.geany.org/Download/).
2.  **Configure a Execução:** Vá em **Construir → Definir Comandos de Construção**.
3.  No campo **"Diretório de Trabalho" (Working Directory)**, insira `%d` para garantir que ele execute na pasta do arquivo.
4.  No campo **"Executar" (Execute)**, adicione o comando abaixo e salve:
   
    ```
    lua "%f"
    ```
    
6.  **Teste:** Abra um dos arquivos da pasta `Exemplos` (ex: `Subprogramas.lua`) e pressione **F5** para rodar.

---

<p align="center">
  Este projeto está licenciado para uso educacional. <br>
  Sinta-se livre para reutilizar com devida atribuição. <br>
  © 2025 — Feito para a comunidade Lua
</p>
