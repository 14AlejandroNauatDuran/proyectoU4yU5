import sys
import ply.yacc as yacc
from php_lexer import tokens

VERBOSE = 1

precedence = (
    ('left', 'INCLUDE', 'REQUIRE'),
    ('left', 'COMMA'),
    ('left', 'EQUAL', 'PLUSEQUAL', 'MINUSEQUAL'),
    ('left', 'SEMI'),
    ('left', 'OR'),
    ('left', 'XOR'),
    ('left', 'AND'),
    ('nonassoc', 'ISEQUAL', 'DEQUAL'),
    ('nonassoc', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('right', 'LBRACKET'),
    ('nonassoc', 'NEW', 'CLONE'),
    ('left', 'ELSEIF'),
    ('left', 'ELSE'),
    ('right', 'PRIVATE', 'PROTECTED', 'PUBLIC'),
)

def p_program(p):
    'program : OPENTAG declaration_list CLOSETAG'
    pass

def p_declaration_list(p):
   '''declaration_list : declaration_list  declaration
   					   | declaration
   '''
   pass

def p_declaration(p):
	'''declaration : var_declaration
				   | fun_declaration
				   | area fun_declaration
				   | header_declaration
				   | class_declaration
				   | echo_stmt
				   | selection_stmt
			       | iteration_stmt
				   | typeclass
	'''
	pass

def p_echo_stmt(p):
	'''echo_stmt : echo_stmt ECHO STRING SEMI
				 | echo_stmt ECHO IDVAR SEMI
				 | empty
				 | echo_stmt ECHO NUM SEMI
				 | echo_stmt ECHO boolean SEMI
				 | echo_stmt ECHO fun_declaration SEMI
	'''
	pass

def p_header_declaration(p):
	'''header_declaration : REQUIRE LPAREN STRING RPAREN SEMI
                          | INCLUDE LPAREN STRING RPAREN SEMI
    '''
	pass

def p_class_declaration(p):
	'''class_declaration : area CLASS ID LBLOCK attribute RBLOCK
						 | CLASS ID LBLOCK attribute RBLOCK
	'''
	pass

def p_attribute1(p):
	'''attribute : attribute area var_declaration
				 | area var_declaration
				 | attribute area fun_declaration
				 | area fun_declaration
	'''
	pass


def p_area(p):
	'''area : PRIVATE
			| PUBLIC
			| PROTECTED
	'''
	pass

def p_var_declaration(p):
	'''var_declaration : IDVAR SEMI var_declaration
                       | IDVAR SEMI
                       | TIMESTIMES IDVAR SEMI
                       | TIMESTIMES IDVAR SEMI var_declaration
                       | IDVAR EQUAL NUM SEMI var_declaration
                       | IDVAR EQUAL NUM SEMI
                       | IDVAR EQUAL boolean SEMI var_declaration
                       | IDVAR EQUAL boolean SEMI
                       | IDVAR EQUAL IDVAR SEMI var_declaration
                       | IDVAR EQUAL IDVAR SEMI
                       | AMPERSANT IDVAR SEMI var_declaration
                       | AMPERSANT IDVAR EQUAL IDVAR SEMI  selection_stmt
                       | AMPERSANT IDVAR SEMI
                       | IDVAR EQUAL simple_expression SEMI
	'''
	pass

def p_fun_declaration(p):
	'''fun_declaration : FUNCTION ID LPAREN params RPAREN
					   | FUNCTION ID LPAREN params RPAREN compount_stmt
	'''
	pass

def p_params(p):
	'''params : param_list
			  | empty
	'''
	pass

def p_param_list(p):
	'''param_list : param_list COMMA param_list
				  | param
	'''
	pass

def p_param(p):
	'''param : IDVAR
             | IDVAR LBRACKET RBRACKET
    '''
	pass


def p_compount_stmt(p):
	'compount_stmt : LBLOCK echo_stmt local_declarations echo_stmt statement_list echo_stmt RBLOCK'
	pass

def p_local_declarations(p):
	'''local_declarations : local_declarations var_declaration
						  | empty
	'''
	pass

def p_statement_list(p):
	'''statement_list : statement_list statement
					  | empty
	'''
	pass

def p_statement(p):
	'''statement : expression_stmt
				 | compount_stmt
				 | selection_stmt
				 | iteration_stmt
			     | return_stmt
			     | class_declaration
				 | echo_stmt
	'''
	pass
