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

use_installed_package = True

if use_installed_package:
    pass
else: 
    import os, sys
    DEMO_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_DIR = os.path.abspath(os.path.join(DEMO_DIR, '..'))
    sys.path.insert(0, PROJECT_DIR)


#%%

from plre.plre import PLRE


#%%

# specify the set of propositional symbols used in the propositional
# logic formulae about to be loaded
propSymbolSet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# specify a text file containing propositional logic formula expressed in
# Conjunctive Normal Form (CNF) and referencing symbols in the symbol set
formulaFileName = 'demo_formulae.txt'

# instantiate a PLRE object
plre = PLRE(propSymbolSet, formulaFileName)


#%% display the formulae

print('index | linenum | formula')
print()
for fcg in plre.fcg_store:
    index = str(fcg.formula_index).zfill(2)
    print(f'{index} | {fcg.formula_lineNum} | {fcg.formula}')


#%% display a formula's computational graph BEFORE execution

index = 24

plre.display_formula_graph_by_index(index)


#%% specify a possible world (a truth-value assignment)

# list the propositional symbols that are assigned value True in this world
symbols_with_truthvalue_true = ['A', 'C', 'D']

# validate the world symbols against the symbol set
for symbol in symbols_with_truthvalue_true:
    if symbol not in propSymbolSet:
        raise ValueError(f'symbol {symbol} not recognised')

print(f'Symbols assigned value True: {symbols_with_truthvalue_true}')


#%% compute the truth values of all propositional logic formulae

res = plre.compute_truth_values(symbols_with_truthvalue_true)

print(f'Number of formulae: {len(plre.fcg_store)}')
print()
print('The truth-value assignment (possible world) assigns True to symbols')
print(f'{symbols_with_truthvalue_true}')
print('and False to all other symbols.')
print()
print(f"Number of formulae NOT satisfied by this world: {len(res['indices'])}")


#%% display the formulae not satisfied by the specified world

print('The formulae NOT satisfied by the current world:')
print()
print('index | linenum | formula')
print()
for idx, formula in enumerate(res['formulae']):
    index = str(res['indices'][idx]).zfill(2)
    linenum = str(res['lineNums'][idx]).zfill(2)
    print(f'{index} | {linenum} | {formula}')
    #print(f"formula: {formula}")
    #print(f"index  : {res['indices'][idx]}")
    #print(f"linenum: {res['lineNums'][idx]}")
    print()
    

#%% display a formula's computational graph AFTER execution

index = 24

plre.display_formula_graph_by_index(index)



