#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
A pytest test module.

This test module defines tests for propositional logic formulae in CNF
(conjunctive normal form) format.

The tests in this module are for formulae involving a single CNF clause.
'''


#%%

# nb: this module assumes the `plre` package has been installed!

import plre.plre_core as pc
from plre.plre_core import Graph_PropLogicFormulaCNF

import pytest


#%%

# TODO: work out how to share one definition of a propSymbolSet across test files

propSymbolSet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


#%%

class Test_SingleClauseFormulae_PositiveExamples:

    def test_formula_01(self):
        formula = 'A'
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_02(self):
        formula = '(A)' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_03(self):
        formula = '( A )' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)
    
    def test_formula_04(self):
        formula = '(A )' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)
    
    def test_formula_05(self):
        formula = '( A)' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_06(self):
        formula = 'A | B' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_07(self):
        formula = '(A | B)' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_08(self):
        formula = '( A | B )' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_09(self):
        formula = '(A | B )' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)
    
    def test_formula_10(self):
        formula = '( A | B)' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_11(self):
        formula = 'A | B | C' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_12(self):
        formula = '(A | B | C)' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_13(self):
        formula = '( A | B | C )' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_14(self):
        formula = '(A | B | C )' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_15(self):
        formula = '( A | B | C)' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_16(self):
        formula = '!A' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_17(self):
        formula = '(!A)' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_18(self):
        formula = '( !A )' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_19(self):
        formula = '(!A )' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_20(self):
        formula = '( !A)' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_21(self):
        formula = '!A | B' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_22(self):
        formula = 'A | !B' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_23(self):
        formula = '!A | !B' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_24(self):
        formula = '(!A | !B)' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_25(self):
        formula = '( !A | !B )' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_26(self):
        formula = 'A | !B | C | !D' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_27(self):
        formula = '(A | !B | C | !D)' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_28(self):
        formula = '!A | B | !C | D' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_29(self):
        formula = '(!A | B | !C | D)' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)

    def test_formula_30(self):
        formula = '!A | B | !C | D | !E' 
        graph = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)
        assert isinstance(graph, Graph_PropLogicFormulaCNF)


#%%

class Test_SingleClauseFormulae_NegativeExamples:
    '''
    A class of test methods devoted to verifying that syntactically invalid 
    CNF formulae are correctly detected as being syntactically invalid.
    '''

    def test_formula_01(self):
        formula = 'XxxX' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_02(self):
        formula = '(' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_03(self):
        formula = ')' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_04(self):
        formula = '()' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_05(self):
        formula = pc.LogicOps.logical_OR
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_06(self):
        formula = pc.LogicOps.logical_AND
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_07(self):
        formula = pc.LogicOps.logical_NOT
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_08(self):
        formula = 'A)' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_09(self):
        formula = '(A' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_10(self):
        formula = 'A (' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_11(self):
        formula = 'A )' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_12(self):
        formula = 'A | |' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_13(self):
        formula = 'A | &' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_14(self):
        formula = 'A | (' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_15(self):
        formula = 'A | )' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_16(self):
        formula = '(!A | !B) | C' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_17(self):
        formula = '(!A | !B) | (C)' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_18(self):
        formula = '(!A | B | !C) | D' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_19(self):
        formula = 'A | ! B' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)

    def test_formula_20(self):
        formula = 'A | !&' 
        with pytest.raises(ValueError):
            _ = pc.parse_formula_build_graph(formula, propSymbolSet, verbose=False)







