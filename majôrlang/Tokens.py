from enum import Enum

# Enumeração dos tokens
Tokens = Enum('Tokens', [
	#matematica
    'SOM',     #+
    'SUB',      #-
    'MUT',      #*
    'DIV',        #/
    'POW', 	#^
    #comparador
    'MAIOR', 	#>
    'MENOR',	 #<
    'ENQUAL', 	#==
    'MAIORENQUAL', 	#>=
    'MENORENQUAL',	#<=
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
    '==': Tokens.ENQUAL,
    '>=': Tokens.MAIORENQUAL,
    '<=': Tokens.MENORENQUAL,
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