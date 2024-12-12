import re 
import Tokens
import Parser
import interpretador
import compilador_C
#Analisador Léxico
def lexer(code):
	# Palavras-chave
	linha = 1
	regex = re.compile(r'\b(del||if|wehile|true|false|expand|else|return|def|mprint|input)\b|'
		#tipagem
				   r'\b(int|srt|bool|float|b8)\b|'
				   r'#(.*?)\n|'
	# Operadores de comparação
                   r'(>=|<=|==|!=|>|<)|'
                   r'\*\*|'
	# Operadores aritméticos e de comparação simples
                   r'[+\-*/^><=;]|'
                   r':|'
	# Adiciona o símbolo de atribuição           
	# Números inteiros
	               r'[0-9]+\.[0-9]+|'
                   r'0x[0-9a-fA-F]+|0b[01]+|[0-9]+|'
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
		
		if value in Tokens.TOKENS:
			Tokenizer.append((Tokens.TOKENS[value],value,linha))
		elif re.match(r'[0-9]+\.[0-9]+', value):
			Tokenizer.append((Tokens.Tokens['FLOAT'].name, float(value), linha))
		#verifica se é um número
		elif re.match(r'[0-9]+|0x[0-9a-fA-F]+|0b[01]+', value):
			print(value)
			Tokenizer.append((Tokens.Tokens['INTEIRO'].name, int(value,16),linha))
		elif re.match(r'0x[0-9a-fA-F]+', value):
			print(value)
			Tokenizer.append((Tokens.Tokens['INTEIRO'].name, int(value),linha))
		elif re.match(r'0b[01]+', value):
			print(value)
			Tokenizer.append((Tokens.Tokens['INTEIRO'].name, int(value,2),linha))
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
			if len(value) > 0:
				print('ERRO:Token INVALIDO',value,'linha:',linha)
	return Tokenizer
		


if __name__ == "__main__":
	with open("/storage/emulated/0/major/python/linguagem_major/majôrlang/test/bit_array.mj", 'r') as arquivo:
		arquivo_e_linhas = arquivo.read()
	lexe = lexer(arquivo_e_linhas)
	#for i in lexe:
#		print(i)
	paser = Parser.Parser(lexe).parser()
	Interpreter = compilador_C.compilador(len(paser))
	for i in paser:
		Interpreter.interpret(i)