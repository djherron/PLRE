# Generated from CNF.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,
        9,1,1,1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,0,
        0,4,0,2,4,6,0,0,39,0,8,1,0,0,0,2,30,1,0,0,0,4,35,1,0,0,0,6,37,1,
        0,0,0,8,13,3,2,1,0,9,10,5,1,0,0,10,12,3,2,1,0,11,9,1,0,0,0,12,15,
        1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,
        16,17,5,0,0,1,17,1,1,0,0,0,18,19,5,4,0,0,19,24,3,4,2,0,20,21,5,2,
        0,0,21,23,3,4,2,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,
        1,0,0,0,25,27,1,0,0,0,26,24,1,0,0,0,27,28,5,5,0,0,28,31,1,0,0,0,
        29,31,3,4,2,0,30,18,1,0,0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,5,3,
        0,0,33,36,3,6,3,0,34,36,3,6,3,0,35,32,1,0,0,0,35,34,1,0,0,0,36,5,
        1,0,0,0,37,38,5,6,0,0,38,7,1,0,0,0,4,13,24,30,35
    ]

class CNFParser ( Parser ):

    grammarFileName = "CNF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "NOT", "LPAREN", "RPAREN", 
                      "VARIABLE", "WS" ]

    RULE_cnf = 0
    RULE_clause = 1
    RULE_literal = 2
    RULE_atom = 3

    ruleNames =  [ "cnf", "clause", "literal", "atom" ]

    EOF = Token.EOF
    AND=1
    OR=2
    NOT=3
    LPAREN=4
    RPAREN=5
    VARIABLE=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CnfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CNFParser.ClauseContext)
            else:
                return self.getTypedRuleContext(CNFParser.ClauseContext,i)


        def EOF(self):
            return self.getToken(CNFParser.EOF, 0)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CNFParser.AND)
            else:
                return self.getToken(CNFParser.AND, i)

        def getRuleIndex(self):
            return CNFParser.RULE_cnf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCnf" ):
                listener.enterCnf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCnf" ):
                listener.exitCnf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCnf" ):
                return visitor.visitCnf(self)
            else:
                return visitor.visitChildren(self)




    def cnf(self):

        localctx = CNFParser.CnfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_cnf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.clause()
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 9
                self.match(CNFParser.AND)
                self.state = 10
                self.clause()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(CNFParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CNFParser.LPAREN, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CNFParser.LiteralContext)
            else:
                return self.getTypedRuleContext(CNFParser.LiteralContext,i)


        def RPAREN(self):
            return self.getToken(CNFParser.RPAREN, 0)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(CNFParser.OR)
            else:
                return self.getToken(CNFParser.OR, i)

        def getRuleIndex(self):
            return CNFParser.RULE_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClause" ):
                listener.enterClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClause" ):
                listener.exitClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClause" ):
                return visitor.visitClause(self)
            else:
                return visitor.visitChildren(self)




    def clause(self):

        localctx = CNFParser.ClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_clause)
        self._la = 0 # Token type
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(CNFParser.LPAREN)
                self.state = 19
                self.literal()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 20
                    self.match(CNFParser.OR)
                    self.state = 21
                    self.literal()
                    self.state = 26
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 27
                self.match(CNFParser.RPAREN)
                pass
            elif token in [3, 6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(CNFParser.NOT, 0)

        def atom(self):
            return self.getTypedRuleContext(CNFParser.AtomContext,0)


        def getRuleIndex(self):
            return CNFParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CNFParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(CNFParser.NOT)
                self.state = 33
                self.atom()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(CNFParser.VARIABLE, 0)

        def getRuleIndex(self):
            return CNFParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = CNFParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(CNFParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





