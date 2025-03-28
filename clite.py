import ply.lex as lex

tokens = [ 'STR' , 'FLOAT' ,'INT' ]

t_ignore  = ' \t'

def t_STR(t):
  r'[a-zA-Z]+(\s[a-zA-Z]+)+'
  t.value = str(t.value)
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
