-- Seminário 02 - Linguagem Lua
-- Exemplos de Código

-- Uso de referências (com tabelas)
print("\n--- Uso de referencias ---")
local table1 = {a = 1, b = 2}
local table2 = table1 -- table2 referencia a mesma tabela que table1

print("Antes da modificacao:")
print("table1.a: ", table1.a)
print("table2.a: ", table2.a)

table2.a = 10

print("Depois da modificacao via table2:")
print("table1.a: ", table1.a) -- table1.a também mudou
print("table2.a: ", table2.a)

-- Palavras Chave e Reservadas
print("\n---Palavras chave e reservadas ---")
-- As palavras-chave não podem ser usadas como nomes de variáveis.
-- Exemplo de nome de variável válido:
local variavel = 20
print("variavel: ", variavel)
-- local function = 20 - Tentar usar 'function' como nome de variável resultaria em erro de sintaxe.

-- Variáveis: Nomes, Vinculação, Tempo de Vida e Escopo
print("\n--- Variaveis ---")
local global_var = 100 -- Em Lua, variáveis não declaradas com 'local' são globais por padrão

function test_scope()
    local local_var = 200
    print("Dentro da funcao - global_var: ", global_var)
    print("Dentro da funcao - local_var: ", local_var)

    if true then
        local block_var = 300
        print("Dentro do bloco if - block_var: ", block_var)
    end
end

test_scope()
print("Fora da funcao - global_var: ", global_var)
-- print(local_var) -- Erro: local_var está fora de escopo aqui

-- Expressões: Associatividade, Precedência e Sobrecarga de Operadores
print("\n--- Expressoes ---")
local result_precedence = 2 + 3 * 4 
print("2 + 3 * 4 = ", result_precedence)

local result_associativity = 10 / 2 * 5 
print("10 / 2 * 5 = ", result_associativity)

-- Sobrecarga de Operadores (exemplo com metatables)
local my_vector = {x = 1, y = 2}
local other_vector = {x = 3, y = 4}

local mt = {
    __add = function(v1, v2)
        return {x = v1.x + v2.x, y = v1.y + v2.y}
    end
}

setmetatable(my_vector, mt)
setmetatable(other_vector, mt)

local sum_vector = my_vector + other_vector
print("Soma de vetores (sobrecarga de operador +): ", sum_vector.x, ", ", sum_vector.y)

-- Estruturas de Controle e Desvios de Fluxo

-- Comandos Condicionais
print("\n--- Comandos Condicionais ---")
local temperature = 25

if temperature > 30 then
    print("Esta muito quente!")
elseif temperature > 20 then
    print("Temperatura agradavel.")
else
    print("Esta frio.")
end

-- Comandos de Repetição
print("\n--- Comandos de Repeticaoo ---")

-- while-do-end
local count = 1
while count <= 3 do
    print("While loop - Contagem: ", count)
    count = count + 1
end

-- repeat-until
local i = 1
repeat
    print("Repeat-until loop - i: ", i)
    i = i + 1
until i > 3

-- for numérico
for j = 1, 3 do
    print("For numerico - j: ", j)
end

-- for genérico (com ipairs para arrays)
local fruits = {"apple", "banana", "cherry"}
for index, value in ipairs(fruits) do
    print("For generico (ipairs) - ", index, ": ", value)
end

-- for genérico (com pairs para tabelas)
local person = {name = "Alice", age = 30}
for key, value in pairs(person) do
    print("For generico (pairs) - ", key, ": ", value)
end


