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