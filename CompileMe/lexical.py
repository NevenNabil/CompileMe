# Import the 'lex' module from the 'ply' package for lexical analysis.
import ply.lex as lex
# Import the 'kwlist' from the 'keyword' module to include Python keywords in the tokens.
from keyword import kwlist
from tkinter import messagebox

# Define lists for different categories of tokens.
operators = ["plus", "minus", "product", "division", "integer_division", "module", "power", "equals", "non_equal",
             "less", "greater",
             "less_equal", "greater_equal"]
delimiters = ["left_parenthesis", "right_parenthesis", "left_bracket", "right_bracket", "left_brace", "right_brace",
              "period", "comma", "colon",
              "semicolon", "at", "assign", "increment", "decrement", "self_product", "self_division",
              "self_integer_division", "self_module", "self_power"]
others = ["identifier", "identation", "backspace", "float", "integer", "string", "newline"]
# Combine all categories to create the list of all token types.
tokens = kwlist + operators + delimiters + others

# Define a regular expression pattern to ignore spaces.
t_ignore = ' '

# Define regular expressions for each operator token.
t_plus = r'\+'
t_minus = r'-'
t_product = r'\*'
t_division = r'/'
t_integer_division = r'//'
t_module = r'%'
t_power = r'\*\*'
t_equals = r'=='
t_non_equal = r'!='
t_less = r'<'
t_greater = r'>'
t_less_equal = r'<='
t_greater_equal = r'>='
# Define regular expressions for each delimiter token.
t_left_parenthesis = r'\('
t_right_parenthesis = r'\)'
t_left_bracket = r'\['
t_right_bracket = r']'
t_left_brace = r'{'
t_right_brace = r'}'
t_period = r'\.'
t_comma = r','
t_colon = r':'
t_semicolon = r';'
# Define regular expressions for each assignment operator token.
t_assign = r'='
t_increment = r'\+='
t_decrement = r'-='
t_self_product = r'\*='
t_self_division = r'/='
t_self_integer_division = r'//='
t_self_module = r'%='
t_self_power = r'\*\*='


# Define a function to handle the 'False' keyword token.
def t_False(t):
    r'False'
    return t


# Define a function to handle the 'None' keyword token.
def t_None(t):
    r'None'
    return t


# Define a function to handle the 'True' keyword token.
def t_True(t):
    r'True'
    return t


# Define a function to handle the 'and' keyword token.
def t_and(t):
    r'and'
    return t


# Define a function to handle the 'as' keyword token.
def t_as(t):
    r'as'
    return t


# Define a function to handle the 'assert' keyword token.
def t_assert(t):
    r'assert'
    return t


# Define a function to handle the 'break' keyword token.
def t_break(t):
    r'break'
    return t


# Define a function to handle the 'class' keyword token.
def t_class(t):
    r'class'
    return t


# Define a function to handle the 'continue' keyword token.
def t_continue(t):
    r'continue'
    return t


# Define a function to handle the 'def' keyword token.
def t_def(t):
    r'def'
    return t


# Define a function to handle the 'del' keyword token.
def t_del(t):
    r'del'
    return t


# Define a function to handle the 'elif' keyword token.
def t_elif(t):
    r'elif'
    return t


# Define a function to handle the 'else' keyword token.
def t_else(t):
    r'else'
    return t


# Define a function to handle the 'except' keyword token.
def t_except(t):
    r'except'
    return t


# Define a function to handle the 'finally' keyword token.
def t_finally(t):
    r'finally'
    return t


# Define a function to handle the 'for' keyword token.
def t_for(t):
    r'for'
    return t


# Define a function to handle the 'from' keyword token.
def t_from(t):
    r'from'
    return t


# Define a function to handle the 'global' keyword token.
def t_global(t):
    r'global'
    return t


# Define a function to handle the 'if' keyword token.
def t_if(t):
    r'if'
    return t


# Define a function to handle the 'import' keyword token.
def t_import(t):
    r'import'
    return t


# Define a function to handle the 'lambda' keyword token.
def t_lambda(t):
    r'lambda'
    return t


# Define a function to handle the 'nonlocal' keyword token.
def t_nonlocal(t):
    r'nonlocal'
    return t


# Define a function to handle the 'not' keyword token.
def t_not(t):
    r'not'
    return t


# Define a function to handle the 'or' keyword token.
def t_or(t):
    r'or'
    return t


# Define a function to handle the 'pass' keyword token.
def t_pass(t):
    r'pass'
    return t


# Define a function to handle the 'raise' keyword token.
def t_raise(t):
    r'raise'
    return t


# Define a function to handle the 'return' keyword token.
def t_return(t):
    r'return'
    return t


# Define a function to handle the 'try' keyword token.
def t_try(t):
    r'try'
    return t


# Define a function to handle the 'while' keyword token.
def t_while(t):
    r'while'
    return t


# Define a function to handle the 'with' keyword token.
def t_with(t):
    r'with'
    return t


# Define a function to handle the 'yield' keyword token.
def t_yield(t):
    r'yield'
    return t


# Define a function for recognizing identifiers.
def t_identifier(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


# Define a function to handle the 'in' keyword token.
def t_in(t):
    r'in'
    return t


# Define a function to handle the 'is' keyword token.
def t_is(t):
    r'is'
    return t


# Define a function to handle the '\n' keyword token.
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    return t


# Define a function to handle the '\t' keyword token.
def t_identation(t):
    r'\t'
    return t


# Define a function to handle the '\r' keyword token.
def t_backspace(t):
    r'\r'
    return t


# Define a function to handle the float.
def t_float(t):
    r'-?\d+\.\d*'
    t.value = float(t.value)
    return t


# Define a function to handle the integer.
def t_integer(t):
    r'-?\d+'
    t.value = int(t.value)
    return t


# Define a function to handle the string.
def t_string(t):
    r'(\" | \').*(\" | \')'
    return t


# Define a function to handle lexer errors.
def t_error(t):
    messagebox.showerror('Python Error', 'Error:' + "Invalid token %s at line %d, position %d"% (t.value, t.lineno, t.lexpos))
    t.lexer.skip(1)


# Define the main function for the lexer.
def main():
    text = ""
    # Open the input file for reading.
    file = open("input.py", "r")
    # Read the content of the file.
    content = file.read()
    file.close()

    input_text0 = ""
    fileWrite = open('graph.txt', 'w')
    fileWrite.write(input_text0)
    fileWrite.close()

    # Create a lexer instance.
    lexer = lex.lex()
    # Set the lexer input to the content of the file.
    lexer.input(content)
    # Iterate over the tokens produced by the lexer.
    while True:
        token = lexer.token()
        if not token:
            break
        # Print the token and add its string representation to the text.
        text += token.__str__() + "\n"
    return text
