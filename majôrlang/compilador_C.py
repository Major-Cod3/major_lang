from Parser import *


class compilador:
	def __init__(self,):
		script = """#include <stdio.h>
#include <stdlib.h>
int main() {
		"""
		self.linha = script.splitlines()
		del script
		self.variables = {}
		self.main = open('main.cpp','w')
	def node_data(self, node):
		for no in node:
			self.interpret(no,self.tamanho_final)
	def interpret(self, node,tamanho_final):
		self.tamanho_final = tamanho_final
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
		elif isinstance(node, Number):
			return node.value
		elif isinstance(node, String_str):
			return node.nome
		elif isinstance(node, IDENTIFIER):
			return node.name
		elif isinstance(node, BinaryOperation):
			return self.visit_binary_operation(node)
		else:
			
			raise Exception(f"Unknown AST node: {node}")
		if self.tamanho_final == 1:
			self.linha.append("}")
			self.main.write("\n".join(self.linha))
	def visit_var_assign(self,node):
	       self.variables[node.identifier] = self.interpret(node.value,self.tamanho_final)
	       match node.tipo:
	       	case 'INTEIRO':
	       		self.linha.append(f"int {node.identifier} = {self.interpret(node.value,self.tamanho_final)};")
	       	case 'FLOAT':
	       		self.linha.append(f"float {node.identifier} = {self.interpret(node.value,self.tamanho_final)};")
	       	case 'STRING':
	       		self.linha.append(f'char {node.identifier}[] = "{self.interpret(node.value,self.tamanho_final)}";')
	       	case None:
	       		self.linha.append(f'{node.identifier} = {self.interpret(node.value,self.tamanho_final)};')
	def visit_if_assign(self,node):
		self.linha.append(f"if ( " + str(self.interpret(node.condition,self.tamanho_final)) + ')')
		self.linha.append('{')
		self.node_data(node.body)
		self.linha.append("}")
		if node.else_body:
				self.linha.append('else{')
				self.node_data(node.else_body)
				self.linha.append("}")
				
	
	def visit_while_assign(self,node):
		self.linha.append(f"while ( " + str(self.interpret(node.condition,self.tamanho_final)) + ')')
		self.linha.append('{')
		self.node_data(node.body)
		self.linha.append("}")
	def visit_expand_assign(self,node):
		from Lexicon_Analyzer import lexer
		with open(node.arquivo, 'r') as modulo:
			modulo = modulo.read()
		lexer = lexer(modulo)
		parser = Parser(lexer).parser()
		self.linha.insert(2,"class "+node.identifier+" {\n"+"public:\n"+node.identifier+"() {\n")
		self.node_data(parser)
		self.linha.insert(3,'};\n};\n')
	def visit_def_assign(self,node):
		pass
		
	def visit_Mprint_assign(self,node):
		for i in node.value:
		  if isinstance(i, String_str):
		  	valor = f'"{self.interpret(i,self.tamanho_final)}"'
		  elif isinstance(i, IDENTIFIER):
		  	tipo = self.variables[self.interpret(i,self.tamanho_final)]
		  	if isinstance(tipo, float):
		  			valor = f'"%f",{self.interpret(i,self.tamanho_final)}'
		  	elif isinstance(tipo, int):
		  			valor = f'"%d",{self.interpret(i,self.tamanho_final)}'
		  	elif isinstance(tipo, str):
		  			valor = f'"%s",{self.interpret(i,self.tamanho_final)}'
		  self.linha.append(f'printf({valor});\n')
	def visit_binary_operation(self,node):
			left = node.left
			operator = node.operator
			right = node.right
			if operator =='+':
				return str(self.interpret(left,self.tamanho_final))+"+"+str(self.interpret(right,self.tamanho_final))
			elif operator =='-':
				return str(self.interpret(left,self.tamanho_final))+"-"+str(self.interpret(right,self.tamanho_final))
			elif operator =='*':
				return str(self.interpret(left,self.tamanho_final))+"*"+str(self.interpret(right,self.tamanho_final))
			elif operator =='^':
				return str(self.interpret(left,self.tamanho_final))+"^"+str(self.interpret(right,self.tamanho_final))
			elif operator =='/':
				return str(self.interpret(left,self.tamanho_final))+"/"+str(self.interpret(right,self.tamanho_final))
			elif operator =='>':
				return str(self.interpret(left,self.tamanho_final))+">"+str(self.interpret(right,self.tamanho_final))
			elif operator =='<':
				return str(self.interpret(left,self.tamanho_final))+"<"+str(self.interpret(right,self.tamanho_final))
			elif operator =='>=':
				return str(self.interpret(left,self.tamanho_final))+">="+str(self.interpret(right,self.tamanho_final))
			elif operator =='<=':
				return str(self.interpret(left,self.tamanho_final))+"<="+str(self.interpret(right,self.tamanho_final)) 
			elif operator =='==':
				return str(self.interpret(left,self.tamanho_final))+"=="+str(self.interpret(right,self.tamanho_final))
				