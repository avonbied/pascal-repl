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
ID = Token("IDENTIFIER", "0")
#NOTE: STR implementation isn't correct. Should start at '"' char but doesn't. Is more like IDENTIFIER

class Lexer(object):
    def __init__(self, symbolSeq):
        # Client input string
        self.__symbolSeq = symbolSeq if symbolSeq is not None else ""
        # Index in input string
        self.__pos = 0 # type:Int
        # Token Buffer
        self.__buffer = ()
        # Auto Analyzed
        self.analyze()

    @property
    def buffer(self):
        return(self.__buffer)

    @property
    def symbolSeq(self):
        return(self.__symbolSeq)

    def error(self):
        raise Exception("Invalid Syntax")

    def __isFull(self):
        return(len(self.__symbolSeq) > 0)

    @property
    def current_char(self): # type:Char
        try:
            return(self.symbolSeq[0])
        except:
            print("FAILED: current_char")

    def _peekChar(self): # type:Char
        if self.__pos+1 > len(self.__symbolSeq):
            return(self.symbolSeq[self.__pos+1])
        self.error()

    def _pushToken(self, token):
        # Adds Token to the end of the Buffer
        self.__buffer += (token,)

    # function(sequence)
    # : sequence {
    #   char => term
    #   while nextChar is type -> {
    #     nextChar => term
    #     if hasNext : { NEXT } ; { EXIT }
    #   }
    # }
    def __formTerm(self, seq):
        term, pos = "", 0
        if seq[0].isdigit():
            while seq[0].isdigit():
                term += seq[0]
                pos += 1
                seq = seq[1:]
                if not len(seq) > 0:
                    break
        else:
            while seq[0].isalnum():
                term += seq[0]
                pos += 1
                seq = seq[1:]
                if not len(seq) > 0:
                    break
        return(term, pos)

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
        seq = self.__symbolSeq
        while len(seq) > 0:
            if not len(seq) > 0:
                break
            if seq[0].isdigit():
                (term, pos) = self.__formTerm(seq)
                self._pushToken(LITERAL.copy(term))
                seq = seq[pos:]
                continue
            elif seq[0].isalpha():
                (term, pos) = self.__formTerm(seq)
                self._pushToken(ID.copy(term))
                seq = seq[pos:]
                continue
            elif seq[0] in "+-/*%":
                self._pushToken(OP.copy(seq[0]))
                seq = seq[1:]
            else:
                seq = seq[1:]
        self._pushToken(EOF)

    def __eq__(self, otherObj):
        if otherObj is None:
            return(False)
        return(self.buffer == otherObj.buffer)

    def __sizeof__(self):
        return(len(self.buffer))