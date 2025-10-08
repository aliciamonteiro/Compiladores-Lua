-- 1. Lançando Erros com 'error'
function dividir(a, b)
    if b == 0 then
        error("Tentativa de divisao por zero!")
    end
    return a / b
end

print("--- Exemplo de 'error' ---")
-- A linha abaixo causaria um erro fatal se não fosse comentada
-- dividir(10, 0)
print("Chamada direta a dividir(10, 2): ", dividir(10, 2))
print("\n")


-- 2. Tratamento de Erros com 'pcall'
print("\n--- Exemplo de 'pcall' ---")

-- Caso de sucesso
local status_sucesso, resultado_sucesso = pcall(dividir, 10, 2)
if status_sucesso then
    print("pcall (sucesso): Resultado da divisao: ", resultado_sucesso)
else
    print("pcall (sucesso): Erro: ", resultado_sucesso)
end

-- Caso de erro
local status_erro, mensagem_erro = pcall(dividir, 10, 0)
if status_erro then
    print("pcall (erro): Resultado da divisão: ", mensagem_erro)
else
    print("pcall (erro): Erro: ", mensagem_erro)
end
print("\n")


-- 3. Tratamento de Erros com 'xpcall' e um manipulador de erros personalizado
print("\n--- Exemplo de 'xpcall' ---")

-- Função manipuladora de erros personalizada
local function meu_manipulador_de_erro(msg)
    print("  [MANIPULADOR DE ERRO] Um erro foi capturado: ", msg)
    -- Você pode adicionar lógica de log, formatação, etc. aqui
    return "Erro personalizado: " .. msg .. " (timestamp: " .. os.date() .. ")"
end

-- Função que pode gerar um erro
function funcao_com_erro(param)
    if param < 0 then
        error("Parametro negativo nao permitido!")
    end
    return "Parametro valido: " .. param
end

-- Caso de sucesso com xpcall
local status_xpcall_sucesso, resultado_xpcall_sucesso = xpcall(funcao_com_erro, meu_manipulador_de_erro, 5)
if status_xpcall_sucesso then
    print("xpcall (sucesso): ", resultado_xpcall_sucesso)
else
    print("xpcall (sucesso): Falha na execucao: ", resultado_xpcall_sucesso)
end

-- Caso de erro com xpcall
local status_xpcall_erro, mensagem_xpcall_erro = xpcall(funcao_com_erro, meu_manipulador_de_erro, -1)
if status_xpcall_erro then
    print("xpcall (erro): ", mensagem_xpcall_erro)
else
    print("xpcall (erro): Falha na execucao: ", mensagem_xpcall_erro)
end


