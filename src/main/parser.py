# -*- coding: utf-8 -*-
"""Parser Class

This class is a wrapper to validate the processed input
  from a *<Lexer> buffer*.  It checks whether the sequence
  of <Tokens> matches a valid pattern.  If it matches then
  a _Pass_ ParseFlag is outputted, otherwise a _Fail_
  ParseFlag is outputted.

Input: <Tuple[Token]>
Output: <ParseFlag>
"""
class Parser(object):
    def __init__(self, log: object):
        self.__list = ()
        self.check()

        # Debug log reference
        self.__log = log

    def check(self):
        pos = 0
        while self.__list[pos].type != "EOF":
            print(True)
            pos += 1
        print("Done")

    def __str__(self) -> str:
        return("")