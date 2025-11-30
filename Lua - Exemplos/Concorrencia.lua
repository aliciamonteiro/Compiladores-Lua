
-- Slide 3: Concorrência - Exemplo de Co-rotinas para Concorrência Colaborativa

-- Co-rotina 1: Imprime números pares
local function producer_even(co_consumer)
    for i = 1, 10, 2 do -- Números pares
        print("Producer (Even): " .. i)
        coroutine.resume(co_consumer, i) -- Passa o número para o consumidor
        coroutine.yield() -- Cede o controle
    end
    print("Producer (Even) finished.")
end

-- Co-rotina 2: Imprime números ímpares
local function producer_odd(co_consumer)
    for i = 2, 10, 2 do -- Números ímpares
        print("Producer (Odd): " .. i)
        coroutine.resume(co_consumer, i) -- Passa o número para o consumidor
        coroutine.yield() -- Cede o controle
    end
    print("Producer (Odd) finished.")
end

-- Co-rotina Consumidor: Processa os números
local function consumer()
    while true do
        local num = coroutine.yield() -- Espera por um número do produtor
        if num == nil then break end -- Se nil, produtor terminou
        print("Consumer: Received " .. num)
    end
    print("Consumer finished.")
end

-- Cria as co-rotinas
local co_consumer = coroutine.create(consumer)
local co_producer_even = coroutine.create(function() producer_even(co_consumer) end)
local co_producer_odd = coroutine.create(function() producer_odd(co_consumer) end)

print("--- Exemplo de Co-rotinas ---")

-- Inicia a execução, alternando entre os produtores
while coroutine.status(co_producer_even) ~= "dead" or coroutine.status(co_producer_odd) ~= "dead" do
    if coroutine.status(co_producer_even) == "suspended" then
        coroutine.resume(co_producer_even)
    end
    if coroutine.status(co_producer_odd) == "suspended" then
        coroutine.resume(co_producer_odd)
    end
end

-- Garante que o consumidor termine se ainda estiver suspenso
if coroutine.status(co_consumer) == "suspended" then
    coroutine.resume(co_consumer, nil) -- Sinaliza que não há mais dados
end

print("--- Fim do exemplo de Co-rotinas ---")


