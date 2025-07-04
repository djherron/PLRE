#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This module defines classes and functions that represent the core
of the Propositional Logic Reasoning Engine (PLRE).

The PLRE represents propositional logic formulae as computational
graphs. 

Given a truth-value assignment (aka an interpretation, or a possible 
world), the PLRE determines the truth-values of propositional logic
formulae by executing their computational graphs.

Source:
    Our computational graph solution borrows and adapts from here:
    https://homepages.inf.ed.ac.uk/htang2/mlg2022/tutorial-3.pdf,
    INFR10086 Machine Learning, 2022/23
    Tutorial 4: Computation Graphs
'''

#%%

class GraphNode:
    '''
    A class for nodes in computational graphs designed for representing
    propositional logic formulae.
    '''

    def __init__(self, type, id, *dependencies):

        self.id = id 
        self.type = type
        self.dependencies = [] 
        self.dependencies.extend(dependencies) 
        self.propSymbol = None
        self.value = None


#%%

class Graph_PropLogicFormulaCNF:
    '''
    A class for computational graphs designed for representing
    propositional logic formulae.
    
    This graph class assumes propositional logic formulae are always in
    Conjunctive Normal Form (CNF).
    Any propositional formula can be converted to CNF. 
    In CNF, a formula is expressed as a conjunction (AND) of one or more 
    clauses, and each clause is a disjunction (OR) of one or more literals.
    A literal is a propositional symbol that may or may not be negated.
    
    Examples of propositional symbols:
        A, B, C, D
    
    Examples of literals: 
        A, !A, B, !B, C, !C, D, !D
    
    Examples of clauses (disjunctions of literals):
        A
        !A
        A | B
        A | !B
        A | B | !C
    
    Examples of conjunctions of clauses:
        ( A | B ) & C
        ( A | B ) & !C
        ( A | B ) & ( C | !D )
        ( A | B ) & C & !D
        A & B & C
        A & !B & !C 
    '''

    def __init__(self, formula, formula_index=0, formula_lineNum=0):
        
        # a list of the nodes in the graph, stored in topological order so
        # that the graph can be executed by processing the list of nodes
        # sequentially, from start to end
        self.nodes = []
        
        # string; the propositional logic formula to which the 
        # computational graph corresponds
        self.formula = formula
        
        # the index number (relative position) of the formula within a
        # text file of formula
        self.formula_index = formula_index
        
        # the line number in a text file containing the formula
        # represented by the computational graph; this line number acts as
        # a form of 'external Id' for referring to the formula in messages
        self.formula_lineNum = formula_lineNum

    def propSymbol(self, propSymbol):
        '''
        Create a node for a propositional symbol and add it to the graph.
        
        A propositional symbol has no dependencies. Hence all 
        propositional symbols are leaf nodes of a computational graph.
        '''

        gn = GraphNode('propSymbol', len(self.nodes))
        gn.propSymbol = propSymbol
        self.nodes.append(gn) 
        return gn

    def logicalOR(self, gn1, gn2):
        '''
        Create a node for a logical OR operator and add it to the graph.
        
        A logical OR operator is a binary operator. Hence it has two 
        dependencies, both of which must be graph nodes of some type.
        '''

        gn = GraphNode('logical_OR', len(self.nodes), gn1, gn2)
        self.nodes.append(gn) 
        return gn
    
    def logicalNOT(self, gn1):
        '''
        Create a node for a logical NOT operator and add it to the graph.
        
        A logical NOT operator is a unary operator. Hence it has one 
        dependency, which must be a graph node for a propositional symbol.
        
        Note: We assume propositional logic formula in CNF (conjunctive
        normal form) only. Thus, logical NOT operators can only appear in
        relation to individual propositional symbols, not to parenthesised
        clauses of any kind, whether disjunctive or conjunctive.
        Note: If we want to generalise our solution and accept formula not
        in CNF, then we'd need to relax this restriction and permit logical
        NOT operators to appear in front of left brackets, '('.
        '''
        
        gn = GraphNode('logical_NOT', len(self.nodes), gn1)
        self.nodes.append(gn) 
        return gn 

    def logicalAND(self, gn1, gn2):
        '''
        Create a node for a logical AND operator and add it to the graph.
        
        A logical AND operator is a binary operator. Hence it has two 
        dependencies, both of which must be graph nodes of some type.
        '''
        
        gn = GraphNode('logical_AND', len(self.nodes), gn1, gn2)
        self.nodes.append(gn) 
        return gn


#%% 

def throw_exception(formula, formula_lineNum, clause_num, message):
    
    print()
    print('Formula parsing problem')
    print()
    print(f'formula   : {formula}')
    print(f'line num  : {formula_lineNum}')
    print(f'clause num: {clause_num}')
    print(f'problem   : {message}')
    print()
    raise ValueError(message)
    

#%% a function to parse a propositional logic formula in CNF

def parse_formula_build_graph(formula, propSymbolSet,
                              formula_index=0,
                              formula_lineNum=0, verbose=False):
    '''
    Parse a propositional logic formula, in CNF (conjunctive normal
    form), and build its computational graph.

    Parameters
    ----------
    formula : string
        A propositional logic formula in CNF (conjunctive normal form).
    propSymbolSet : list of strings
        A list of string tokens representing the set (universe) of 
        propositional symbols that can appear in propositional logic formulae.
    formula_index : integer (non-negative)
        An integer indicating the index number (ie relative position) of the
        formula within a text file of formulae.
    formula_lineNum : integer (non-negative)
        An integer indicating the line number of a text file to which the
        formula corresponds.
    verbose : Boolean
        A logical flag controlling the verbosity of the execution.

    Returns
    -------
    g : Graph_PropLogicFormulaCNF
        The propositional logic formula represented as an executable
        computational graph.
    
    Discussion
    ----------
    Our propositional logic formulae, in CNF, are composed of up to 5 
    token types:
        1) literal (a propositional symbol that may or may not be negated
           using the logical NOT operator, '!', and which may or may not
           be prefixed or suffixed by a left or right parenthesis)
        2) logical OR operator '|'
        3) logical AND operator '&'
        4) left parenthesis '('
        5) right parenthesis ')'

    '''

    left_bracket_open = False
    operator_OR_active = False
    operator_AND_active = False
    graph_top_node = None
    clause_top_node = None
    clause_literal_obtained = False
    clause_component_last = None
    clause_component_current = None
    clause_num = 1
    
    if verbose:
        print()
        print(f'formula: {formula}')
        print(f'index  : {formula_index}')
        print(f'linenum: {formula_lineNum}')

    # instantiate a computational graph for the formula
    g = Graph_PropLogicFormulaCNF(formula, formula_index, formula_lineNum)

    # split the string containing the formula into tokens, using blank 
    # space as the delimiter
    tokens = formula.split()
    
    # iterate over the tokens of the formula
    for token in tokens:
        
        if verbose:
            print(f'token: {token}')
        
        propSymbol = None
        
        if token == '|':  # logical OR
        
            if not clause_literal_obtained:
                msg = 'clause must begin with a literal'
                throw_exception(formula, formula_lineNum, clause_num, msg)
        
            operator_OR_active = True
            
            clause_component_current = 'operator'
            
        elif token == '&':  # logical AND

            if operator_OR_active:
                msg = 'clause ill-formed'
                throw_exception(formula, formula_lineNum, clause_num, msg)

            if left_bracket_open:
                msg = 'clause needs a closing parenthesis'
                throw_exception(formula, formula_lineNum, clause_num, msg)
        
            # the AND operator marks the end of a CNF clause, so we do
            # end-of-clause processing for the current clause, and set up
            # for a new clause
            if operator_AND_active:
                # add a node for the *previous* logical_AND to the graph,
                # ANDing whatever came before the current clause with the
                # current clause; save the node for the *previous* logical_AND
                # as the new top node of the graph (so far); then we'll be
                # ready to process a new clause
                graph_top_node = g.logicalAND(graph_top_node, clause_top_node)
            else:
                # we have encountered the first logical_AND of the formula;
                # save the top node of the current clause as the top node of
                # the graph (so far)
                graph_top_node = clause_top_node
                clause_top_node = None
                operator_AND_active = True
            
            # prepare for a new clause
            clause_literal_obtained = False
            clause_component_current = None
            clause_component_last = None
            clause_num += 1
                
        elif token == '(':
            
            if clause_literal_obtained:
                msg = 'left parenthesis misplaced'
                throw_exception(formula, formula_lineNum, clause_num, msg)
            
            if left_bracket_open:
                msg = 'two open left parentheses not valid in CNF'
                throw_exception(formula, formula_lineNum, clause_num, msg)
            else:
                left_bracket_open = True
                
        elif token == ')':
            
            if left_bracket_open:
                left_bracket_open = False
            else:
                msg = 'singleton right parenthesis not allowed'
                throw_exception(formula, formula_lineNum, clause_num, msg)
                
        else:  # a literal
            
            literal = token
        
            if literal.startswith('('):
                if clause_literal_obtained:
                    msg = 'left parenthesis misplaced'
                    throw_exception(formula, formula_lineNum, clause_num, msg)
                if left_bracket_open:
                    msg = 'two open left parentheses not valid in CNF'
                    throw_exception(formula, formula_lineNum, clause_num, msg)
                else:
                    left_bracket_open = True
                literal = token[1:]
            
            if literal.startswith('!'):   # negated literal
                literal = literal[1:]
                if len(literal) == 0:
                    msg = 'singleton ! operator not allowed'
                    throw_exception(formula, formula_lineNum, clause_num, msg)
                negatedPropSymbol = True
            else:
                negatedPropSymbol = False
            
            propSymbol = literal
            if literal.endswith(')'):
                if left_bracket_open:
                    left_bracket_open = False
                else:
                    msg = 'singleton right parenthesis not allowed'
                    throw_exception(formula, formula_lineNum, clause_num, msg)                
                propSymbol = literal[:-1]
            
            if propSymbol not in propSymbolSet:
                msg = f'propSymbol {propSymbol} not recognised'
                throw_exception(formula, formula_lineNum, clause_num, msg)
            
            clause_literal_obtained = True
            
            # create node for propositional symbol and add to graph
            gn = g.propSymbol(propSymbol)
            
            if negatedPropSymbol:
                # create node for logical NOT operator and add to graph, 
                # with the propositional symbol as its dependency
                gn = g.logicalNOT(gn)           
            
            if operator_OR_active:
                clause_top_node = g.logicalOR(clause_top_node, gn)
                operator_OR_active = False
            else:
                clause_top_node = gn
            
            clause_component_current = 'literal'
        
        #
        # per CNF, ensure that within a clause we always have an 
        # alternating sequence of literals and logical_OR operators
        #
        
        if verbose:
            print(f'clause component last: {clause_component_last}')
            print(f'clause component cur : {clause_component_current}')
        
        # TODO: verify we're handling parentheses OK; re-test everything
        
        if token in ['(', ')']:
            pass
        else:
            if clause_component_last == None:
                if clause_component_current == 'operator':
                    msg = 'clause must begin with a literal'
                    throw_exception(formula, formula_lineNum, clause_num, msg)
            elif clause_component_last == 'operator':
                if clause_component_current == 'literal':
                    pass
                else:
                    msg = 'operator must be followed by a literal'
                    throw_exception(formula, formula_lineNum, clause_num, msg)
            elif clause_component_last == 'literal':
                if clause_component_current == 'operator':
                    pass
                else:
                    msg = 'only an operator can follow a literal'
                    throw_exception(formula, formula_lineNum, clause_num, msg)
            else:
                raise ValueError('internal problem: clause_component_last')
            
            clause_component_last = clause_component_current 

    
    if left_bracket_open:
        raise ValueError('formula needs a closing parenthesis')
    
    if operator_OR_active:
        raise ValueError(f'clause {clause_num} ill-formed')
    
    if operator_AND_active:
        # add a node for the last active logical_AND operator to the graph,
        # and thereby connect (AND) the last clause of the formula with
        # the graph containing all the other clauses of the formula
        _ = g.logicalAND(graph_top_node, clause_top_node)

    return g 


#%% a function for displaying a computational graph

def display_proplogic_graph(graph):
    
    print(f'formula: {graph.formula}')
    print(f'index  : {graph.formula_index}')
    print(f'linenum: {graph.formula_lineNum}')
    print()
    print('graph:')
    print()
    
    print('id | node type   | symbol | value | dependencies')
    print()
    
    for gnode in graph.nodes:
        nodeId = str(gnode.id).zfill(2)
        deps = []
        if len(gnode.dependencies) == 0:
            pass
        elif len(gnode.dependencies) == 1:
            nId = str(gnode.dependencies[0].id).zfill(2)
            deps.append(nId)
        elif len(gnode.dependencies) == 2:
            nId = str(gnode.dependencies[0].id).zfill(2)
            deps.append(nId)
            nId = str(gnode.dependencies[1].id).zfill(2)
            deps.append(nId)
        else:
            raise ValueError('Node has unexpected number of dependencies')
        if gnode.propSymbol == None:
            propSymbol = ''
        else:
            propSymbol = gnode.propSymbol
        if gnode.value == None:
            value = 'None'
        else:
            value = str(gnode.value)
        print(nodeId, '|', gnode.type.ljust(11), '|', propSymbol.ljust(6), '|', value.ljust(5), '|', deps)
    
    print()
    print(f'formula truth value: {graph.nodes[-1].value}')
    
    return None


#%% a function for executing a computational graph

def execute_proplogic_graph(graph, symbols_with_truthvalue_true, verbose):
    '''
    Execute a computational graph that represents a propositional logic
    formula, given an interpretation (a truth-value assignment 
    representing one possible world).
    
    Parameters
    ----------
    graph : Graph_PropLogicFormulaCNF
        A computational graph of a propositional logic formula in CNF.
    symbols_with_truthvalue_true : list of strings
        A list of propositional symbols assigned truthvalue True in an
        interpretation (possible world) with respect to which the 
        computational graph is to be executed to determine its truth value.
    verbose : Boolean
        A boolean flag indicating whether or not to be verbose when
        executing the computational graph.

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    truthValue : Boolean
        The Boolean truth value (True or False) of the propositional logic
        formula, given the interpretation (possible world).
    '''
    

    if verbose:
        print('id | node type   | symbol | value | dependencies')
        print()

    for gnode in graph.nodes:
        
        if gnode.type == 'propSymbol':

            if gnode.propSymbol in symbols_with_truthvalue_true:
                truthValue = True
            else:
                truthValue = False
            gnode.value = truthValue
        
        elif gnode.type == 'logical_OR':

            gnode.value = gnode.dependencies[0].value or \
                          gnode.dependencies[1].value 
            
        elif gnode.type == 'logical_NOT':

            gnode.value = not gnode.dependencies[0].value

        elif gnode.type == 'logical_AND':

            gnode.value = gnode.dependencies[0].value and \
                          gnode.dependencies[1].value 
        
        else:

            print(f'node type not recognised: {gnode.type}')

        if verbose:
            nodeId = str(gnode.id).zfill(2)
            deps = []
            if len(gnode.dependencies) == 0:
                pass
            elif len(gnode.dependencies) == 1:
                nId = str(gnode.dependencies[0].id).zfill(2)
                deps.append(nId)
            elif len(gnode.dependencies) == 2:
                nId = str(gnode.dependencies[0].id).zfill(2)
                deps.append(nId)
                nId = str(gnode.dependencies[1].id).zfill(2)
                deps.append(nId)
            else:
                raise ValueError('Node as unexpected number of dependencies')
            if gnode.propSymbol == None:
                propSymbol = ''
            else:
                propSymbol = gnode.propSymbol
            if gnode.value == None:
                value = 'None'
            else:
                value = str(gnode.value)
            print(nodeId, '|', gnode.type.ljust(11), '|', propSymbol.ljust(6), '|', value.ljust(5), '|', deps)

    # get the truth value of the propositional logic formula from the
    # value of the last (top-level) node in the computational graph
    truthValue = graph.nodes[-1].value

    return truthValue


#%%




