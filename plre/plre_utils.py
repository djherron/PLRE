"""
@author: David Herron
"""

'''
A module of utility functionality.
'''

#%%

from antlr4 import *
from plre.CNFLexer import CNFLexer
from plre.CNFParser import CNFParser
import re

#%%

def get_cnf_expressions_old(filepath):
    '''
    Extract CNF expressions from a text file.

    This function uses one or more blank lines to separate 
    CNF expressions.

    NOTE: this function does NOT permit comments in the input file.
    '''
    # read the entire contents into a single string
    with open(filepath, 'r') as fp:
        content = fp.read()
    
    # split the content (into distinct CNF expressions) on one or more 
    # blank lines
    blocks = re.split(r'\n\s*\n', content.strip())
    expressions = [block.strip() for block in blocks if block.strip()]

    return expressions

#%%

def get_cnf_expressions(filepath):
    '''
    Extract CNF expressions from a text file.

    This function uses one or more blank lines to separate 
    CNF expressions.
    
    This function also permits input text files to contain 
    comment lines --- those starting with '#'.
    These comment lines are filtered out before the CNF expressions 
    are extracted.  This feature permits PLRE users to document the
    propositional logic formulae they specify, in CNF, in PLRE input
    text files.
    '''
    # read the contents into a list of strings, one string per line
    with open(filepath, 'r') as fp:
        lines = fp.readlines()
    
    # remove comment lines; and, in the process, concatenate the strings
    # for the lines into one large string of content
    content = ''.join(line for line in lines if not line.startswith('#'))

    # split the content into distinct CNF expressions; split on one or 
    # more adjacent blank lines
    blocks = re.split(r'\n\s*\n', content.strip())
    expressions = [block.strip() for block in blocks if block.strip()]

    return expressions


#%%

def parse_cnf(expression_text):
    input_stream = InputStream(expression_text)
    lexer = CNFLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CNFParser(stream)
    tree = parser.cnf()
    if parser.getNumberOfSyntaxErrors() > 0:
        print(f'syntax errors: {parser.getNumberOfSyntaxErrors()}')
        return None, parser
    return tree, parser

