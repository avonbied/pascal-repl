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
template = {
    # EOF indicates the End-Of-File (aka end of input)
    "EOF": Token("EOF", None),
    # OPERATORS supported : (PLUS, NEG, MULT, DIV, MOD)
    "OP": Token("OPERATOR", '+'),
    # LITERALS supported : (INT, STR)
    "LIT": [Token("LIT_INT", "0"), Token("LIT_FLOAT", "0.0")],
    "ID": Token("IDENTIFIER", "")
}
#NOTE: STR implementation isn't correct. Should start at '"' char but doesn't. Is more like IDENTIFIER
class Lexer(object):
    def __init__(self, log: object):
        # Index in input string
        self.__pos = 0 # type:Int
        # Token Buffer
        self.__buffer = ()

        # Debug log reference
        self.__log = log

    # -> Tuple[Token]
    @property
    def buffer(self) -> tuple:
        return(self.__buffer)

    # raise Exception("Invalid Syntax")
    def __error(self, msg: str, info: str):
        self.__log.log(("Lexer", msg, info))

    # Token ->
    def __pushToken(self, token: object):
        # Adds Token to the end of the Buffer
        self.__buffer += (token,)

    def __clearBuffer(self):
        self.__buffer = ()

    def __formNumeric(self, seq: str) -> str:
        pass

    def __formString(self, seq:str) -> str:
        pass

    def __formId(self, seq:str) -> str:
        pass

    # function(sequence)
    # : sequence {
    #   char => term
    #   while nextChar is type -> {
    #     nextChar => term
    #     if hasNext : { NEXT } ; { EXIT }
    #   }
    # }
    # str -> Tuple(str, int)
    def __formTerm(self, seq: str) -> tuple:
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
    def analyze(self, symbolSeq: str):
        # Lexical Analyzer
        # Breaks sentences into tokens.
        # Client input string
        seq = symbolSeq if symbolSeq is not None else ""
        while len(seq) > 0:
            if not len(seq) > 0:
                break
            if seq[0].isdigit():
                (term, pos) = self.__formTerm(seq)
                self.__pushToken(template["Lit"][0].copy(term))
                seq = seq[pos:]
                continue
            elif seq[0].isalpha():
                (term, pos) = self.__formTerm(seq)
                self.__pushToken(ID.copy(term))
                seq = seq[pos:]
                continue
            elif seq[0] in "+-/*%":
                self.__pushToken(template["OP"].copy(seq[0]))
                seq = seq[1:]
            else:
                seq = seq[1:]
        self._pushToken(template["EOF"])

    def __eq__(self, otherObj: object) -> bool:
        if otherObj is None:
            return(False)
        try:
            return(self.buffer == otherObj.buffer)
        else:
            self.__error("Types can't be compared", {"value1":self, "value2":otherObj})

    def __len__(self) -> int:
        return(len(self.buffer))