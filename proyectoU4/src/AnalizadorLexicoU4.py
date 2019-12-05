# -*- coding: utf-8 -*-
import ply.lex as lex
import re
import codecs
import os
import sys 


tokens = ['VARIABLES','APE_PHP','CIE_PHP','CADENA','PCOMA','NUMEROS']

Reservadas = ['AND','DO','WHILE','FUNCTION','REQUIRE_ONCE','CLASS','FOR','ECHO','CASE','TRY',
        'NEW','FINALLY','IF'

]

OperadoresArit = ['SUMA','RESTA','MULTIPLICACION','DIVISION','POTENCIA']

OperadoresRela = ['MENOR','MAYOR','MENOR_IGUAL','MAYOR_IGUAL','IGUAL','DIFERENTE','DISTINTO','ASIGNACION']

bloquesParen = ['PARENTESIS_IZQ','PARENTESIS_DER','LLAVE_IZQ','LLAVE_DER']

tokens = tokens + Reservadas + OperadoresArit + OperadoresRela + bloquesParen
print(tokens)

t_AND = r'and'
t_DO = r'do'
t_WHILE = r'while'
t_FUNCTION = r'FUNCTION'
t_REQUIRE_ONCE = r'require_once'
t_CLASS = r'CLASS'
t_FOR = r'for'
t_ECHO = r'echo'
t_CASE = r'case'
t_TRY = r'try'
t_NEW = r'new'
t_FINALLY = r'finally'
t_IF = r'if'

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'

t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_DISTINTO = r'<>'
t_ASIGNACION = r'='

t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_PCOMA = r';'

#T_VARIABLES = r'[a-zA-Z_]\w*'
t_ignore = r' \t'

def t_NUMEROS(t):
    r'\d+.?\d*'
    return t