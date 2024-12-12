from AST import *
class Parser():
	def __init__(self,tokens):
		self.tokens = tokens
		self.Index = 0
		self.linha = 0
	def parser(self):
		statement = []
		while self.Index < len(self.tokens):
			
			statement.append(self.statement())
			
		return statement
		
	def statement(self):
		self.linha = self.tokens[self.Index][2]
		if self.match('DYNAMICS'):
			
			return self.var_assign()
		elif self.match('IF'):
			return self.if_statement()
		elif self.match('DEF'):
			return self.def_statement()
		elif self.match('WHILE'):
			return self.while_statement()
		elif self.match('EXPAND'):
			return self.expand_statement()
		elif self.match('MPRINT'):
			return self.mprint_statement()
		elif self.match('INPUT'):
			return self.input_statement()
		elif self.match('RETURN'):
			return self.return_statement()
		elif self.match('IDENTIFIER'):
			
			return self.var_update()
		elif self.match('DELETE'):
			var = self.consume('IDENTIFIER')[1]
			return Delete(var)
		else:
			print(self.tokens[self.Index])
			self.erro(f"Invalid primary token na linha:{self.linha}")
	def var_assign(self):
		#  variavel
		modelo = self.previous()
		tipor = self.tokens[self.Index]
		self.Index +=1
		self.consume('COLON')
		identifier = self.consume('IDENTIFIER')[1]
		self.consume('ATTRIBUTION')
		value = self.expression()
		if self.check_type(tipor[0],value):
			return VarAssign(identifier,value,tipor[0])
		else:
			self.expression()
	def var_update(self):
		
		identifier = self.tokens[self.Index-1][1]
		if self.check('ATTRIBUTION'):
			self.consume('ATTRIBUTION')
			value = self.expression()
			return VarAssign(identifier,value)
		elif self.check('LSQB'):
			self.consume('LSQB')
			value = self.expression()
			self.consume('RSQB')
			return ARRAYS_position(identifier, value)
		elif self.match('LPAREN') and self.match('RPAREN'):
			 	return function_call(identifier)
		return IDENTIFIER(identifier)
	def if_statement(self):
		#if
		self.consume('LPAREN')
		condition = self.expression()
		self.consume('RPAREN')
		self.consume('LBRACE')
		body =[]
		
		while not self.check('RBRACE'):

			body.append(self.statement())
		self.consume('RBRACE')
		#else
		else_body = []
		if self.check('ELSE'):
			self.consume('ELSE')
			self.consume('LBRACE')
			while not self.check('RBRACE'):
				else_body.append(self.statement())
			self.consume('RBRACE')
			
		return IFStatement(condition, body,else_body) 
	def def_statement(self):
		argumentos = []
		nome_funcao = self.consume('IDENTIFIER')[1]
		self.consume('LPAREN')
		if self.check('IDENTIFIER'):
			while not self.check('RPAREN'):
				argumentos.append(self.consume('IDENTIFIER')[1])
		self.consume('RPAREN')
		self.consume('LBRACE')
		body =[]
		while not self.check('RBRACE'):
			body.append(self.statement())
		self.consume('RBRACE')
		return DEFStatement(nome_funcao,argumentos, body)
		
	def while_statement(self):
		#while
		self.consume('LPAREN')
		condition = self.expression()
		self.consume('RPAREN')
		self.consume('LBRACE')
		body =[]
		while not self.check('RBRACE'):
			body.append(self.statement())
		self.consume('RBRACE')
		return WHILEStatement(condition, body)
	
	def expand_statement(self):
		 identifier = self.consume('IDENTIFIER')[1]
		 arquivo = self.consume('STRING')[1]
		 return EXPANDStatement(identifier,arquivo)
	def return_statement(self):
		self.consume('LBRACE')
		retorno = []
		while not self.check('RBRACE'):
			retorno.append(self.expression())
			retorno.append(self.statement())
		self.consume('RBRACE')
		return ReturnStatement(retorno)
	
	def mprint_statement(self):
		self.consume('LPAREN')
		mPrint = []
		while not self.check('RPAREN'):
			mPrint.append(self.expression())
		self.consume('RPAREN')
		return MPrint(mPrint)
	def input_statement(self):
		self.consume('LPAREN')
		variavel = self.consume('IDENTIFIER')[1]
		text = self.consume('STRING')[1]
		self.consume('RPAREN')
		return Input(variavel,text)
	def consume(self, token_type):
		if self.check(token_type):
			current_token = self.tokens[self.Index]
			self.Index += 1
			return current_token
		self.erro(f'SyntaxError: Unexpected token {token_type}, na linha:{self.linha}')
	def expression(self):
		left = self.primary_expression()
		while True:
			if self.match('MAIOR'):
				operator = '>'
			elif self.match('MENOR'):
				operator = '<'
			elif self.match('ENQUAL'):
				operator = '=='
			elif self.match('MAIORENQUAL'):
				operator = '>='
			elif self.match('MENORENQUAL'):
				operator = '<='
			elif self.match('SOM'):
				operator = '+'
			elif self.match('SUB'):
				operator = '-'
			elif self.match('MUT'):
				operator = '*'
			elif self.match('DIV'):
				operator = '/'
			elif self.match('POW'):
				operator = '**'
			else:
				break
			right = self.primary_expression()  # Captura a próxima expressão à direita
			left = BinaryOperation(left, operator, right)  # Combina as duas expressões
		return left
			
	def primary_expression(self):
		if self.match('INTEIRO'):
				return Number(int(self.previous()[1]))
		elif self.match('FLOAT'):
			return Number(float(self.previous()[1]))
		elif self.match('IDENTIFIER'):
			return self.var_update()
		elif self.match('STRING'):
			return String_str(str(self.previous()[1]))
		elif self.match('LPAREN'):
		      expr = self.expression()  # Permitir subexpressões entre parênteses
		      self.consume('RPAREN')  # Consumir ')'
		      return expr
		else:
			self.erro(f"Invalid primary expression na linha:{self.linha},{self.previous()}")
		
	def match(self,token_type):
		if self.check(token_type):
			self.Index += 1
			return True
		return False
	def check_type(self, expected_type, value):
		if isinstance(value, Number):
			if expected_type == 'INTEIRO' and value.is_integer() or expected_type == 'BIN8':
				return True
			elif expected_type == 'FLOAT' and value.is_float():
				return True
		elif isinstance(value, BinaryOperation):
		      left_type = self.check_type(expected_type, value.left)
		      right_type = self.check_type(expected_type, value.right)
		      return left_type and right_type
		elif isinstance(value, IDENTIFIER) or isinstance(value, ARRAYS_position):
			return True
		elif expected_type == 'STRING' and isinstance(value, String_str):
			if isinstance(value.nome, str):
				return True
		return False
		
	def check(self,token_type):
		return self.Index < len(self.tokens) and self.tokens[self.Index][0] == token_type
	
	def previous(self):
		return self.tokens[self.Index -1]
	
	def erro(self,message):
		raise Exception(message)




if __name__ == "__main__":
	tokens =[('INTEIRO', 'int', 2), ('COLON', ':', 2), ('IDENTIFIER', 'um', 2), ('ATTRIBUTION', '=', 2), ('INTEIRO', 0, 2), ('FLOAT', 'float', 3), ('COLON', ':', 3), ('IDENTIFIER', 'pi', 3), ('ATTRIBUTION', '=', 3), ('FLOAT', 3.14159, 3), ('WHILE', 'while', 4), ('LPAREN', '(', 4), ('IDENTIFIER', 'um', 4), ('MENOR', '<', 4), ('INTEIRO', 100, 4), ('RPAREN', ')', 4), ('LBRACE', '{', 5), ('MPRINT', 'mprint', 6), ('LPAREN', '(', 6), ('IDENTIFIER', 'um', 6), ('RPAREN', ')', 6), ('INTEIRO', 'int', 7), ('COLON', ':', 7), ('IDENTIFIER', 'um', 7), ('ATTRIBUTION', '=', 7), ('IDENTIFIER', 'um', 7), ('SOM', '+', 7), ('INTEIRO', 1, 7), ('RBRACE', '}', 8), ('MPRINT', 'mprint', 9), ('LPAREN', '(', 9), ('IDENTIFIER', 'pi', 9), ('RPAREN', ')', 9)]
	paser = Parser(tokens).parser()
	print(paser)