
"""
Trabalho Teórico-Prático - Análise Sintática - 3ª Avaliação

Este programa implementa um analisador sintático voltado para o reconhecimento e validação
das diferentes formas de acesso a colunas em datasets utilizando a biblioteca Pandas.

Autores: Alicia Monteiro, Eduardo COuto, Kleiton Josivan, João Vitor Fernandes e Robert Danilo
Data: 13/12/2025

"""
import re

# Definição dos tipos de tokens
TOKEN_SPECS = [
    ('OPERADOR', r'==|!=|>=|<=|>|<'),
    ('STRING', r'\'.*?\'|\".*?\"'),  # Aspas simples ou duplas
    ('DIGITOS', r'\d+'),
    
    ('L_COLCHETE', r'\['),
    ('R_COLCHETE', r'\]'),
    ('DOIS_PONTOS', r':'),
    ('SINAL', r'-'), # negativo
    
    ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'), 
    
    ('ESPACO', r'\s+'), # Ignora os espaços
]

def tokenize(code):
    tokens = []
    regex_groups = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECS)
    
    for match in re.finditer(regex_groups, code):
        kind = match.lastgroup
        if kind == 'ESPACO':
            continue
        tokens.append({'type': kind, 'value': match.group(kind)})
        
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0 

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return {'type': 'EOF', 'value': None}

    def eat(self, token_type=None, token_value=None):
        current_token = self.peek()
        
        if self.pos >= len(self.tokens):
            raise SyntaxError(f"Erro: Fim inesperado da entrada. Esperado {token_type} ou {token_value}.")
            
        if token_type and current_token['type'] != token_type:
            raise SyntaxError(f"Erro de sintaxe. Esperado tipo {token_type}, mas encontrei {current_token['type']}: '{current_token['value']}'")
        
        if token_value and current_token['value'] != token_value:
            raise SyntaxError(f"Erro de sintaxe. Esperado valor '{token_value}', mas encontrei '{current_token['value']}'")
            
        self.pos += 1
        return current_token

    # Regras da gramática 

    def parse_S(self):
        """S ⮕ VAR '[' INDICE ']'"""
        print("S: Início")
        self.parse_VAR()
        self.eat('L_COLCHETE')
        self.parse_INDICE()
        self.eat('R_COLCHETE')
        print("S: Sucesso")

    def parse_VAR(self):
        """VAR ⮕ ID"""
        print("  VAR: Início")
        token = self.eat('ID')
        print(f"  VAR: ID reconhecido '{token['value']}'")
        return token

    def parse_NUMERO(self):
        """NUMERO ⮕ SINAL_OPC DIGITOS"""
        print("  NUMERO: Início")
        
        is_negative = False
        start_pos = self.pos
        
        if self.peek()['type'] == 'SINAL':
            self.eat('SINAL')
            is_negative = True
            
        if self.peek()['type'] == 'DIGITOS':
            token = self.eat('DIGITOS')
            value = int(token['value'])
            if is_negative:
                value = -value
            print(f"  NUMERO: Reconhecido {value}")
            return {'type': 'NUMERO', 'value': value}
        else:
            self.pos = start_pos 
            raise SyntaxError("Erro: Não é um NUMERO válido (faltou DIGITOS).")
        
    def parse_STRING(self):
        """STRING ⮕ '\'' CARACTERES '\'' | '"' CARACTERES '"'"""
        print("  STRING: Início")
        token = self.eat('STRING')
        value = token['value'].strip('\'').strip('\"')
        print(f"  STRING: Reconhecida '{value}'")
        return {'type': 'STRING', 'value': value}

    def parse_ACESSO(self):
        """ACESSO ⮕ VAR '[' INDICE ']'"""
        print("  ACESSO: Início")
        self.parse_VAR()
        self.eat('L_COLCHETE')
        self.parse_INDICE()
        self.eat('R_COLCHETE')
        print("  ACESSO: Sucesso")
        return {'type': 'ACESSO', 'value': 'Acesso Aninhado'}
        
    def parse_FATIAMENTO_NUM(self):
        """FATIAMENTO_NUM ⮕ NUM_OPC ':' NUM_OPC"""
        print("  FATIAMENTO_NUM: Início")
        start = None
        end = None
        start_pos = self.pos
        
        # 1. Tenta parsear o NUMERO inicial (NUM_OPC)
        try:
            start = self.parse_NUMERO()
        except SyntaxError:
            pass # NUM_OPC é opcional, então falha aqui é OK, se o próximo for ':'
            
        # 2. Consome ':'
        if self.peek()['type'] != 'DOIS_PONTOS':
            # Se não encontrou NUMERO e não tem ':', não é fatiamento numérico
            self.pos = start_pos 
            raise SyntaxError("Erro: Não é FATIAMENTO_NUM.")
            
        self.eat('DOIS_PONTOS')
        
        # 3. Tenta parsear o NUMERO final (NUM_OPC)
        try:
            end = self.parse_NUMERO()
        except SyntaxError:
            pass # NUM_OPC é opcional

        # 4. Validação (se não consumiu nada além de ':' e falhou, reverte)
        if start is None and end is None and self.tokens[self.pos-1]['type'] == 'DOIS_PONTOS':
            print("  FATIAMENTO_NUM: Fatiamento completo/vazio (:) reconhecido.")
            
        print("  FATIAMENTO_NUM: Sucesso")
        return {'type': 'FATIAMENTO_NUM', 'value': (start, end)}


    def parse_FATIAMENTO_STR(self):
        """FATIAMENTO_STR ⮕ STR_OPC ':' STR_OPC"""
        print("  FATIAMENTO_STR: Início")
        start = None
        end = None
        start_pos = self.pos
        
        # 1. Tenta parsear a STRING inicial (STR_OPC)
        try:
            start = self.parse_STRING()
        except SyntaxError:
            pass # STR_OPC é opcional
            
        # 2. Consome ':'
        if self.peek()['type'] != 'DOIS_PONTOS':
            # Se não encontrou STRING e não tem ':', não é fatiamento string
            self.pos = start_pos 
            raise SyntaxError("Erro: Não é FATIAMENTO_STR.")
            
        self.eat('DOIS_PONTOS')
        
        # 3. Tenta parsear a STRING final (STR_OPC)
        try:
            end = self.parse_STRING()
        except SyntaxError:
            pass # STR_OPC é opcional

        # 4. Validação
        if start is None and end is None and self.tokens[self.pos-1]['type'] == 'DOIS_PONTOS':
            # Se casou apenas ':', é ambíguo. Para desambiguação, deve ser tentado pelo FATIAMENTO_NUM.
            # Se chegou aqui, é porque FATIAMENTO_NUM falhou ou porque FATIAMENTO_STR foi priorizado.
            # Não fazemos reversão, pois FATIAMENTO_NUM será tentado depois se este falhar.
            print("  FATIAMENTO_STR: Fatiamento completo/vazio (:) reconhecido.")
            
        print("  FATIAMENTO_STR: Sucesso")
        return {'type': 'FATIAMENTO_STR', 'value': (start, end)}
        
    def parse_OPERADOR(self):
        """OPERADOR ⮕ '==' | '!=' | '>' | '<' | '>=' | '<='"""
        print("  OPERADOR: Início")
        token = self.eat('OPERADOR')
        print(f"  OPERADOR: Reconhecido '{token['value']}'")
        return token

    def parse_EXPRESSAO(self):
        """EXPRESSAO ⮕ NUMERO | STRING | VAR | ACESSO"""
        print("  EXPRESSAO: Início (Tentando match)")
        start_pos = self.pos
        
        # 1. Tenta NUMERO
        if self.peek()['type'] in ['SINAL', 'DIGITOS']:
            try:
                return self.parse_NUMERO()
            except SyntaxError:
                pass 
        
        # 2. Tenta STRING
        if self.peek()['type'] == 'STRING':
            try:
                return self.parse_STRING()
            except SyntaxError:
                pass
                
        # 3. Tenta VAR / ACESSO
        if self.peek()['type'] == 'ID':
            # Lookahead para ACESSO (ID seguido de '[')
            try:
                # Procura por '[' para verificar se é ACESSO
                next_token_index = next(i for i, token in enumerate(self.tokens[self.pos:]) if token['type'] == 'L_COLCHETE')
                
                # Se encontrou '[', tenta ACESSO
                if self.tokens[self.pos + next_token_index]['type'] == 'L_COLCHETE':
                    try:
                        return self.parse_ACESSO()
                    except SyntaxError:
                         self.pos = start_pos # Reverte se ACESSO falhou
                         pass
            except StopIteration:
                pass # Não encontrou '[', tenta VAR
            
            # Se não foi ACESSO, tenta VAR
            return self.parse_VAR()
            
        self.pos = start_pos
        raise SyntaxError(f"Erro: EXPRESSAO inválida. Token atual: {self.peek()}")

    def parse_COMPARACAO(self):
        """COMPARACAO ⮕ EXPRESSAO OPERADOR EXPRESSAO"""
        print("  COMPARACAO: Início")
        self.parse_EXPRESSAO()
        self.parse_OPERADOR()
        self.parse_EXPRESSAO()
        print("  COMPARACAO: Sucesso")
        return {'type': 'COMPARACAO', 'value': 'Comparação'}
    
    def parse_INDICE(self):
        """INDICE ⮕ NUMERO | STRING | FATIAMENTO_NUM | FATIAMENTO_STR | ACESSO | COMPARACAO"""
        print("INDICE: Início (Tentando match)")
        start_pos = self.pos
        
        # A ordem é crucial para desambiguação
        
        # 1. Tenta COMPARACAO (Começa com EXPRESSAO e busca OPERADOR)
        try:
            return self.parse_COMPARACAO()
        except SyntaxError as e:
            self.pos = start_pos 
            print(f"INDICE: Comparação falhou. Erro: {e}")
            pass
            
        # 2. Tenta ACESSO (ID seguido de '[')
        if self.peek()['type'] == 'ID':
            try:
                # Verificar se o ID é seguido por '['
                next_token_index = next(i for i, token in enumerate(self.tokens[self.pos:]) if token['type'] == 'L_COLCHETE')
                if self.tokens[self.pos + next_token_index]['type'] == 'L_COLCHETE':
                    try:
                        return self.parse_ACESSO()
                    except SyntaxError:
                         self.pos = start_pos
                         pass
            except StopIteration:
                pass 
        
        # 3. Tenta FATIAMENTO_STR (Prioridade para 'STR' para desambiguar x[:])
        # Começa com STRING ou DOIS_PONTOS
        if self.peek()['type'] in ['STRING', 'DOIS_PONTOS']:
            try:
                return self.parse_FATIAMENTO_STR()
            except SyntaxError as e:
                self.pos = start_pos
                print(f"INDICE: Fatiamento String falhou. Erro: {e}")
                pass
                
        # 4. Tenta FATIAMENTO_NUM (Começa com SINAL, DIGITOS, ou DOIS_PONTOS)
        if self.peek()['type'] in ['SINAL', 'DIGITOS', 'DOIS_PONTOS']:
            try:
                return self.parse_FATIAMENTO_NUM()
            except SyntaxError as e:
                self.pos = start_pos
                print(f"INDICE: Fatiamento Numérico falhou. Erro: {e}")
                pass
            
        # 5. Tenta NUMERO 
        if self.peek()['type'] in ['SINAL', 'DIGITOS']:
            try:
                return self.parse_NUMERO()
            except SyntaxError:
                pass

        # 6. Tenta STRING
        if self.peek()['type'] == 'STRING':
            try:
                return self.parse_STRING()
            except SyntaxError:
                pass
                
        self.pos = start_pos
        raise SyntaxError(f"Erro: Índice inválido. Token atual: {self.peek()}")

# Função de teste
def run_parser(input_string):
    print(f"\n{'='*50}")
    print(f"Analisando: {input_string}")
    print(f"{'='*50}")
    
    try:
        tokens = tokenize(input_string)
        print("Tokens gerados:", [t['value'] for t in tokens])
        parser = Parser(tokens)
        parser.parse_S()
        
        # Verifica se todos os tokens foram consumidos
        if parser.pos < len(parser.tokens):
            raise SyntaxError(f"Erro: Tokens não consumidos após análise. Próximo: {parser.peek()}")
            
        print("\n✓ Cadeia válida!")
    except SyntaxError as e:
        print(f"\n✗ Erro de análise: {e}")
    except Exception as e:
        print(f"\nErro inesperado: {e}")


# Cadeias de teste
test_cases = [
    "x[:'Tested']", 
    
    # 1. Acesso por número
    "x[0]", 
    "x[-2]",
    
    # 2. Acesso por string
    "x['Date']", 
    "x[:'Tested']",
    
    # 3. Fatiamento numérico
    "x[0:5]", 
    "x[:]", 
    "x[6:]", 
    
    # 4. Fatiamento por strings
    "x['Data':'State']", 
    'x["District":"Tested"]',
    "x[\"Data\":]", 
    
    # 5. Acesso aninhado 
    "x[ y[0] ]", 
    "m[ n['State':'Data'] ]", 
    "base [ colunas [ : ] ]",

    
    # 6. Comparação 
    "x[ y['dia'] > 5 ]", 
    'base[ nome[-5:] != "João"]',
    "valor [ dias [ : ] == util ]",
    
    
    # 7. Erros
    
    'x[',
    "erro[0",
    "errando)1]",
    '[0]',
    "errei[5:texto]",
]

# Execução dos testes
for case in test_cases:
    run_parser(case)