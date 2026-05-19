# Generated from CNF.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CNFParser import CNFParser
else:
    from CNFParser import CNFParser

# This class defines a complete generic visitor for a parse tree produced by CNFParser.

class CNFVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CNFParser#cnf.
    def visitCnf(self, ctx:CNFParser.CnfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNFParser#clause.
    def visitClause(self, ctx:CNFParser.ClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNFParser#literal.
    def visitLiteral(self, ctx:CNFParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNFParser#atom.
    def visitAtom(self, ctx:CNFParser.AtomContext):
        return self.visitChildren(ctx)



del CNFParser