# PLRE

A propositional logic reasoning engine.

# Overview

The PLRE (propositional logic reasoning engine) is a Python package for determining the truth values of propositional logic formulae, given an assignment of truth values to the propositional symbols used in the formulae.

The propositional logic formulae are expressed in a text file in **conjunctive normal form** [CNF](https://en.wikipedia.org/wiki/Conjunctive_normal_form).

At instantiation, the engine consumes a list of propositional symbols and a text file containing propositional logic formulae (in CNF) expressed using subsets of the propositional symbols. Each formula is parsed and represented as an executable computational graph.

Given a truth-value assignment, an API function computes the truth values of each of the formulae and reports those that are NOT satisfied (i.e. for which the truth value computed was False).

Other API functions provide ancillary services, like displaying the computational graph of a formula.

The anticipated use case for the PLRE is in neurosymbolic AI systems that blend symbolic reasoning with subsymbolic learning.


# Syntax for logical operators

The PLRE uses a special syntax to make it easy to express logical operators in CNF formulae in text files.

logical operator | conventional symbol | PLRE symbol | notes
--- | --- | --- | --- |
logical NOT | $\lnot$ | ! | (exclamation mark)
logical OR  | $\lor$  | \| | (vertical bar)
logical AND | $\land$ | & | (ampersand)


# Conjunctive normal form (CNF)

Per [Wikipedia](https://en.wikipedia.org/wiki/Conjunctive_normal_form), a CNF formula is a **conjunction** of one or more **clauses**, where each **clause** is a **disjunction** of one or more **literals**, and where a **literal** is a propositional symbol that may or may not be **negated**. Every propositional logic formula can be expressed in CNF. 

Consider the set of propositional symbols: `{A, B, C, D, E, F, G, H}`

**Example formulae in CNF with a single clause**

`A`

`!A`

`A | B | !C`

**Example formulae in CNF with a multiple clauses**

`A & B & !C`

`(A | B) & (C | !D)`

`(A | B | !C) & (!D | E | F) & (G | !H)`






