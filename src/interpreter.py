# -*- coding: utf-8 -*-
"""Interpreter Class

This class is
"""
from enum import Enum
#from operation import Operation as Op
# INTEGER[], OPERATOR[], CHAR[], EOF

_T = ("EOF" "OPERATOR" "LITERAL")

class Interpreter(object):
    def __init__(self, lexer):
        # Token Sequence
        self.list = lexer.buffer
        # Index in Token sequence
        self.pos = 0
        # Type of current Token
        self.currentToken = None
        # Input Buffer
        self.buffer = ()

    def error(self):
        raise Exception("Error parsing input")

    def _getToken(self):
        return(self.list[self.pos])

    def _nextToken(self):
        self.pos += 1
        return(self._getToken())

    ##########################################################
    # Parser / Interpreter code                              #
    ##########################################################

    def tokenPop(self, tokenType):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        # if the token is of the tokenType goto nextToken
        # else raise error
        if self.currentToken.type == tokenType:
            self.currentToken = self._nextToken()
        else:
            self.error()

    def term(self):
        """Return an INTEGER token value."""
        token = self.currentToken
        self.tokenPop("LITERAL")
        return int(token.value)

    def expr(self):
        """Arithmetic expression parser / interpreter."""
        # expr -> INTEGER PLUS INTEGER
        # set current token to the first token taken from the input
        self.currentToken = self._nextToken()
        # set current token to the first token from input

        # Begin accumulation
        result = self.term()

        while self.currentToken.type == "OPERATOR":
            token = self.currentToken
            if token.value == '+':
                self.tokenPop("OPERATOR")
                result = result + self.term()
            elif token.value == '-':
                self.tokenPop("OPERATOR")
                result = result - self.term()
            elif token.value == '*':
                self.tokenPop("OPERATOR")
                result = result * self.term()
            elif token.value == '/':
                self.tokenPop("OPERATOR")
                result = result / self.term()

        # after the above call the currentToken is set to EOF token

        return result