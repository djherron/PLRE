# Generated from CNF.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,50,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,0,3,0,20,8,0,1,1,1,1,1,1,3,1,25,8,1,1,2,1,2,
        1,2,1,2,3,2,31,8,2,1,3,1,3,1,4,1,4,1,5,1,5,5,5,39,8,5,10,5,12,5,
        42,9,5,1,6,4,6,45,8,6,11,6,12,6,46,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,
        9,5,11,6,13,7,1,0,4,2,0,33,33,126,126,2,0,65,90,97,122,4,0,48,57,
        65,90,95,95,97,122,3,0,9,10,13,13,32,32,54,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,
        1,19,1,0,0,0,3,24,1,0,0,0,5,30,1,0,0,0,7,32,1,0,0,0,9,34,1,0,0,0,
        11,36,1,0,0,0,13,44,1,0,0,0,15,20,5,38,0,0,16,17,5,65,0,0,17,18,
        5,78,0,0,18,20,5,68,0,0,19,15,1,0,0,0,19,16,1,0,0,0,20,2,1,0,0,0,
        21,25,5,124,0,0,22,23,5,79,0,0,23,25,5,82,0,0,24,21,1,0,0,0,24,22,
        1,0,0,0,25,4,1,0,0,0,26,31,7,0,0,0,27,28,5,78,0,0,28,29,5,79,0,0,
        29,31,5,84,0,0,30,26,1,0,0,0,30,27,1,0,0,0,31,6,1,0,0,0,32,33,5,
        40,0,0,33,8,1,0,0,0,34,35,5,41,0,0,35,10,1,0,0,0,36,40,7,1,0,0,37,
        39,7,2,0,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,
        0,41,12,1,0,0,0,42,40,1,0,0,0,43,45,7,3,0,0,44,43,1,0,0,0,45,46,
        1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,49,6,6,0,0,
        49,14,1,0,0,0,6,0,19,24,30,40,46,1,6,0,0
    ]

class CNFLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AND = 1
    OR = 2
    NOT = 3
    LPAREN = 4
    RPAREN = 5
    VARIABLE = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "AND", "OR", "NOT", "LPAREN", "RPAREN", "VARIABLE", "WS" ]

    ruleNames = [ "AND", "OR", "NOT", "LPAREN", "RPAREN", "VARIABLE", "WS" ]

    grammarFileName = "CNF.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


