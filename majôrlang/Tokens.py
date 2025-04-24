from enum import Enum
#bit a bit
TOKENS ={
	#bitwise = {
	'&':'bitwise_AND',
	'|':'bitwise_OR',
	'^':'bitwise_XOR',
	'~':'bitwise_NOT',
	'>>':'bitwise_Shift_Right',
	'<<':'bitwise_Shift_Left',
	#}
	#Aritméticos = {
    '+': 'SOM',
    '-': 'SUB',
    '**': 'POW',
    '*': 'MUT',
    '/': 'DIV',
    
    #}
    
    #simbulos = {
	'=': 'ATTRIBUTION',
    '[': 'LSQB',
	']': 'RSQB',
	'{': 'LBRACE',
	'}': 'RBRACE',
	'(': 'LPAREN',
	')': 'RPAREN',
	':' : 'COLON',
	';' : 'SEMICOLON',
	#}
	#comparação = {
    '>': 'MAIOR',
    '<': 'MENOR',
    '==': 'IQUAL',
    '>=': 'MAIORIQUAL',
    '<=': 'MENORIQUAL',
    #}
    #lógicos = {
    'or': 'OR',
    'and': 'AND',
    'not': 'NOT',
    #}
    #tipo = {
    'int': 'INTEIRO',
    'i8': 'INT8',
    'i16': 'INT16',
    'i32': 'INT32',
    'i64': 'INT64',
    'u8': 'UINT8',
    'u16': 'UINT16',
    'u32': 'UINT32',
    'u64': 'UINT64',
    
    'float': 'FLOAT',
    'f32': 'FLOAT32',
    'f64': 'FLOAT64',
    'f128': 'FLOAT128',
    
    'b8': 'BIN8',
    'b16': 'BIN16',
    'b32': 'BIN32',
    'b64': 'BIN64',
    
    'str': 'STRING',
    'bool': 'BOOLEANO',
    #}
    #palavras_chave = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'true': 'TRUE',
    'false': 'FALSE',
    'expand': 'EXPAND',
    'def': 'DEF',
    'mprint': 'MPRINT',
    'input': 'INPUT',
    'return': 'RETURN',
    'del': 'DELETE',
    'dyn':  'DYNAMICS',
    'let': 'LET',
    #}
}
# Enumeração dos tokens
Tokens = Enum('Tokens', [
	#bit a bit
	'bitwise_AND',
	'bitwise_OR',
	'bitwise_XOR',
	'bitwise_NOT',
	'bitwise_Shift_Right',
	'bitwise_Shift_Left',
	#matematica
    'SOM',     #+
    'SUB',      #-
    'MUT',      #*
    'DIV',        #/
    'POW', 	#^
    #comparador
    'MAIOR', 	#>
    'MENOR',	 #<
    'IQUAL', 	#==
    'MAIORIQUAL', 	#>=
    'MENORIQUAL',	#<=
    #Símbolos
    'LSQB',	#[
    'RSQB',	# ]
    'LBRACE',	# {
    'RBRACE',	# }
    'LPAREN',    # (
    'RPAREN',   # )
    'ATTRIBUTION', # =
    'COLON',
    'SEMICOLON',
    #palavra_chaves
    'VAR',
    'IF', 
    'WHILE', 
    'TRUE', 
    'FALSE',
    'OR', 
    'AND', 
    'EXPAND',
    'OUTPUT',
    'INPUT',
    'ELSE',
    'DEF',
    'RETURN',
#DADOS
    'STRING',
    'INTEIRO',
    'FLOAT',
    'BOOLEANO',
    'IDENTIFIER',
#print
    'MPRINT',
])

# Mapeamento de palavras-chave e símbolos para tokens
token_map = {
    '+': Tokens.SOM,
    '-': Tokens.SUB,
    '*': Tokens.MUT,
    '/': Tokens.DIV,
    '^': Tokens.POW,
    '>': Tokens.MAIOR,
    '<': Tokens.MENOR,
    '==': Tokens.IQUAL,
    '>=': Tokens.MAIORIQUAL,
    '<=': Tokens.MENORIQUAL,
    '=': Tokens.ATTRIBUTION,
    '[': Tokens.LSQB,
	']': Tokens.RSQB,
	'{': Tokens.LBRACE,
	'}': Tokens.RBRACE,
	'(': Tokens.LPAREN,
	')': Tokens.RPAREN,
	':' : Tokens.COLON,
	';' : Tokens.SEMICOLON,
	'var': Tokens.VAR,
    'if': Tokens.IF,
    'else': Tokens.ELSE,
    'while': Tokens.WHILE,
    'true': Tokens.TRUE,
    'false': Tokens.FALSE,
    'OR': Tokens.OR,
    'AND': Tokens.AND,
    'expand': Tokens.EXPAND,
    'def': Tokens.DEF,
    'mprint': Tokens.MPRINT,
    'return': Tokens.RETURN,
    
    'int': Tokens.INTEIRO,
    'str': Tokens.STRING,
    'bool':Tokens.BOOLEANO,
    'float': Tokens.FLOAT,
}