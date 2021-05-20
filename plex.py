import ply.lex as lex

# List of tokens
tokens = (
   'ID',
   'PLUS',
   'TIMES',
   'LPAREN',
   'RPAREN'
)

# Regular expression rules for simple tokens
t_ID      = r'[a-c]'
t_PLUS    = r'\+'
t_TIMES   = r'\*'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# # Test it out
# data = '''(3 + 4) * 10'''

# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
#     # type, value, location, and index