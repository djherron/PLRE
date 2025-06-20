#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This script demonstrates:
    1) the representation of an arbitrary propositional logic formula, in 
       CNF (conjunctive normal form), as an executable computational graph, 
    and
    2) the execution of the computational graph representing that formula 
       to determine its truth value, given an arbitrary interpretation (aka
       some truth-value assignment representing a possible world, or a 
       possible set of predictions from a neural network)
'''


#%% imports

import plre_core as pc


#%% specify a set of propositional symbols

#propSymbolSet = ['A', 'B', 'C']
#propSymbolSet = ['A', 'B', 'C', 'D']
propSymbolSet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


 #%% specify a propositional logic formula, in conjunctive normal form (CNF)

formula = '(A )  & C'

#formula = '(!A | !B) | (A) & C'
#formula = '(!A | !B) & C'
#formula = '(A | !B) & C'
#formula = '(A | B) & C'
#formula = 'A | B | C'
#formula = '!A | B | C & !B | !C & C | D'

#
# --- tested --- single clause formulae
#

#formula = 'A'
#formula = '( A )'
#formula = 'A | B | C'
#formula = '( A | B | C'      # fails with Exception
#formula = '( A | B | C )'
#formula = 'A | B | !C'

#
# --- tested --- multiple clauses, but all clauses are single-literal
#

#formula = 'A & B'
#formula = 'A & B & C'
#formula = 'A & !B & C'
#formula = '!A & !B & !C'
#formula = '( A & B & C'      # fails with Exception
#formula = '( A & B & C )'    # fails with Exception

#
# --- tested --- multiple clauses with complex clauses
#

#formula = 'A & ( B | C )'
#formula = '( A | B ) & ( C | D )'
#formula = '( A | B | !C ) & ( !B | C | !D )'
#formula = '( A | B | !C ) & ( !B | C | !D ) & ( !A | D )'

# this pair of test examples demonstrate that parentheses are optional;
# the parsing recognises the precedence of the logical AND in the CNF
# format and that operator, &, is sufficient to mark the start/end of 
# clauses; but users may prefer using parentheses to give clarity 
#formula = '( A | B ) & ( C | !D ) & ( E | F | G )'
#formula = 'A | B & C | !D & E | F | G'


#%% parse the propositional logic formula and build its computational graph

graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)


#%% display the computational graph in the console

pc.display_proplogic_graph(graph)


#%% specify an interpretation (a truth-value assignment or possible world)

#
# We define an interpretation implicitly rather than explicitly to make it
# easier for the user and faster for computation. The user needs to list 
# only those symbols that are assigned a truth value of TRUE. All other
# propositional symbols are automatically assigned a truth value of FALSE.
#
# Each interpretation is a truth-value assignment to all of the atomic 
# propositional symbols. Each interpretation represents a possible world.
#
# An empty list is supported. This interpretation assigns all propositional
# symbols a value of False.
#

#symbols_with_truthvalue_true = []
#symbols_with_truthvalue_true = ['A','C']
symbols_with_truthvalue_true = ['A', 'B']
#symbols_with_truthvalue_true = ['A','C', 'E']


print('The interpretation (possible world) for evaluating the formula')
print('assigns the following symbols a truth value of TRUE:')
print(symbols_with_truthvalue_true)


#%% validate the world (the interpretation) against the symbol set

# check that each symbol in the set of propositional symbols explicitly
# assigned a truth value of TRUE is a recognised (valid) symbol

for symbol in symbols_with_truthvalue_true:
    if symbol not in propSymbolSet:
        raise ValueError(f'symbol {symbol} not recognised')

print('Symbols with truth-values True are valid')


#%% execute the computational graph for the formula on the interpretation

print(f'formula: {formula}')
print()
print('graph:')
print()

# execute the graph
truthValue = pc.execute_proplogic_graph(graph, 
                                        symbols_with_truthvalue_true, 
                                        verbose=True)

# show the result
print()
print(f'formula truth value: {truthValue}')
















