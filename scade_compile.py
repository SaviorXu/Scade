from ply.yacc import yacc
from scade_lex import scade_lex,get_tokens,tokens,lex_value
from SymbolClass import *

scade_lexr=scade_lex()

def p_program(p):
    'Program : Decls_zero_or_mode'
    p[0]=p[1]

def p_decls_zero_or_mode(p):
    '''Decls_zero_or_mode : Decls Decls_zero_or_mode
    | empty'''
    p[0]=p[1]+p[2]

def p_decls(p):
    '''Decls : Const_block'''
    p[0]=p[1]

def p_const_block(p):
    '''Const_block : CONST Const_decl SEMICOLON Const_block
    | empty'''
    pass

def p_const_decl(p):
    '''Const_decl : Interface_status id COLON Type_expr EQU Expr
    | Interface_status id COLON Type_expr'''
    # if len(p)==7:
    #     symbol=Symbol(p[2].values,'Const',p[4].type)
    pass


def p_interface_status(p):
    '''Interface_status : Visibility_zero_or_one External
    | Visibility_zero_or_one'''
    p[0]=lex_value('Interface_status')
    if len(p)==3:
        p[0].objects.extend(p[1])
        p[0].objects.extend(p[2])
    elif len(p)==2:
        p[0].objects.extend(p[1])

def p_visibility_zero_or_one(p):
    '''Visibility_zero_or_one : Visibility
    | empty'''
    p[0]=p[1]

def p_external(p):
    'External : IMPORTED'
    p[0]=lex_value('External')
    p[0].value=p[1].value

def p_visibility(p):
    '''Visibility : PRIVATE
    | PUBLIC'''
    p[0]=lex_value('Visibility')
    p[0].value=p[1].value

#not finish
def p_type_expr(p):
    '''Type_expr : BOOL
    | INT32
    | INT8'''
    p[0]=lex_value('Type_expr')
    p[0].value=p[1].value

#not finish
def p_expr(p):
    '''Expr : Atom'''
    p[0]=p[1]

#not finish
def p_atom(p):
    '''Atom : Bool_atom
    | INTEGERNUM'''
    p[0]=p[1]

def p_bool_atom(p):
    '''Bool_atom : TRUE
    | FALSE'''
    p[0]=p[1]

# def p_opt_body(p):
#     'Opt_body : Simple_Equation'
#     p[0]=lex_value('Opt_body')
#     p[0]=p[1]
#     print(p[0].value)



# def p_simple_equation(p):
#     'Simple_Equation : Lhs EQU Expr SEMICOLON'
#     p[0]=lex_value('Simple_Equation')
#     p[0].value=p[1].value+"="+p[3].value+";"


# def p_lhs(p):
#     'Lhs : LV6ID'
#     p[0]=p[1]
#
# def p_expr(p):
#     '''Expr : Arith_expr
#           | Atom
#           | Id_expr'''
#     p[0] = lex_value('Expr')
#     p[0].value=p[1].value
#
# def p_arith_expr(p):
#     '''Arith_expr : Unary_arith_op Expr
#     | Expr Bin_arith_op Expr'''
#     p[0]=lex_value('Arith_expr')
#     if len(p)==3:
#         p[0].value=p[1].value+str(p[2].value)
#     else:
#         p[0].value=p[1].value+p[2].value+str(p[3].value)
#
# def p_unary_arith_op(p):
#     '''Unary_arith_op : MINUS
#     | PLUS
#     | LNOT'''
#     p[0]=p[1]
#
# def p_bin_arith_op(p):
#     '''Bin_arith_op : PLUS
#     | MINUS
#     | '''
#     p[0]=p[1]
#
# def p_atom(p):
#     'Atom : INTCONST'
#     p[0]=lex_value('Atom')
#     p[0].value=p[1].value
#
# def p_id_expr(p):
#     '''Id_expr : LV6ID
#     | empty '''
#     p[0]=p[1]

def p_error(p):
    print("Syntax error in input!")

def p_empty(p):
    'empty : '
    p[0]=lex_value('Empty')

if __name__=='__main__':
    parser=yacc(debug=1)
    strs=str("const e:bool=true;")
    string_tokens=get_tokens(strs)
    # print(string_tokens)
    scade_lexr.set_tokens(string_tokens)
    nodes=parser.parse(strs,lexer=scade_lexr)
    # print(nodes)


