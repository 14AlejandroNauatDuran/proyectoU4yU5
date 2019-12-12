import sys
import ply.lex as lex

# TOKENS http://php.net/manual/es/tokens.php
tokens = (

    # OPEN AND CLOSE TAG
    'OPENTAG','CLOSETAG',

    # RESERVERD WORDS LIST
    # http://php.net/manual/es/reserved.keywords.php
    '__HALT_COMPILER','ABSTRACT','AND','ARRAY','AS','BREAK','CALLABLE','CASE',
    'CATCH','CLASS','CLONE','CONST','CONTINUE','DECLARE','DEFAULT','DIE','DO',
    'ECHO','ELSE','ELSEIF','EMPTY','ENDDECLARE','ENDFOR','ENDFOREACH','ENDIF',
    'ENDSWITCH','ENDWHILE','EVAL','EXIT','EXTENDS','CLOSETAGAL','FOR','FOREACH',
    'FUNCTION','GLOBAL','GOTO','IF','IMPLEMENTS','INCLUDE','INCLUDE_ONCE',
    'INSTANCEOF','INSTEADOF','INTERFACE','ISSET','LIST','NAMESPACE','NEW','OR',
    'PRINT','PRIVATE','PROTECTED','PUBLIC','REQUIRE','REQUIRE_ONCE','RETURN',
    'STATIC','SWITCH','THROW','TRAIT','TRY','UNSET','USE','VAR','WHILE','XOR',

    #boolean
    'TRUE','FALSE',

    # SYMBOLS
    'PLUS','PLUSPLUS','PLUSEQUAL','MINUS','MINUSMINUS','MINUSEQUAL','TIMES',
    'TIMESTIMES','DIVIDE','LESS','LESSEQUAL','GREATER','GREATEREQUAL','EQUAL',
    'DEQUAL','DISTINT','ISEQUAL','SEMI','COMMA','LPAREN','RPAREN','LBRACKET',
    'RBRACKET','LBLOCK','RBLOCK','COLON','AMPERSANT','HASHTAG','DOT','QUOTES',
    'APOSTROPHE','DOT_DOT',

    # OTHERS
    'COMMENTS','COMMENTS_C99','ID','IDVAR','NUM','STRING','VOID',
)


# RE Tokens

# Take from: http://www.dabeaz.com/ply/example.html
# Ignored characters
t_ignore = " \t"

def t_VOID(t):
    r'VOID|void'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print (chr(27)+"[1;31m"+"\t ERROR: Illegal character"+chr(27)+"[0m")
    print ("\t\tLine: "+str(t.lexer.lineno)+"\t=> " + t.value[0])
    t.lexer.skip(1)


# RE OPEN AND CLOSE TAG
def t_OPENTAG(t):
    r'(<\?(php)?)'
    return t

def t_CLOSETAG(t):
    r'\?>'
    return t


# RE RESERVERD WORDS LIST
def t___HALT_COMPILER(t):
    r'__halt_compiler'
    return t

def t_ABSTRACT(t):
    r'abstract'
    return t

def t_AND(t):
    r'and|AND|\&\&'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_AS(t):
    r'as'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CALLABLE(t):
    r'callable'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CLONE(t):
    r'clone'
    return t

def t_CONST(t):
    r'const'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DECLARE(t):
    r'declare'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DIE(t):
    r'die'
    return t

def t_DO(t):
    r'do'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELSEIF(t):
    r'elseif'
    return t

def t_EMPTY(t):
    r'empty'
    return t

def t_ENDDECLARE(t):
    r'enddeclare'
    return t

def t_ENDFOR(t):
    r'endfor'
    return t

def t_ENDFOREACH(t):
    r'endforeach'
    return t

def t_ENDIF(t):
    r'endif'
    return t

def t_ENDSWITCH(t):
    r'endswitch'
    return t

def t_ENDWHILE(t):
    r'endwhile'
    return t

def t_EVAL(t):
    r'eval'
    return t

def t_EXIT(t):
    r'exit'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_CLOSETAGAL(t):
    r'CLOSETAGal'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FUNCTION(t):
    r'function'
    return t