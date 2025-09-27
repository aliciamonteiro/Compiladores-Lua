-- Seminário 01 - Linguagem Lua
-- Declarações e separação de instruções

print("Oi, mundo!\n")

-- Seminário 02 - Linguagem Lua
-- Tipo de variáveis

print(type("Hello world"))  --> string
print(type(10.4*3))         --> number
print(type(print))          --> function
print(type(type))           --> function
print(type(true))           --> boolean
print(type(nil))            --> nil
print(type(type(X)))        --> string

print("\n")

print(type(a))   --> nil   (`a' is not initialized)
a = 10
print(type(a))   --> number
a = "a string!!"
print(type(a))   --> string
a = print        -- É válido
a(type(a))       --> function

print("\n")

-- Exemplos

-- Tipo nil
local valor_nil = nil
print("Tipo nil:", type(valor_nil))

-- Tipo boolean
local valor_boolean = true
print("Tipo boolean:", type(valor_boolean))

-- Tipo number
local valor_inteiro = 42
print("Tipo number:", type(valor_inteiro))

-- Tipo string
local valor_string = "Olá, Lua!"
print("Tipo string:", type(valor_string))

-- Tipo table
local minha_tabela = {
 nome = "Lua", 
 ano = 1993, 
 10, 20, 30
}
print("Tipo table:", type(minha_tabela))
print("Acessando tabela:", minha_tabela.nome, minha_tabela[1], "\n")

