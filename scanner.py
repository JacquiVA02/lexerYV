import ply.lex as lex

tokens = [ 'INT' ]

t_INT = r'[0-9]+'

lexer = lex.lex()

lexer.input("123 456")

while True:
    token = lexer.token()
    if not token:
        break
    print(token)