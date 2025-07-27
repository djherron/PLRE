#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This module implements a propositional logic reasoning engine (PLRE).

Functionality of the PLRE:
    0) accept list of propositional symbols at instantiation
    1) load propositional logic formulae from text file
    2) parse each formula and build its computational graph; keep the 
       order of the resulting collection of computational graphs
       synchronised with the text file formulae
    3) accept a truth assignment (aka an interpretation, or a 
       possible world)
    4) given a possible world, determine the truth-value of each 
       propositional logic formula by executing its computational graph
    5) track which formulae are satisfied (True) and which not (False)
    6) provide a list of formula Ids whose truth-value is False (ie 
       that are not satisfied by the possible world)
'''


#%%

from . import plre_core as pc


#%%

class PLRE():
    
    def __init__(self, propSymbolSet, formulaFileName):
        super(PLRE, self).__init__()
        
        # the set of propositional symbols referred to in the 
        # propositional logic formulae
        self.propSymbolSet = propSymbolSet
        
        # the name of a text file containing propositional logic formulae
        # expressed in Conjunctive Normal Form (CNF)
        self.formulaFileName = formulaFileName
        
        # a list in which to store formula computational graphs
        self.fcg_store = []
        
        # a list in which to store line numbers (as formula identifiers)
        self.fcg_lineNums = []
        
        # validate the set of propositional symbols
        self.validate_symbols()
        
        # load the propositional logic formulae from the text file and
        # represent them as computational graphs
        self.load_formulae()
        
        return None
    
    def validate_symbols(self):
        
        if len(self.propSymbolSet) == 0:
            raise ValueError('the set of propositional symbols must be non-empty')
        
        pss = set(self.propSymbolSet)
        if len(pss) < len(self.propSymbolSet):
            raise ValueError('the set of propositional symbols contains duplicates')
        
        for symbol in self.propSymbolSet:
            if not symbol.isidentifier():
                raise ValueError("propositional symbol names must be valid Python identifiers")
            if pc.LogicOps.logical_NOT in symbol:
                raise ValueError("propositional symbol names cannot use the logical NOT character")
            if pc.LogicOps.logical_AND in symbol:
                raise ValueError("propositional symbol names cannot use the logical AND character")           
            if pc.LogicOps.logical_OR in symbol:
                raise ValueError("propositional symbol names cannot use the logical OR character")
    
    def load_formulae(self):
        
        # load a text file containing propositional logic formulae
        with open(self.formulaFileName) as fp:
            formula_file_lines = fp.readlines()
        
        formula_index = 0
     
        # iterate over the lines of the text file
        for idx, line in enumerate(formula_file_lines):

            line = line.strip()
            line_num = idx + 1
        
            linetype = ''
            if len(line) == 0 or line == '':  # blank line
                linetype = 'blank'
            elif line[0] == '#':  # comment line
                linetype = 'comment'
            else:
                linetype = 'formula'
            
            # blank lines and comment lines are allowed in the formula file
            # to help the analyst organise the set of formulae; but these
            # lines require no processing and are ignored
            if not linetype == 'formula':
                continue
            
            # count the formula, to give each on an 'index' number identifier
            # reflecting its relative position in the text file of formulae
            formula_index += 1
            
            # parse the propositional logic formula and build its
            # computational graph
            fcg = pc.parse_formula_build_graph(line, 
                                               self.propSymbolSet,
                                               formula_index,
                                               line_num,
                                               verbose=False)
            
            # save the formula's computational graph in the store
            self.fcg_store.append(fcg)
            
            self.fcg_lineNums.append(line_num)
        
        
        print(f"Loaded formulae from file: '{self.formulaFileName}'")
        print()
        print(f'Number of formulae loaded: {len(self.fcg_lineNums)}')
        
        
    def compute_truth_values(self, symbols_with_truthvalue_true):
        '''
        Compute the truth values of the propositional logic formulae
        by executing their computational graphs, given a possible world.
        
        Parameters
        ----------
        symbols_with_truthvalue_true : List of Strings
            A list of propositional symbols asserted to have truth-value
            True, in a possible world (truth-value assignment). All other
            propositional symbols are given a truth-value of False.

        Returns
        -------
        results : Dictionary
            A dictionary identifying the propositional logic formulae
            whose truth value was computed to be False (ie that are NOT
            satisfied) by the world (truth-value assignment) implied by
            the list of symbols with truth-value True.
        '''
        
        # a list of indices of propositional logic formula whose truth
        # values are computed to be False, given the world implied by 
        # the set of symbols with truthvalues True
        formulae_not_satisfied = []
        
        #
        # iterate over the computational graphs of the propositional 
        # logic formulae and execute each one given the interpretation
        # (aka truth-value assignment, or possible world) implied by the
        # list of symbols with truth-value True
        #
        
        for idx, graph in enumerate(self.fcg_store):
            
            tval = pc.execute_proplogic_graph(graph, 
                                              symbols_with_truthvalue_true, 
                                              verbose=False)
            
            if tval == False:
                formulae_not_satisfied.append(idx)
        
        #
        # prepare return package
        #
        
        results = {'indices': [], 'lineNums': [], 'formulae': []}
        
        for idx in formulae_not_satisfied:
            graph = self.fcg_store[idx]
            results['formulae'].append(graph.formula)
            results['indices'].append(graph.formula_index)
            results['lineNums'].append(graph.formula_lineNum)

        return results
        

    def display_formula_graph_by_index(self, formula_index):
           
        graph = None
        for fcg in self.fcg_store:
            if fcg.formula_index == formula_index:
                graph = fcg
        
        if graph == None:
            raise ValueError('Formula index not recognised')
        
        pc.display_proplogic_graph(graph)


#%%















