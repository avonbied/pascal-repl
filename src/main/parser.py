# -*- coding: utf-8 -*-
"""Parser Class

This class is a wrapper to validate the processed input
  from a *<Lexer> buffer*.  It checks whether the sequence
  of <Tokens> matches a valid pattern.  If it matches then
  a _Pass_ ParseFlag is outputted, otherwise a _Fail_
  ParseFlag is outputted.

Input: <Lexer>
Output: <ParseFlag>
"""
class Parser(object):
    def __init__(self, buffer):
        self.__list = buffer
        self.check()

    def check(self):
        pos = 0
        while self.__list[pos].type != "EOF":
            print(True)
            pos += 1
        print("Done")