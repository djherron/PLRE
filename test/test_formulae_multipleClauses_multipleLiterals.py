#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
A pytest test module.

This test module defines tests for propositional logic formulae in CNF
(conjunctive normal form) format.

The tests in this module are for formulae involving multiple CNF clauses,
but where each clause may involve multiple literals.
'''


#%%

# nb: this module assumes the `plre` package has been installed!

import plre.plre_core as pc
from plre.plre_core import Graph_PropLogicFormulaCNF

import pytest


#%%

# TODO: work out how to share one definition of a propSymbolSet across test files

propSymbolSet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

#formula = 'A & (B | C)'
#formula = '( A | B ) & ( C | D )'
#formula = '( A | B | !C ) & ( !B | C | !D )'
#formula = '( A | B | !C ) & ( !B | C | !D ) & ( !A | D )'


#%%

class Test_SingleClauseFormulae_PositiveExamples:

    def test_formula_01(self):
        formula = 'A & (B | C)'
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_02(self):
        formula = '(A) & (B | C)' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_03(self):
        formula = '( A ) & ( B | C )' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)
    
    def test_formula_04(self):
        formula = '(A | B) & C'
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_05(self):
        formula = '(A | B) & (C)'
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_06(self):
        formula = '(A | B) & (C | D)'
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_07(self):
        formula = '( A | B ) & ( C | D )'
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_08(self):   
        formula = 'A | B & C | D'  # not recommended as interpretation can be confusing
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_09(self):
        formula = '(!A | B) & (!C | D)'
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_10(self):
        formula = '(A | !B) & (C | !D)'
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_11(self):
        formula = '(A | B | C) & (D | E) & (F | G)'
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_12(self):
        formula = '(A | !B | C) & (D | !E) & (!F | G)'
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_13(self):
        formula = '(!A | B | !C) & (!D | E) & (F | !G)'
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_14(self):
        formula = '(!A | B | !C) & D & (E | F | !G)'
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_15(self):
        formula = '(!A | B | !C) & !D & (E | !F | G)'
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)


#%%

class Test_SingleClauseFormulae_NegativeExamples:
    '''
    A class of test methods devoted to verifying that syntactically invalid 
    CNF formulae are correctly detected as being syntactically invalid.
    '''

    def test_formula_01(self):
        formula = '(A & B | C)' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_02(self):
        formula = '(A & B) | C' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_03(self):
        formula = '(A & B) | C' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_04(self):
        formula = '(A|B) & (C|D)' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_05(self):
        formula = '(!A |B) & (C| !D)' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)








