import re 
import Tokens
import Parser
import interpretador
import compilador_C
#Analisador Léxico
def lexer(code):
	# Palavras-chave
	linha = 1
	regex = re.compile(r'\b(var|if|wehile|true|false|expand|else|return|def|mprint)\b|'
				   r'\b(int|srt|bool|float)\b|'
				   r'#(.*?)\n|'
	# Operadores de comparação
                   r'(>=|<=|==|!=|>|<)|'
	# Operadores aritméticos e de comparação simples
                   r'[+\-*/^><=;]|'
                   r':|'
	# Adiciona o símbolo de atribuição           
	# Números inteiros
	               r'[0-9]+\.[0-9]+|'
                   r'[0-9]+|'                    
	# Identificadores              
                   r'[a-zA-Z_][a-zA-Z0-9_]*|' 
                   r'"[^"]*"|'
                   r"'[^']*'|"
                   r'[\{\}\[\]\(\)]|'
                   r'\n'
                   ) 
	Tokenizer = []
	for match in regex.finditer(code):
		value = match.group(0)
		## Verifica se o valor está no mapa de tokens, como palavras-chave ou operadores
		
		if value in Tokens.token_map:
			Tokenizer.append((Tokens.token_map[value].name,value,linha))
		elif re.match(r'[0-9]+\.[0-9]+', value):
			Tokenizer.append((Tokens.Tokens['FLOAT'].name, float(value), linha))
		#verifica se é um número
		elif re.match(r'[0-9]+', value):
			Tokenizer.append((Tokens.Tokens['INTEIRO'].name, int(value),linha))
		
		elif re.match( r'"[^"]*"', value) or re.match( r"'[^']*'", value):
			Tokenizer.append((Tokens.Tokens['STRING'].name,value.strip('"\''), linha))
		#Verifica se é um identificador
		elif re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', value):
			Tokenizer.append((Tokens.Tokens['IDENTIFIER'].name, value,linha))
		elif re.match(r'#(.*?)\n', value):
			#comentario
			linha += 1
			continue
		elif re.match(r'\n', value):
			linha += 1
		else:
			print('ERRO:Token INVALIDO',value)
	return Tokenizer
		


if __name__ == "__main__":
	with open("/storage/emulated/0/major/python/linguagem major/test/main.tst", 'r') as arquivo:
		arquivo_e_linhas = arquivo.read()
	lexe = lexer(arquivo_e_linhas)
	
	paser = Parser.Parser(lexe).parser()
	Interpreter = compilador_C.compilador()
	t = len(paser)
	for i in paser:
		Interpreter.interpret(i,t)
		t -=1