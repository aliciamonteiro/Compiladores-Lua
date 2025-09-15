# Linguagem Lua

## Disciplina: Compiladores e Paradigmas da Computação

**Docente:** Sebastião Alves  
**Discentes:** Alicia Monteiro, Eduardo Couto, João Vitor Fernandes, Kleiton Josivan e Robert Danilo  

---
## Sobre a Linguagem Lua
Lua é uma linguagem de programação leve, rápida e poderosa, criada no Brasil em 1993.  
É muito utilizada em aplicações que exigem **facilidade de integração** com outras linguagens, como jogos, sistemas embarcados e scripts de configuração.

Algumas características da linguagem:
- Sintaxe simples e limpa.
- Tipagem dinâmica.
- Interpretada.
- Suporte a programação estruturada e funcional.
- Amplamente usada em engines de jogos como **Roblox** e **World of Warcraft** (addons).
- Mais informações da linguagem: https://www.lua.org

---

## ⚙️ Como rodar Lua na sua máquina

### 🔹 1. Instalar o interpretador Lua
- Acesse o site oficial: [https://www.lua.org/download.html](https://www.lua.org/download.html)  
- Baixe o **executável** compatível com seu sistema operacional (Windows/Linux/Mac).  
- Adicione o caminho do executável do Lua nas **variáveis de ambiente** do seu computador.  

---

### 🔹 2. Configurar no VS Code
1. Abra o **Visual Studio Code**.  
2. Instale a extensão:  
   - **Name:** Lua  
   - **Id:** sumneko.lua  
   - **Publisher:** sumneko  
   - **Version:** 3.15.0  
   - [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=sumneko.lua)  
3. Crie um arquivo `exemplo.lua`.  
4. Exemplo de código:  

```lua
print("Olá, mundo! Estou rodando Lua")
