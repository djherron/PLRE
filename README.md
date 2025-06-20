# PLRE

A propositional logic reasoning engine.

# Overview

The PLRE (propositional logic reasoning engine) is a Python package for determining the truth values of propositional logic formulae, given an assignment of truth values to the propositional symbols used in the formulae.

The propositional logic formulae are expressed in a text file in **conjunctive normal form** [CNF](https://en.wikipedia.org/wiki/Conjunctive_normal_form).

At instantiation, the engine consumes a list of propositional symbols and a text file containing propositional logic formulae (in CNF) expressed using subsets of the propositional symbols. Each formula is parsed and represented as an executable computational graph.

Given a truth-value assignment, an API function computes the truth values of each of the formulae and reports those that are NOT satisfied (i.e. for which the truth value computed was False).

The anticipated use case for the PLRE is in neurosymbolic AI systems that blend symbolic reasoning with subsymbolic learning.


# Conjunctive normal form (CNF)

A CNF formula is a conjunction


Every propositional logic formula can be expressed in CNF.  

**Example formulae in CNF using symbols A, B, C, D:**
A
A | B | !C
A & B & !C
(A | B) & (C | !D)
(A | B | !C) & (!D | E | F) & (G | !H)

# Syntax


operator | conventional symbol | PLRE symbol | notes
--- | --- | --- | --- |
logical NOT | $\lnot$ | ! | (exclamation mark)
logical OR  | $\lor$  | \| | (vertical bar)



