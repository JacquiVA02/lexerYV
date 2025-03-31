import ply.lex as lex

tokens = [ 'STR' , 'STR2' , 'FLOAT' ,'INT' ]

states = (
  ('string', 'exclusive'),
)

t_ignore  = ' \t'

def t_STR(t):
  r'[a-zA-Z]+(\s[a-zA-Z]+)+'
  t.value = str(t.value)
  return t

def t_STR2(t):
    r'"'
    setattr(t.lexer, "str_buffer", '"') 
    t.lexer.begin('string')

def t_string_content(t):
    r'[^"\\]+|\\(.)'
    t.lexer.str_buffer += t.value

def t_string_placeholder(t):
    r'[\"\']%s[\"\']'
    t.lexer.str_buffer += t.value

def t_string_end(t):
    r'"'
    t.lexer.str_buffer += '"'
    t.value = t.lexer.str_buffer
    t.type = 'STR2'
    t.lexer.begin('INITIAL')
    return t

def t_FLOAT(t):
  r'([0-9]+([_][0-9]+)*[.][0-9]*([eE][+-]?[0-9]+([_][0-9])?)?|[0-9]+([_][0-9]+)*[eE][+-]?[0-9]+([_][0-9]+)?|[.][0-9]+([eE][+-][0-9]+)?)'
  t.value = float(t.value)
  return t

def t_INT(t):
  r'[0-9]+([_][0-9]+)*'
  t.value = int(t.value)
  return t

def getLexer():
  return lex.lex()
