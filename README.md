# PLRE (Propositional Logic Reasoning Engine)

The PLRE (propositional logic reasoning engine) is a pure Python propositional logic formula *model checker*.

Propositions expressed in conjunctive normal form (CNF) are evaluated to determine their truth values, given a propositional symbol truth-value assignment.

**Table of Contents**
- [Overview](#overview)
- [Related work](#related-work)
  - [Automated reasoning](#automated-reasoning)
  - [Decision problems and procedures](#decision-problems-and-decision-procedures)
  - [Computational logic](#computational-logic)
- [Target use case](#target-use-case)
- [Logical operator symbols](#logical-operator-symbols)
- [Conjunctive normal form (CNF)](#conjunctive-normal-form-cnf)
- [PLRE example](#plre-example)
- [Version history](#version-history)
- [Installation](#installation)



## Overview

The PLRE (propositional logic reasoning engine) is a Python tool for determining the Boolean truth values of propositional logic formulae expressed in [conjunctive normal form](https://en.wikipedia.org/wiki/Conjunctive_normal_form) (CNF), given a truth-value assignment (an assignment of truth values to the atomic propositional symbols referenced in the CNF expressions).

The PLRE is a *model checker*: it checks whether or not a certain truth-value assignment satisfies (i.e. is a model of) a given CNF expression (propositional logic formula).


## Related work

### Automated reasoning

The PLRE contributes to the field of **automated reasoning**, in particular to the **model checking** dimension of its subfield **automated theorem proving**. Per Wikipedia, [model checking](https://en.wikipedia.org/wiki/Model_checking) problems are formulated as logic tasks that involve checking ``whether a structure satisfies a given logical formula''. The article then gives this example:
> **A simple model-checking problem consists of verifying whether a formula in the propositional logic is satisfied by a given structure.**

This is precisely what the PLRE does. So the PLRE can also be described as being a **propositional model checker**.  

[Note on terminalogy. The term 'structure' is used in Model Theory, a subfield of mathematical logic, in place of 'interpretation'. This allows Model Theory to use the term 'interpretation' for a different purpose --- i.e. to permit discussion of the notion of 'interpretations' of 'structures'. In the case of propositional logic, the term 'structure' corresponds to a truth-value assignment that interprets the propositional symbols.]


### Decision problems and decision procedures

Per Wikipedia, a [decision problem](https://en.wikipedia.org/wiki/Decision_problem) is a computational problem that can be framed as a question with a binary answer, **{yes, no}** or **{True, False}**, on some set of inputs. For example, consider the question: "given two numbers $x$ and $y$, does $x$ evenly divide $y$?". This is a decision problem. The **model checking** problem solved by the PLRE, of deciding whether a logical formula is **satisfied** by a structure (or interpretation, or propositional truth-value assignment) is also a **decision problem**.

Per the same Wikipedia article, a [decision procedure](https://en.wikipedia.org/wiki/Decision_problem) for a decision problem is an **algorithm** that can answer the question with respect to all inputs. For example, the algorithm of 'long division' is a **decision procedure** for the divisor decision problem just described. To perform the **model checking** task, the PLRE employs a strategy of representing a propositional logic formula as an executable computational graph, and then executing that graph, given a truth-value assignment. This PLRE **algorithm** for deciding whether a formula is **satisfied** or not is an example of a **decision procedure**.

### Computational logic

Per Wikipedia, [computational logic](https://en.wikipedia.org/wiki/Computational_logic) is basically alternate terminology for **automated reasoning** and **automated theorem proving**. It also has strong connections with **logic programming**.

The term **computational logic** was first used in 1970:
> Robinson et al., (1970).  Computational Logic - The Unification Computation. *Machine Intelligence 6*, 63-72, Edinburgh University Press, 1971.

In the 2nd paragraph of the paper, Robinson uses the term *computational logic*, and gives it a footnote explanation, saying:
> Surely a better phrase than 'theorem proving', for the branch of artificial intelligence which deals with how to make machines do deduction efficiently.

So Robinson defined **computational logic** broadly.

The journal [ACM Transactions on Computational Logic](https://dl.acm.org/journal/tocl) also defines the term *computational logic* broadly. The journal says it is 
> devoted to research concerned with **all uses of logic in computer science**. 

The PLRE fits these definitions of **computational logic**.


## Target use case

The target use case for the PLRE is as a symbolic reasoning component in neurosymbolic systems --- AI systems that blend symbolic reasoning with deep (subsymbolic) learning.

For example, the PLRE can be used to evaluate whether or not predictions of neural networks conform to (satisfy) logical requirements or constraints, such as the propositional logic requirements accompanying the annotated images in the ROAD-R dataset, per Giunchiglia et al., (2023).
> Giunchiglia et al., (2023). ROAD-R: The Autonomous Driving Dataset with Logical Requirements. *Machine Learning, 112*. https://doi.org/10.1007/s10994-023-06322-z


## Logical operator symbols

The ANTLR v4 grammar for CNF specifies that alternative symbols may be used for the logical operators, to make it easy to express propositional formulae, in CNF, in text files.

logical operator | conventional symbol | PLRE symbol 
--- | --- | --- | 
logical NOT | $\lnot$ | ~, !, NOT 
logical OR  | $\lor$  | \|, OR 
logical AND | $\land$ | &, AND

Note that CNF does not permit the shortcut propositional logic operators for IMPLICATION ($\rightarrow$) or EQUIVALENCE ($\leftrightarrow$).  Formulae that might contain such operators must be re-expressed using the three operators permitted by CNF.

## Conjunctive normal form (CNF)

Per [Wikipedia](https://en.wikipedia.org/wiki/Conjunctive_normal_form), a CNF formula is a **conjunction** of one or more **clauses**, where each **clause** is a **disjunction** of one or more **literals**, and where a **literal** is a propositional symbol that may or may not be **negated**. Every propositional logic formula can be expressed in CNF. 

The ANTLR v4 grammar for CNF used by the PLRE requires parentheses around CNF clauses, except in the degenerate case where a CNF clause consists of a single literal only.

### Example propositional logic formulae in CNF

Consider this set of propositional symbols: `{A, B, C, D, E, F, G, H}`

**formulae that consist of a single CNF clause**:

`A`

`!A`

`(A | B | !C)`

**formulae that are conjunctions of multiple CNF clauses**:

`A & (B | C) & !D`

`(A | B) & (C | !D)`

`(A | B | !C) & (!D | E | F) & (G | !H)`

## PLRE example

Suppose a set of propositional symbols: `{A, B, C, D, E}`.

Suppose some propositional logic formulae constructed using that set of symbols:
1. `A | B | !C`
2. `(A | B) & (C | !D)`
3. `(A | B) & (C | !D) & E`

Suppose a PLRE truth-value assignment:
* a list of symbol names assigned truth-value True; suppose $\{A, C\}$
* all symbols not in the list are assigned truth-value False; hence $\{B, D\}$

Given this truth-value assignment, the truth values of the three formulae computed by the PLRE would be as follows:

id | formula | computed truth value
--- | --- | --- |
1 | `A \| B \| !C` | True
2 | `(A \| B) & (C \| !D)` | True
3 | `(A \| B) & (C \| !D) & E` | False

The PLRE can report formula truth-values at the level of individual formulae (e.g. which formulae evaluated False ?), and in aggregate (e.g. the number of formulae that evaluated True ?).

## Version history

### Version 1.0.0

This GitHub repository contains the PLRE v1.0.0

The PLRE v1.0.0 uses a CNF parser generated by ANTLR v4 from an ANTLR v4 grammar for CNF generated by AI chatbot model Claude.ai.  Propositions expressed in CNF are converted into parse trees by a CNF parser generated by ANTLR v4 from the CNF grammar specified by Claude.ai.

The truth value of CNF expressions is evaluated, given a propositional symbol truth-value assignment, by visiting the nodes of its parse tree using a visitor class, per the visitor software design pattern. The visitor implements a depth-first, post-order traversal of the parse tree, which is guaranteed to be topological. The custom visitor class contains a method for processing each type of node encountered in a walk of a CNF parse tree, which permits application-specific logic to be implemented such as for logical operations (negation, disjunction, and conjunction).

### Version 0.5.0

The original version of the PLRE, v0.5.0, used a hand-coded CNF parser to convert CNF expressions into computational graphs. The nodes of the computational graph for a given CNF expression are stored in a list in topological order.

To evaluate a CNF expression, its computational graph is *executed* by walking the graph's list of nodes in sequential order and evaluating each node as it is encountered.

PLRE v0.5.0 is not available in this GitHub repository.



## Installation

You can install the PLRE package (i.e. the `plre` directory) using `pip` by doing the following:

1. download the PLRE GitHub repository

2. open a Terminal session

3. move into the root directory of the PLRE project, where the `pyproject.toml` file lives
* `$ cd <PLRE-root-dir>`

4. install the PLRE package
* `$ pip install .`

`pip` reads the `pyproject.toml` file which instructs it to invoke `setuptools` to generate a `.whl` file containing the `plre` directory only.

`pip` then installs the `.whl` file in the active Python environment under the package name `plre`.

You can now `import plre`. 


