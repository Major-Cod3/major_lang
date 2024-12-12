class ASTNode:
	def __init__(self):
		self.fim = ';'
class VarAssign(ASTNode):
	def __init__(self,identifier, value,tipo=None):
	       super().__init__()
	       self.tipo = tipo
	       self.identifier = identifier
	       self.value = value
		
class IFStatement(ASTNode):
	def __init__(self,condition, body,else_body=None):
	       super().__init__()
	       self.condition = condition
	       self.body=body
	       self.else_body =else_body

class WHILEStatement(ASTNode):
	def __init__(self,condition, body):
	       super().__init__()
	       self.condition = condition
	       self.body=body

class EXPANDStatement(ASTNode):
	def __init__(self,identifier, arquivo):
	       super().__init__()
	       self.identifier = identifier
	       self.arquivo = arquivo
	       

class DEFStatement(ASTNode):
	def __init__(self,name, condition, body):
	       super().__init__()
	       self.name = name
	       self.condition = condition
	       self.body=body

class ReturnStatement(ASTNode):
	def __init__(self,retorno):
	       super().__init__()
	       self.retorno = retorno
class MPrint(ASTNode):
	def __init__(self,value):
	       super().__init__()
	       self.value = value
class Input(ASTNode):
	def __init__(self,variavel,text):
	       super().__init__()
	       self.text = text
	       self.var = variavel
class Number:
    def __init__(self, value):
        super().__init__()
        self.value = value
    
    def is_integer(self):
        # Verifica se o valor é inteiro
        return isinstance(self.value, int)
    
    def is_float(self):
        # Verifica se o valor é float
        return isinstance(self.value, float)

    def __repr__(self):
        return str(self.value)  # Para fins de debug, exibe o valor

class String_str(ASTNode):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
    
    
    def __repr__(self):
        return f'str({self.nome})'  # Para fins de debug, exibe o valor

class IDENTIFIER(ASTNode):
	def __init__(self,name):
	       super().__init__()
	       self.name = name
	def __repr__(self):
		return f'IDENTIFIER({self.name})'  # Para fins de debug, exibe o valor

class BinaryOperation(ASTNode):
    def __init__(self, left, operator, right):
        super().__init__()
        self.left = left
        self.operator = operator
        self.right = right
    def __repr__(self):
        return f"({self.left} {self.operator} {self.right})"  # Para fins de debug, exibe o valor
       
class function_call(ASTNode):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
    
    
    def __repr__(self):
        return 'function call'  # Para fins de debug, exibe o valor

class Delete(ASTNode):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
    
    
    def __repr__(self):
        return f'Delete({self.nome})'  # Para fins de debug, exibe o valor

class ARRAYS_position(ASTNode):
    def __init__(self, nome,position):
        super().__init__()
        self.nome = nome
        self.position = position