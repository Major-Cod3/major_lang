from Parser import *
import sys

class compilador:
	def __init__(self,final):
		script = """#include <stdio.h>
#include <stdlib.h>
"""
		self.linha = script.splitlines()
		self._final = final
		del script
		self.variables = {}
		self.boffer = 0
		self.main = open('main.cpp','w')
	def node_data(self, node):
		
		
		backup_variables = list(self.variables.keys())
		
		
			
		for no in node:

			self.interpret(no)
		
		for i in list(self.variables.keys()):
			if not i in backup_variables:
				self.linha.append(f'free({i[1:]});')
				
				del self.variables[i]
		
		

	def interpret(self, node):
		if isinstance(node, VarAssign):
			self.visit_var_assign(node)
		elif isinstance(node, IFStatement):
			self.visit_if_assign(node)
		elif isinstance(node, WHILEStatement):
			self.visit_while_assign(node)
		elif isinstance(node, EXPANDStatement):
			self.visit_expand_assign(node)
		elif isinstance(node, DEFStatement):
			self.visit_def_assign(node)
		elif isinstance(node, MPrint):
			self.visit_Mprint_assign(node)
		elif isinstance(node, Input):
			self.visit_Input_assign(node)
		elif isinstance(node, Number):
			return node.value
		elif isinstance(node, String_str):
			return node.nome
		elif isinstance(node, IDENTIFIER):
			return '*' +node.name
		elif isinstance(node, ARRAYS_position):
			return self.visit_array_assign(node)
		elif isinstance(node, function_call):
			return self.linha.append(f"{node.nome}();")
		elif isinstance(node, BinaryOperation):
			return self.visit_binary_operation(node)
		elif isinstance(node, Delete):
			self.linha.append(f'free({node.nome});')
			del self.variables['*'+node.nome]
		else:
			
			raise Exception(f"Unknown AST node: {node}")
		
		if self._final == 0:
			self.main.write("\n".join(self.linha))
			sys.exit()
	def visit_var_assign(self,node):
	       self.variables['*'+node.identifier] = (node.tipo, self.interpret(node.value))
	       
	       match node.tipo:
	       	case 'INT8':
	       		self.linha.append(f"int *{node.identifier} =  (int*) malloc(1); *{node.identifier} = {self.interpret(node.value)};")
	       		self.boffer += 1
	       	case 'INT16':
	       		self.linha.append(f"int *{node.identifier} =  (int*) malloc(2); *{node.identifier} = {self.interpret(node.value)};")
	       		self.boffer += 2
	       	case 'INT32':
	       		self.linha.append(f"int *{node.identifier} =  (int*) malloc(4); *{node.identifier} = {self.interpret(node.value)};")
	       		self.boffer += 4
	       	case 'INT64':
	       		self.linha.append(f"int *{node.identifier} =  (int*) malloc(8); *{node.identifier} = {self.interpret(node.value)};")
	       		self.boffer += 8
	       	case 'FLOAT':
	       		self.linha.append(f"float *{node.identifier} =  (float*) malloc(8); *{node.identifier} = {self.interpret(node.value)};")
	       		self.boffer += 8
	       	case 'BIN8':
	       		self.linha.append(f'char *{node.identifier} =  (char*) malloc(1); *{node.identifier} = {self.interpret(node.value)};')
	       		self.boffer += 1
	       	case 'STRING':
	       		tamanho = len(self.interpret(node.value))
	       		self.linha.append(f'char *{node.identifier} =  (char*) malloc(sizeof(char)*{tamanho});')
	       		self.boffer += tamanho
	       		
	       		self.linha.append(f'snprintf({node.identifier}, {tamanho}, "{self.interpret(node.value)}");')
	       	case None:
	       		self.linha.append(f' *{node.identifier} = {self.interpret(node.value)};')
	def visit_if_assign(self,node):
		self.linha.append(f"if ( " + str(self.interpret(node.condition)) + ')')
		self.linha.append('{')
		self.node_data(node.body)
		self.linha.append("}")
		if node.else_body:
				self.linha.append('else{')
				self.node_data(node.else_body)
				self.linha.append("}")
				
	
	def visit_while_assign(self,node):
		self.linha.append(f"while ( " + str(self.interpret(node.condition)) + ')')
		self.linha.append('{')
		self.node_data(node.body)
		self.linha.append("}")
	def visit_expand_assign(self,node):
		from Lexicon_Analyzer import lexer
		with open(node.arquivo, 'r') as modulo:
			modulo = modulo.read()
		lexer = lexer(modulo)
		parser = Parser(lexer).parser()
		self.linha.append("class "+node.identifier+" {\n"+"public:\n"+node.identifier+"() {\n")
		self.node_data(parser)
		self.linha.append('};\n};\n')
		self._final -= 1
	def visit_def_assign(self,node):
		self.linha.append(f"int {node.name}()"+'{')
		numer_ = len(self.linha)
		
			
			
		self.node_data(node.body)
		if self.boffer > 0:
			self.linha.insert(numer_ , f'void *boffer =  malloc({self.boffer});')
			
			self.boffer = 0
			self.linha.append(f'free(boffer);')
		self.linha.append('}')
		self._final -= 1
	def visit_Mprint_assign(self,node):
		#print(node.value)
		for i in node.value:
		  #valor = None
		  #print(self.interpret(i))
		  if isinstance(i, String_str):
		  	valor = f'"{self.interpret(i)}"'
		  elif isinstance(i, IDENTIFIER):
		  	tipo = self.variables[self.interpret(i)][0]
		  	match tipo:
		  		case 'INT8' | 'BIN8' | 'INT16' | 'INT32' | 'INT64':
		  			valor = f'"%d",{self.interpret(i)}'
		  		case 'FLOAT':
		  			valor = f'"%f",{self.interpret(i)}'
		  		case 'STRING':
		  			valor = f'"%s",{self.interpret(i)[1:]}'
		  elif isinstance(i, ARRAYS_position):
		  	valor = f'"%d",{self.interpret(i)}'
		  elif isinstance(i, BinaryOperation):
		  	valor = f'"%d",{self.interpret(i)}'
		self.linha.append(f'printf({valor});\n')
	def visit_Input_assign(self,node):
		self.linha.append(f'printf("{node.text}");')
		valor = ""
		
		tipo = self.variables['*'+node.var][1]
		if isinstance(tipo, float):
		  	valor = "%f"
		elif isinstance(tipo, int):
			valor = "%d"
		elif isinstance(tipo, str):
			valor = "%s"
		self.linha.append(f'scanf("{valor}",{node.var});')
	
	
	def visit_array_assign(self,node):
		tipo = self.variables['*'+node.nome][0]
		match tipo:
			case 'BIN8':
				return f"(*{node.nome} & (1<< {node.position}))>=1"
	def visit_binary_operation(self,node):
			left = node.left
			operator = node.operator
			right = node.right
			#não remova os espaços
			if operator =='+':
				return str(self.interpret(left))+" + "+str(self.interpret(right))
			elif operator =='-':
				return str(self.interpret(left))+" - "+str(self.interpret(right))
			elif operator =='*':
				return str(self.interpret(left))+" * "+str(self.interpret(right))
			elif operator =='**':
				return (str(self.interpret(left))+" * " + str(self.interpret(left))) * self.interpret(right)
			elif operator =='/':
				return str(self.interpret(left))+" / "+str(self.interpret(right))
			elif operator =='>':
				return str(self.interpret(left))+" > "+str(self.interpret(right))
			elif operator =='<':
				return str(self.interpret(left))+" < "+str(self.interpret(right))
			elif operator =='>=':
				return str(self.interpret(left))+" >= "+str(self.interpret(right))
			elif operator =='<=':
				return str(self.interpret(left))+" <= "+str(self.interpret(right)) 
			elif operator =='==':
				return str(self.interpret(left))+" == "+str(self.interpret(right))
				