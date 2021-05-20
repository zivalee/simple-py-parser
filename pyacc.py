import ply.yacc as yacc
from plex import tokens

# EXPR
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

# TERM
def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

# FACTOR
def p_factor_expression(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]
    
def p_factor_ID(p):
    'factor : ID'
    if p[1] == 'a':
        p[0] = aVal
    elif p[1] == 'b':
        p[0] = bVal
    elif p[1] == 'c':
        p[0] = cVal

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('Calc > ')
       aVal = int(input('   a > '))
       bVal = int(input('   b > '))
       cVal = int(input('   c > '))
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print('Ans > ' + str(result))