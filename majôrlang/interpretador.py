from Parser import *


class Interpreter:
    def __init__(self,name=''):
        self.name = name
        self.variables = {}
    def node_data(self, node):
        for no in node:
            self.interpret(no)
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
        elif isinstance(node, Number):
            return node.value
        elif isinstance(node, String_str):
            return node.nome
        elif isinstance(node, IDENTIFIER):
            return self.variables.get(node.name, None)
        elif isinstance(node, BinaryOperation):
            return self.visit_binary_operation(node)
        else:
            
            raise Exception(f"Unknown AST node: {node}")
    def visit_var_assign(self,node):
        self.variables[node.identifier] = self.interpret(node.value)
    def visit_if_assign(self,node):
        if self.interpret(node.condition):
                self.node_data(node.body)
        elif node.else_body:
                self.node_data(node.else_body)
    def visit_while_assign(self,node):
        while self.interpret(node.condition):
            self.node_data(node.body)
    def visit_expand_assign(self,node):
        from Lexicon_Analyzer import lexer
        with open(node.arquivo, 'r') as modulo:
            modulo = modulo.read()
        lexer = lexer(modulo)
        parser = Parser(lexer).parser()
        self.node_data(parser)
    
    def visit_def_assign(self,node):
        pass
        
    def visit_Mprint_assign(self,node):
        mprint = ''
        for i in node.value:
          mprint += str(self.interpret(i))
        print(mprint)
    def visit_binary_operation(self,node):
            left = node.left
            operator = node.operator
            right = node.right
            if operator =='+':
                return self.interpret(left) + self.interpret(right)
            elif operator =='-':
                return self.interpret(left) - self.interpret(right)
            elif operator =='*':
                return self.interpret(left) * self.interpret(right)
            elif operator =='^':
                return self.interpret(left) ^ self.interpret(right)
            elif operator =='/':
                return self.interpret(left) / self.interpret(right)
            elif operator =='>':
                return self.interpret(left) > self.interpret(right)
            elif operator =='<':
                return self.interpret(left) < self.interpret(right)
            elif operator =='>=':
                return self.interpret(left) >= self.interpret(right)
            elif operator =='<=':
                return self.interpret(left) <= self.interpret(right)
            elif operator =='==':
                return self.interpret(left) == self.interpret(right)