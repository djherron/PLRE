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

# Specify whether you have installed the PLRE in your
# Python environment. If you have not done so, don't
# worry, we handle that case.
use_installed_package = False


#%%

# NOTE:
# If the PLRE is not installed, the code block below appends the parent
# directory of the 'plre' package (folder) to sys.path so that the 'plre'
# can be found when the import statements are processed. But the solution
# only works if 'pytest' is invoked at the command line from within the 
# 'test' directory.
#
# Example:
# $ cd test
# $ pytest

import os
import sys

if use_installed_package:
    pass
else: 
    plre_parent_dir = os.path.abspath('..')
    if not os.path.exists(plre_parent_dir):
        print('Error obtaining PLRE parent directory')
    sys.path.append(plre_parent_dir)

import plre.plre_utils as pu

import pytest



#%%

propSymbolSet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


#%%

class Test_MultipleClauseFormulae_MultipleLiterals_PositiveExamples:

    def test_formula_01(self):
        formula = 'A & (B | C)'
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() == 0

    def test_formula_02(self):
        formula = '(A) & (B | C)' 
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() == 0

    def test_formula_03(self):
        formula = '(A | B) & C'
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() == 0

    def test_formula_04(self):
        formula = '(A | B) & (C)'
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() == 0

    def test_formula_05(self):
        formula = '(A | B) & (C | D)'
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() == 0

    def test_formula_06(self):
        formula = '(!A | B) & (!C | D)'
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() == 0

    def test_formula_07(self):
        formula = '(A | !B) & (C | !D)'
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() == 0

    def test_formula_08(self):
        formula = '(A | B | C) & (D | E) & (F | G)'
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() == 0

    def test_formula_09(self):
        formula = '(A | !B | C) & (D | !E) & (!F | G)'
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() == 0

    def test_formula_10(self):
        formula = '(!A | B | !C) & (!D | E) & (F | !G)'
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() == 0

    def test_formula_11(self):
        formula = '(!A | B | !C) & D & (E | F | !G)'
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() == 0

    def test_formula_12(self):
        formula = '(!A | B | !C) & !D & (E | !F | G)'
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() == 0


#%%

class Test_MultipleClauseFormulae_MultipleLiterals_NegativeExamples:
    '''
    A class of test methods devoted to verifying that syntactically invalid 
    CNF formulae are correctly detected as being syntactically invalid.
    '''

    def test_formula_01(self):
        formula = '(A & B | C)' 
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() > 0

    def test_formula_02(self):
        formula = '(A & B) | C' 
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() > 0

    def test_formula_03(self):
        formula = '(A|B) & (C D)' 
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() > 0

    def test_formula_04(self):
        formula = '(!A | B) | (C | !D)' 
        _, parser = pu.parse_cnf(formula)
        assert parser.getNumberOfSyntaxErrors() > 0








