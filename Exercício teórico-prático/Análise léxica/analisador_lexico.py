
"""
Analisador Léxico para Valores Monetários
Trabalho Teórico-Prático - Análise Léxica - 2ª Avaliação

Este programa implementa um analisador léxico que reconhece valores monetários
no formato especificado, usando expressões regulares.

Autores: Alicia Monteiro, Eduardo COuto, Kleiton Josivan, João Vitor Fernandes e Robert Danilo
Data: 30/11/2025
"""

import re
import sys


def criar_regex_moeda():
    """
    Cria a expressão regular para reconhecer valores monetários válidos.
    
    Formato aceito:
    - Símbolo: letras (maiúsculas/minúsculas) opcionalmente seguidas de $, ou apenas $
    - Sinal: opcional (-) após o símbolo, ou valor entre parênteses para negativos
    - Número: formato brasileiro com . para milhares e , para decimais
    - Parte inteira: não pode começar com zero (exceto se for apenas 0)
    - Parte decimal: mínimo 2 dígitos
    - Sem espaços
    
    Observação: Para valores negativos entre parênteses, TODO o valor (símbolo + número)
    fica entre parênteses, exemplo: (R$500,50)
    
    Returns:
        Pattern compilado da expressão regular
    """
    
    # Componentes da expressão regular
    simbolo = r'([A-Za-z]+\$?|\$)'  # Letras + $ opcional, ou apenas $
    parte_inteira = r'([1-9][0-9]{0,2}(\.[0-9]{3})*|0)'  # Número com milhares ou zero
    parte_decimal = r'[0-9]{2,}'  # Mínimo 2 dígitos decimais
    numero = f'{parte_inteira},{parte_decimal}'
    
    # Duas formas de representar valores:
    # 1. Valor normal (positivo ou negativo com sinal -)
    #    Formato: SÍMBOLO-?NÚMERO
    #    Exemplos: R$1.234,56  ou  R$-500,50
    valor_normal = f'{simbolo}-?{numero}'
    
    # 2. Valor negativo entre parênteses
    #    Formato: (SÍMBOLONÚMERO)
    #    Exemplo: (R$500,50)
    valor_entre_parenteses = f'\\({simbolo}{numero}\\)'
    
    # Expressão completa: uma ou outra forma
    regex_completa = f'^({valor_normal}|{valor_entre_parenteses})$'
    
    return re.compile(regex_completa)


def validar_valor(valor, regex):
    """
    Valida se um valor monetário está no formato correto.
    
    Args:
        valor: String com o valor a ser validado
        regex: Pattern compilado da expressão regular
        
    Returns:
        True se válido, False caso contrário
    """
    return regex.match(valor) is not None


def analisar_arquivo(nome_arquivo):
    """
    Lê um arquivo com valores monetários (um por linha) e valida cada um.
    
    Args:
        nome_arquivo: Caminho do arquivo a ser analisado
    """
    regex = criar_regex_moeda()
    
    print("=" * 80)
    print("ANALISADOR LÉXICO DE VALORES MONETÁRIOS")
    print("=" * 80)
    print()
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            
        print(f"Arquivo: {nome_arquivo}")
        print(f"Total de linhas: {len(linhas)}")
        print()
        print("-" * 80)
        
        validos = 0
        invalidos = 0
        
        for i, linha in enumerate(linhas, 1):
            valor = linha.strip()
            
            # Ignora linhas vazias
            if not valor:
                continue
                
            eh_valido = validar_valor(valor, regex)
            
            if eh_valido:
                status = "✓ VÁLIDO"
                validos += 1
            else:
                status = "✗ INVÁLIDO"
                invalidos += 1
            
            print(f"Linha {i:2d}: {valor:30s} → {status}")
        
        print("-" * 80)
        print()
        print("RESUMO:")
        print(f"  Valores válidos:   {validos}")
        print(f"  Valores inválidos: {invalidos}")
        print(f"  Total analisado:   {validos + invalidos}")
        print()
        print("=" * 80)
        
    except FileNotFoundError:
        print(f"ERRO: Arquivo '{nome_arquivo}' não encontrado!")
        sys.exit(1)
    except Exception as e:
        print(f"ERRO ao processar arquivo: {e}")
        sys.exit(1)


def testar_regex():
    """
    Função de teste para validar a expressão regular com exemplos conhecidos.
    """
    regex = criar_regex_moeda()
    
    print("=" * 80)
    print("TESTE DA EXPRESSÃO REGULAR")
    print("=" * 80)
    print()
    
    # Exemplos válidos
    validos = [
        "R$1.234,56",
        "USD$10.000,00",
        "euro45,99",
        "$999,00",
        "BRL$1,23",
        "R$-500,50",         # Sinal após o símbolo
        "(JPY$2.500,75)",    # Todo o valor entre parênteses
        "libra1.000.000,00",
        "CAD$99,99",
        "peso12.345.678,90"
    ]
    
    # Exemplos inválidos
    invalidos = [
        "R$ 1.234,56",      # espaço
        "R$01.234,56",      # zero à esquerda
        "R$1234,56",        # falta separador de milhar
        "R$1.234.56",       # ponto em vez de vírgula
        "R$1.234,5",        # apenas 1 casa decimal
        "123,45",           # sem símbolo
        "$R1.234,56",       # cifrão antes das letras
        "R$1.23,45",        # milhar com 2 dígitos
        "-R$500,50",        # sinal ANTES do símbolo (inválido)
        "R$1.234,"          # falta parte decimal
    ]
    
    print("EXEMPLOS VÁLIDOS:")
    print("-" * 80)
    acertos = 0
    for valor in validos:
        resultado = validar_valor(valor, regex)
        status = "✓" if resultado else "✗ ERRO!"
        if resultado:
            acertos += 1
        print(f"  {status} {valor}")
    
    print()
    print("EXEMPLOS INVÁLIDOS:")
    print("-" * 80)
    for valor in invalidos:
        resultado = validar_valor(valor, regex)
        status = "✓ Corretamente rejeitado" if not resultado else "✗ ERRO - deveria ser inválido!"
        if not resultado:
            acertos += 1
        print(f"  {status} {valor}")
    
    print()
    print(f"Resultado: {acertos}/{len(validos) + len(invalidos)} testes passaram")
    print()
    print("=" * 80)


def exibir_regex():
    """
    Exibe a expressão regular utilizada.
    """
    print("=" * 80)
    print("EXPRESSÃO REGULAR UTILIZADA")
    print("=" * 80)
    print()
    
    regex = criar_regex_moeda()
    print(regex.pattern)
    print()
    
    print("COMPONENTES:")
    print("-" * 80)
    print("SÍMBOLO = ([A-Za-z]+\\$?) | (\\$)")
    print("  → Letras seguidas opcionalmente de $, OU apenas $")
    print()
    print("PARTE_INTEIRA = ([1-9][0-9]{0,2}(\\.[0-9]{3})*) | 0")
    print("  → 1-3 dígitos (não começando com 0) + grupos de milhar, OU apenas 0")
    print()
    print("PARTE_DECIMAL = [0-9]{2,}")
    print("  → Mínimo 2 dígitos")
    print()
    print("NÚMERO = PARTE_INTEIRA,PARTE_DECIMAL")
    print()
    print("VALOR_NORMAL = SÍMBOLO-?NÚMERO")
    print("  → Sinal opcional após o símbolo")
    print()
    print("VALOR_PARÊNTESES = (SÍMBOLONÚMERO)")
    print("  → Todo o valor entre parênteses")
    print()
    print("REGEX_COMPLETA = VALOR_NORMAL | VALOR_PARÊNTESES")
    print()
    print("=" * 80)


if __name__ == "__main__":
    
    argumento = sys.argv[1]

    if argumento == "--teste":
        testar_regex()
    elif argumento == "--regex":
        exibir_regex()
    else:
        analisar_arquivo(argumento)
