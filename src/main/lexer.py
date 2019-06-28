# -*- coding: utf-8 -*-
"""Lexer Class

This class is a wrapper for the lexical analysis process
  of the *Interpreter*.  It essentially converts a stream
  of characters into a tuple of <Tokens>.  The end of the
  sequence will be denoted by an `EOF` token.

Input: "[<char>[, <char>]*]"
Output: ([<Token>, ]*<Token:EOF>)
"""
from .token import Token as Token

## TOKEN LIST ##
# EOF indicates the End-Of-File (aka end of input)
EOF = Token("EOF", None)
# OPERATORS supported : (PLUS, NEG, MULT, DIV, MOD)
OP = Token("OPERATOR", '+')
# LITERALS supported : (INT, STR)
LITERAL = Token("LITERAL", "0")
#NOTE: STR implementation isn't correct. Should start at '"' char but doesn't. Is more like IDENTIFIER

class Lexer(object):
    def __init__(self, textStream):
        # Client input string
        self._text = textStream
        # Index in input string
        self._pos = 0 # type:Int
        # Token Buffer
        self._buffer = ()

    def error(self):
        raise Exception("Invalid Syntax")

    def _getChar(self): # type:Char
        return(self._text[self._pos])

    def _nextChar(self):
        # Move the "pos" pointer and return <Char> at that position
        self._pos += 1
        if self._pos > len(self._text)-1:
            return(None)
        return(self._getChar())

    def _skipSpace(self):
        char = self._getChar()
        while char is not None and char.isspace():
            char = self._nextChar()

    def _formTerm(self):
        char = self._getChar()
        result = ""
        if char.isdigit():
            while char is not None and char.isdigit():
                result += char
                char = self._nextChar()
        else:
            while char is not None and char.isalnum():
                result += char
                char = self._nextChar()
        return(result)

    def _pushToken(self, token):
        while token != EOF:
            self._buffer += (token,)
        self._buffer += (token,)

    def analyze(self):
        # Current Char Data
        currentChar = self._getChar() # type:Char

        # Lexical Analyzer
        # Breaks sentences into tokens.
        while currentChar is not None:
            if currentChar.isspace():
                self._skipSpace()
            elif currentChar.isalnum():
                self._pushToken(LITERAL.copy(self._formTerm()))
                currentChar = self._getChar()
            elif currentChar in "+-/*%":
                self._pushToken(OP.copy(currentChar))
                currentChar = self._getChar()
            else:
                self.error()
        self._pushToken(EOF)

    @property
    def buffer(self):
        return(self._buffer)

    def __sizeof__(self):
        return(len(self._buffer))