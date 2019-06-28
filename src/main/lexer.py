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
    def __init__(self, symbolSeq):
        # Client input string
        self.__symbolSeq = symbolSeq if symbolSeq is not None else ""
        # Index in input string
        self.__pos = 0 # type:Int
        # Token Buffer
        self._buffer = ()

    @property
    def buffer(self):
        return(self._buffer)

    @property
    def symbolSeq(self):
        return(self.__symbolSeq)

    def error(self):
        raise Exception("Invalid Syntax")

    @property
    def __isFull(self):
        return(bool(len(self.__symbolSeq)))

    def __hasNextChar(self): # type:Bool
        # Checks if it's safe to look-ahead
        return(not (self.__pos > len(self.symbolSeq) - 1))

    def __getChar(self): # type:Char
        return(self.symbolSeq[self.__pos])

    def __nextChar(self):
        # Move the "pos" pointer
        self.__pos += 1

    def __pushToken(self, token):
        # Adds Token to the end of the Buffer
        self._buffer += (token,)

    # function(sequence)
    # : sequence {
    #   while char is type -> {
    #     char => term
    #     if hasNext : { nextChar } ; { EXIT }
    #   }
    # }
    def __formTerm(self):
        char = self.__getChar()
        term = ""
        while char.isdigit():
            term += char
            if self.__hasNextChar():
                self.__nextChar()
            else:
                break
        return(term)

    # function(sequence)
    # : buffer {
    #   while isFull -> {
    #     if Digit : { createTerm => buffer }
    #     if Op : { OP => buffer }
    #     if hasNext : { nextChar } ; { EXIT }
    #   }
    #   EOF => buffer
    # }
    def analyze(self):
        # Lexical Analyzer
        # Breaks sentences into tokens.
        while self.__isFull:
            current_char = self.__getChar()
            
            if current_char.isspace():
                pass
            elif current_char.isdigit():
                term = self.__formTerm()
                self.__pushToken(LITERAL.copy(term))
            elif current_char in "+-/*%":
                self.__pushToken(OP.copy(current_char))

            if self.__hasNextChar():
                self.__nextChar()
            else:
                break
        self.__pushToken(EOF)

    def __eq__(self, otherObj):
        if otherObj is None:
            return(False)
        return(self.symbolSeq == otherObj.symbolSeq)

    def __sizeof__(self):
        return(len(self.buffer))