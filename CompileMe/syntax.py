import ply.yacc as yacc
import semantic
from semantic import *
from tkinter import messagebox
from lexical import tokens

# Define the precedence of operators in the grammar
precedence = (
    ("left", "or"),
    ("left", "and"),
    ("right", "not"),
    ("right", "in"),
    ("right", "is"),
    ("right", "assign"),
    ("right", "increment", "decrement", "self_product", "self_division",
     "self_integer_division", "self_module", "self_power"),
    ("left", "equals", "non_equal"),
    ("left", "less", "greater", "less_equal", "greater_equal"),
    ("left", "plus", "minus"),
    ("left", "product", "division", "integer_division", "module"),
    ("left", "power"),
    ("left", "left_parenthesis", "right_parenthesis"),
)


def p_program(p):
    """program : statement_list"""
    # Parse a program consisting of a statement list
    p[0] = Program("Program", p[1])


def p_statement1(p):
    """statement : block_statement"""
    # Parse a statement as a block statement
    p[0] = NonTerminal("Block statement", p[1])


def p_block_statement1(p):
    """block_statement : header newline inner_statement_list backspace"""
    # Parse a block statement with a header, newline, inner statement list, and backspace
    p[0] = NonTerminal("Block statement", p[1], p[3])


def p_block_statement2(p):
    """block_statement : header newline inner_statement_list"""
    # Parse a block statement with a header, newline, and inner statement list
    p[0] = NonTerminal("Block statement", p[1], p[3])


def p_empty_block(p):
    """block_statement : empty"""
    # Parse an empty block statement
    p[0] = Null()


def p_header1(p):
    """header : defined_function"""
    # Parse a header with a defined function
    p[0] = NonTerminal("Header", p[1])


def p_header2(p):
    """header : conditional_statement"""
    # Parse a header with a conditional statement
    p[0] = NonTerminal("Header", p[1])


def p_header3(p):
    """header : repetitive_statement"""
    # Parse a header with a repetitive statement
    p[0] = NonTerminal("Header", p[1])


def p_defined_function(p):
    """defined_function : def identifier left_parenthesis parameter right_parenthesis colon"""
    # Parse a defined function
    p[0] = NonTerminal("Defined function", Terminal(p[2]), p[4])


def p_parameter1(p):
    """parameter : identifier"""
    # Parse a function parameter with an identifier
    p[0] = NonTerminal("Function parameter 1", Terminal(p[1]))


def p_parameter2(p):
    """parameter : parameter comma identifier"""
    # Parse a function parameter with multiple identifiers
    p[0] = NonTerminal("Function parameter 1", p[1], Terminal(p[3]))


def p_parameter3(p):
    """parameter : empty"""
    # Parse no function parameters
    p[0] = Null()


def p_conditional_statement1(p):
    """conditional_statement : if boolean_expression colon"""
    # Parse an 'if' statement with a boolean expression and a colon
    p[0] = NonTerminal("If", p[2])


def p_conditional_statement2(p):
    """conditional_statement : if boolean colon"""
    # Parse an 'if' statement with a boolean and a colon
    p[0] = NonTerminal("If", p[2])


def p_conditional_statement3(p):
    """conditional_statement : elif boolean_expression colon"""
    # Parse an 'else-if' statement with a boolean expression and a colon
    p[0] = NonTerminal("Else-if", p[2])


def p_conditional_statement4(p):
    """conditional_statement : elif boolean colon"""
    # Parse an 'else-if' statement with a boolean and a colon
    p[0] = NonTerminal("Else-if", p[2])


def p_conditional_statement5(p):
    """conditional_statement : else colon"""
    # Parse an 'else' statement with a colon
    p[0] = NonTerminal("Else")


def p_repetitive_statement1(p):
    """repetitive_statement : for identifier in identifier colon"""
    # Parse a 'for' loop statement with an identifier, 'in' keyword, identifier, and a colon
    p[0] = NonTerminal("For loop", Terminal(p[2]), Terminal(p[4]))


def p_repetitive_statement2(p):
    """repetitive_statement : while boolean_expression colon"""
    # Parse a 'while' loop statement with a boolean expression and a colon
    p[0] = NonTerminal("While loop", p[2])


def p_repetitive_statement3(p):
    """repetitive_statement : while boolean colon"""
    # Parse a 'while' loop statement with a boolean and a colon
    p[0] = NonTerminal("While loop", p[2])


def p_inner_statement_list1(p):
    """inner_statement_list : inner_statement newline"""
    # Parse an inner statement list with an inner statement followed by a newline
    p[0] = NonTerminal("Inner statement 1", p[1])


def p_inner_statement_list2(p):
    """inner_statement_list : inner_statement"""
    # Parse an inner statement list with a single inner statement
    p[0] = NonTerminal("Inner statement 2", p[1])


def p_inner_statement_list3(p):
    """inner_statement_list : inner_statement_list inner_statement newline"""
    # Parse a continuation of an inner statement list with another inner statement and a newline
    p[0] = NonTerminal("Inner statement 3", p[1], p[2])


def p_inner_statement_list4(p):
    """inner_statement_list : inner_statement_list inner_statement"""
    # Parse a continuation of an inner statement list with another inner statement
    p[0] = NonTerminal("Inner statement 4", p[1], p[2])


def p_inner_statement1(p):
    """inner_statement : identation statement"""
    # Parse an inner statement with an indentation followed by a statement
    p[0] = NonTerminal("Inner statement", p[2])


def p_inner_statement2(p):
    """inner_statement : identation inner_statement"""
    # Parse an inner statement with an indentation followed by another inner statement
    p[0] = NonTerminal("Inner statement", p[2])


def p_statement_list1(p):
    """statement_list : statement newline"""
    # Parse a statement list with a statement followed by a newline
    p[0] = NonTerminal("Statement 1", p[1])


def p_statement_list2(p):
    """statement_list : statement"""
    # Parse a statement list with a single statement
    p[0] = NonTerminal("Statement 2", p[1])


def p_statement_list3(p):
    """statement_list : statement_list statement newline"""
    # Parse a continuation of a statement list with another statement and a newline
    p[0] = NonTerminal("Statement 3", p[1], p[2])


def p_statement_list4(p):
    """statement_list : statement_list statement"""
    # Parse a continuation of a statement list with another statement
    p[0] = NonTerminal("Statement 4", p[1], p[2])


def p_empty_statement_list(p):
    """statement_list : empty"""
    # Parse an empty statement list
    p[0] = Null()


def p_statement2(p):
    """statement : assign_value"""
    # Parse a statement with an assign value
    p[0] = NonTerminal("Assign statement", p[1])


def p_assign_value(p):
    """assign_value : identifier assign_operator value"""
    # Parse an assign value statement with an identifier, assign operator, and a value
    p[0] = NonTerminal("Assign value", Terminal(p[1]), p[2], p[3])


def p_assign_operator1(p):
    """assign_operator : assign"""
    # Parse an assign operator with an assign symbol
    p[0] = NonTerminal("Assign", Terminal(p[1]))


def p_assign_operator2(p):
    """assign_operator : update"""
    # Parse an assign operator with an update symbol
    p[0] = NonTerminal("Update", p[1])


def p_update1(p):
    """update : increment"""
    p[0] = NonTerminal("Increment or self string concatenation", Terminal(p[1]))


def p_update2(p):
    """update : decrement"""
    p[0] = NonTerminal("Decrement", Terminal(p[1]))


def p_update3(p):
    """update : self_product"""
    p[0] = NonTerminal("Self product", Terminal(p[1]))


def p_update4(p):
    """update : self_division"""
    p[0] = NonTerminal("Self division", Terminal(p[1]))


def p_update5(p):
    """update : self_integer_division"""
    p[0] = NonTerminal("Self integer division", Terminal(p[1]))


def p_update6(p):
    """update : self_module"""
    p[0] = NonTerminal("Self module", Terminal(p[1]))


def p_update7(p):
    """update : self_power"""
    p[0] = NonTerminal("Self power", Terminal(p[1]))


def p_value1(p):
    """value : number"""
    p[0] = NonTerminal("Number", p[1])


def p_number1(p):
    """number : float"""
    p[0] = NonTerminal("Float", Terminal(p[1]))


def p_number2(p):
    """number : integer"""
    p[0] = NonTerminal("Integer", Terminal(p[1]))


def p_number3(p):
    """number : identifier"""
    p[0] = NonTerminal("Variable", Terminal(p[1]))


def p_value2(p):
    """value : boolean"""
    p[0] = NonTerminal("Boolean", p[1])


def p_boolean1(p):
    """boolean : True"""
    p[0] = NonTerminal("True", Terminal(p[1]))


def p_boolean2(p):
    """boolean : False"""
    p[0] = NonTerminal("False", Terminal(p[1]))


def p_boolean3(p):
    """boolean : identifier"""
    p[0] = NonTerminal("Variable", Terminal(p[1]))


def p_value3(p):
    """value : text"""
    p[0] = NonTerminal("Text", p[1])


def p_text1(p):
    """text : string"""
    p[0] = NonTerminal("String", Terminal(p[1]))


def p_text2(p):
    """text : formatted_string"""
    p[0] = NonTerminal("Formatted string", p[1])


def p_text3(p):
    """text : identifier"""
    p[0] = NonTerminal("Variable", Terminal(p[1]))


def p_formatted_string(p):
    """formatted_string : text module left_parenthesis element right_parenthesis"""
    p[0] = NonTerminal("Formatted string", Terminal(p[1]), Terminal(p[2]), p[4])


def p_value4(p):
    """value : expression"""
    p[0] = NonTerminal("Expression", p[1])


def p_expression1(p):
    """expression : arithmetic_expression"""
    p[0] = NonTerminal("Arithmetic expression", p[1])


def p_arithmetic_expression1(p):
    """arithmetic_expression : number arithmetic_operator number"""
    p[0] = NonTerminal("Arithmetic expression 1", p[1], p[2], p[3])


def p_arithmetic_expression2(p):
    """arithmetic_expression : arithmetic_expression arithmetic_operator number"""
    p[0] = NonTerminal("Arithmetic expression 2", p[1], p[2], p[3])


def p_arithmetic_operator1(p):
    """arithmetic_operator : plus"""
    p[0] = NonTerminal("Sum", Terminal(p[1]))


def p_arithmetic_operator2(p):
    """arithmetic_operator : minus"""
    p[0] = NonTerminal("Difference", Terminal(p[1]))


def p_arithmetic_operator3(p):
    """arithmetic_operator : product"""
    p[0] = NonTerminal("Product", Terminal(p[1]))


def p_arithmetic_operator4(p):
    """arithmetic_operator : division"""
    p[0] = NonTerminal("Division", Terminal(p[1]))


def p_arithmetic_operator5(p):
    """arithmetic_operator : integer_division"""
    p[0] = NonTerminal("Integer division", Terminal(p[1]))


def p_arithmetic_operator6(p):
    """arithmetic_operator : module"""
    p[0] = NonTerminal("Module", Terminal(p[1]))


def p_arithmetic_operator7(p):
    """arithmetic_operator : power"""
    p[0] = NonTerminal("Power", Terminal(p[1]))


def p_expression2(p):
    """expression : boolean_expression"""
    p[0] = NonTerminal("Boolean expression", p[1])


def p_boolean_expression1(p):
    """boolean_expression : number relational_operator number"""
    p[0] = NonTerminal("Boolean expression 1", p[1], p[2], p[3])


def p_boolean_expression2(p):
    """boolean_expression : arithmetic_expression relational_operator number"""
    p[0] = NonTerminal("Boolean expression 2", p[1], p[2], p[3])


def p_boolean_expression3(p):
    """boolean_expression : number relational_operator arithmetic_expression"""
    p[0] = NonTerminal("Boolean expression 3", p[1], p[2], p[3])


def p_boolean_expression4(p):
    """boolean_expression : arithmetic_expression relational_operator arithmetic_expression"""
    p[0] = NonTerminal("Boolean expression 4", p[1], p[2], p[3])


def p_boolean_expression5(p):
    """boolean_expression : boolean boolean_operator boolean"""
    p[0] = NonTerminal("Boolean expression 5", p[1], p[2], p[3])


def p_boolean_expression6(p):
    """boolean_expression : not boolean"""
    p[0] = NonTerminal("Boolean expression 6", Terminal(p[1]), p[2])


def p_boolean_expression7(p):
    """boolean_expression : not boolean_expression"""
    p[0] = NonTerminal("Boolean expression 7", Terminal(p[1]), p[2])


def p_boolean_expression8(p):
    """boolean_expression : boolean_expression boolean_operator boolean"""
    p[0] = NonTerminal("Boolean expression 8", p[1], p[2], p[3])


def p_boolean_expression9(p):
    """boolean_expression : boolean_expression relational_operator number"""
    p[0] = NonTerminal("Boolean expression 9", p[1], p[2], p[3])


def p_boolean_expression10(p):
    """boolean_expression : boolean_expression relational_operator arithmetic_expression"""
    p[0] = NonTerminal("Boolean expression 10", p[1], p[2], p[3])


def p_relational_operator1(p):
    """relational_operator : equals"""
    p[0] = NonTerminal("Equals", Terminal(p[1]))


def p_relational_operator2(p):
    """relational_operator : non_equal"""
    p[0] = NonTerminal("Non_equal", Terminal(p[1]))


def p_relational_operator3(p):
    """relational_operator : less"""
    p[0] = NonTerminal("Less", Terminal(p[1]))


def p_relational_operator4(p):
    """relational_operator : greater"""
    p[0] = NonTerminal("Greater", Terminal(p[1]))


def p_relational_operator5(p):
    """relational_operator : less_equal"""
    p[0] = NonTerminal("Less equal", Terminal(p[1]))


def p_relational_operator6(p):
    """relational_operator : greater_equal"""
    p[0] = NonTerminal("Greater equal", Terminal(p[1]))


def p_boolean_operator1(p):
    """boolean_operator : and"""
    p[0] = NonTerminal("And", Terminal(p[1]))


def p_boolean_operator2(p):
    """boolean_operator : or"""
    p[0] = NonTerminal("Or", Terminal(p[1]))


def p_expression_3(p):
    """expression : string_concatenation"""
    p[0] = NonTerminal("String concatenation", p[1])


def p_string_concatenation1(p):
    """string_concatenation : text plus text"""
    p[0] = NonTerminal("String concatenation 1", p[1], Terminal(p[2]), p[3])


def p_string_concatenation2(p):
    """string_concatenation : string_concatenation plus text"""
    p[0] = NonTerminal("String concatenation 2", p[1], Terminal(p[2]), p[3])


def p_value5(p):
    """value : list"""
    p[0] = NonTerminal("List", p[1])


def p_value6(p):
    """value : function_call"""
    p[0] = NonTerminal("Function", p[1])


def p_value7(p):
    """value : None"""
    p[0] = Terminal(p[1])


def p_list(p):
    """list : left_bracket element right_bracket"""
    p[0] = NonTerminal("List statement", p[2])


def p_element1(p):
    """element : value"""
    p[0] = NonTerminal("Element", p[1])


def p_element2(p):
    """element : element comma value"""
    p[0] = NonTerminal("Elements", p[1], p[3])


def p_statement4(p):
    """statement : function_call"""
    p[0] = NonTerminal("Function call statement", p[1])


def p_function_call(p):
    """function_call : identifier left_parenthesis argument right_parenthesis"""
    p[0] = NonTerminal("Function call", Terminal(p[1]), p[3])


def p_argument1(p):
    """argument : value"""
    # Parse a function call argument with a single value
    p[0] = NonTerminal("Function call argument", p[1])


def p_argument2(p):
    """argument : argument comma value"""
    # Parse a continuation of a function call argument list with another value separated by a comma
    p[0] = NonTerminal("Function call argument", p[1], p[3])


def p_argument3(p):
    """argument : empty"""
    # Parse a function call with no arguments
    p[0] = Null()


def p_statement5(p):
    """statement : return value"""
    # Parse a return statement with the keyword "return" followed by a value
    p[0] = NonTerminal("Return statement", Terminal(p[1]), p[2])


def p_statement6(p):
    """statement : break"""
    # Parse a break statement with the keyword "break"
    p[0] = NonTerminal("Break statement", Terminal(p[1]))


def p_empty(p):
    """empty :"""
    # Parse an empty production
    pass


def p_error(p):
    # Handle syntax errors during parsing
    messagebox.showerror('Compiler Error', 'Error:' + "Invalid syntax %s" % p)


global text
parser = yacc.yacc()


def restart_table():
    parser.LRTable = None


def main():
    global text

    input_text0 = ""
    fileWrite = open('graph.txt', 'w')
    fileWrite.write(input_text0)
    fileWrite.close()

    # Read content from the "input.py" file
    text = ""
    file = open("input.py", "r")
    content = file.read()
    file.close()

    # Create a parser and parse the content
    result = parser.parse(content, debug=0, tracking=True)
    text = (result.translate())

    # Save the translated program in the "graph.txt" file
    graphFile = open('graph.txt', 'w')
    graphFile.write(text)
    graphFile.close()

    del parser.statestack[:]
    del parser.symstack[:]
    semantic.count = 0
    semantic.txt = ""
    return text
