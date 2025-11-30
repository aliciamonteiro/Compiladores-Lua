-- Slide 3: Subprogramas

-- 1. Declaração e Chamada
function saudacao()
    print("Ola, mundo!")
end
saudacao()

-- 2. Passagem de Parâmetros
function soma(a, b)
    return a + b
end
local resultado_soma = soma(5, 3)
print("Resultado da Soma: " .. resultado_soma)

-- 3. Retornos Múltiplos
function divide(dividendo, divisor)
    local quociente = math.floor(dividendo / divisor)
    local resto = dividendo % divisor
    return quociente, resto
end

local quociente, resto = divide(10, 3)
print("Quociente: " .. quociente .. " Resto: " .. resto)

-- 4. Funções Variádicas
function somaVariadica(...)
    local soma_total = 0
    for _, num in ipairs({...}) do
        soma_total = soma_total + num
    end
    return soma_total
end

local resultado_variadica = somaVariadica(1, 2, 3, 4, 5)
print("Soma Variadica: " .. resultado_variadica)

-- 5. Funções Lambda (Funções Anônimas)
local multiplicar = function(x, y)
    return x * y
end
print("Multiplicacao (lambda): " .. multiplicar(4, 6))

-- Funções anônimas como argumento
function aplicar_operacao(op, a, b)
    return op(a, b)
end

print("Aplicar operacao (lambda): " .. aplicar_operacao(function(x, y) return x ^ y end, 2, 3))

-- 6. Programação Genérica (em Lua, isso se refere à flexibilidade de tipos)
-- Funções podem operar em diferentes tipos de dados sem restrições explícitas
function imprimir_tipo(valor)
    print("Valor: " .. tostring(valor) .. ", Tipo: " .. type(valor))
end

imprimir_tipo(123)
imprimir_tipo("hello")
imprimir_tipo(true)
imprimir_tipo({a=1, b=2})

-- Exemplo de função que funciona com diferentes tipos (se a operação for válida)
function concatenar_ou_somar(a, b)
    if type(a) == "number" and type(b) == "number" then
        return a + b
    elseif type(a) == "string" and type(b) == "string" then
        return a .. b
    else
        return tostring(a) .. tostring(b)
    end
end

print("Soma (numeros): " .. concatenar_ou_somar(10, 20))
print("Concatenar (strings): " .. concatenar_ou_somar("Hello", "World"))
print("Concatenar (misto): " .. concatenar_ou_somar(10, "World"))

