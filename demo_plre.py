#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This script demonstrates the propositional logic reasoning engine (PLRE).

It demonstrates use of the PLRE via its API, and it showcases its
functionality.
'''

#%%

from plre import PLRE


#%%

# specify the set of propositional symbols used in the propositional
# logic formulae about to be loaded
propSymbolSet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# specify a text file containing propositional logic formula expressed in
# Conjunctive Normal Form (CNF) and referencing symbols in the symbol set
formulaFileName = 'plre_formula.txt'

# instantiate a PLRE object
plre = PLRE(propSymbolSet, formulaFileName)


#%% specify a possible world (a truth-value assignment)

# list the propositional symbols that are assigned value True in this world
symbols_with_truthvalue_true = ['A', 'C', 'D']

# validate the world symbols against the symbol set
for symbol in symbols_with_truthvalue_true:
    if symbol not in propSymbolSet:
        raise ValueError(f'symbol {symbol} not recognised')


#%% compute the truth values of all propositional logic formulae

res = plre.compute_truth_values(symbols_with_truthvalue_true)

print('The specified world assigns True to symbols')
print(f'{symbols_with_truthvalue_true}')
print('and False to all other symbols.')
print()
print(f"Number of formulae not satisfied: {len(res['indices'])}")
print()

for idx, formula in enumerate(res['formulae']):
    print(f"Index  : {res['indices'][idx]}")
    print(f"Line   : {res['lineNums'][idx]}")
    print(f"Formula: {formula}")
    print()
    

#%% display a formula's computational graph

index = 23

plre.display_formula_graph_by_index(index)



