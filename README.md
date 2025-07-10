# PLRE

A propositional logic reasoning engine, or propositional model checker.

# Overview

The PLRE (propositional logic reasoning engine) is a pure Python tool (package) for determining the truth values of propositional logic formulae, given a truth-value assignment (an assignment of truth values to the signature of, i.e. to the propositional symbols used in, the formulae).

The PLRE contributes to the field of **automated reasoning**, in particular to the **model checking** dimension of its subfield **automated theorem proving**. Per [Wikipedia](https://en.wikipedia.org/wiki/Model_checking), **model checking** problems are formulated as logic tasks that involve checking ``whether a structure satisfies a given logical formula''. The article then gives this example:
> **A simple model-checking problem consists of verifying whether a formula in the propositional logic is satisfied by a given structure.**

This is precisely what the PLRE does. So the PLRE can also be described as being a **propositional model checker**.  In the case of propositional logic, a ``structure'' is a truth-value assignment that interprets the signature (the propositional symbols) of the formulae.  For a given truth-value assignment, the PLRE evaluates every formula in a set of formulae and identifies and reports those that are **NOT satisfied** --- i.e. that resolve to Boolean value FALSE.

The propositional logic formulae are expressed in text strings in **conjunctive normal form** [CNF](https://en.wikipedia.org/wiki/Conjunctive_normal_form). Such formulae can be supplied individually, as strings, or in sets via text file.

At instantiation, the PLRE consumes a propositional signature (i.e. a set of propositional symbols) and the name of a text file containing propositional logic formulae (in CNF) that use the signature. The PLRE assumes one formula per text file line. Each formula is parsed and represented as an executable computational graph.

Given a truth-value assignment, the PLRE computes the truth values of each of the propositional formulae and reports those that are **NOT satisfied** (i.e. that resolve to Boolean value FALSE).

The PLRE also provides ancillary services, like displaying the computational graph of a specified formula, before and after execution.

# Target use case

The target use case for the PLRE is as a symbolic reasoning component in neurosymbolic systems --- AI systems that blend symbolic reasoning with deep (subsymbolic) learning.

In particular, the PLRE is suitable for evaluating whether or not predictions of neural networks conform to (satisfy) logical requirements or constraints, such as the propositional logic requirements accompanying the annotated images in the ROAD-R dataset, per
> Giunchiglia et al., (2023). ROAD-R: The Autonomous Driving Dataset with Logical Requirements. *Machine Learning, 112*. https://doi.org/10.1007/s10994-023-06322-z


# Syntax for logical operators

The PLRE uses text-friendly symbols for logical operators to make it easy and intuitive to express propositional formulae, in CNF, in text files.

logical operator | conventional symbol | PLRE symbol 
--- | --- | --- | 
logical NOT | $\lnot$ | ! (exclamation mark)
logical OR  | $\lor$  | \| (vertical bar)
logical AND | $\land$ | & (ampersand)

Note: CNF does not permit shortcut propositional logical operators IMPLICATION ($\rightarrow$) or EQUIVALENCE ($\leftrightarrow$).


# Conjunctive normal form (CNF)

Per [Wikipedia](https://en.wikipedia.org/wiki/Conjunctive_normal_form), a CNF formula is a **conjunction** of one or more **clauses**, where each **clause** is a **disjunction** of one or more **literals**, and where a **literal** is a propositional symbol that may or may not be **negated**. Every propositional logic formula can be expressed in CNF. 

Consider this set of propositional symbols: `{A, B, C, D, E, F, G, H}`

**Example formulae for these symbols in CNF with a single clause**

`A`

`!A`

`A | B | !C`

**Example formulae for these symbols in CNF with multiple clauses**

`A & B & !C`

`(A | B) & (C | !D)`

`(A | B | !C) & (!D | E | F) & (G | !H)`

# Example

Suppose the set of propositional symbols: `{A, B, C, D, E}`.

Suppose the propositional logic formulae
1. `A | B | !C`
2. `(A | B) & (C | !D)`
3. `(A | B) & (C | !D) & E`

Suppose the following truth-value assignment (or possible world):
* symbols assigned True: $\{A, C\}$
* symbols assigned False: all others

Given this truth-value assignment, the truth values of the three example formula computed by the PLRE would be as follows:

id | formula | computed truth value
--- | --- | --- |
1 | `A \| B \| !C` | True
2 | `(A \| B) & (C \| !D)` | True
3 | `(A \| B) & (C \| !D) & E` | False

The PLRE would report formula 3 as NOT being **satisfied** by the truth-value assignment (the possible world).


