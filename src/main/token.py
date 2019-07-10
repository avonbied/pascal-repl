# -*- coding: utf-8 -*-
"""Token Class

This class contains information for token patterns.  Instances
  will have a type and value.  The value property is a sequence
  of related characters.  This relation is defined elsewhere.

Input: "<type>", "<value>"
Output: {type:<str>, value:<str>}
"""
class Token(object):
    def __init__(self, type: str, value: str):
        # token type : tokenTypes[n] ie PLUS, MINUS, etc.
        self.__type = type if type is not None else ""
        # token value : [0-9] | + | - | None
        self.__value = value if value is not None else ""

    @property
    def type(self) -> str:
        return(self.__type)

    @property
    def value(self) -> str:
        return(self.__value)

    # str -> Token
    def copy(self, value: str) -> object:
        if value is None:
            result = Token(self.type, self.value)
            return(result)
        result = Token(self.type, value)
        return(result)

    def __eq__(self, otherObj: object) -> bool:
        if otherObj is None:
            return(False)
        return(self.type == otherObj.type and self.value == otherObj.value)

    def __str__(self) -> str:
        # Examples:
        #   Token(LITERAL, 2)
        #   Token(OPERATOR, '+')
        return("Token({type}, {value})".format(
            type=self.type,
            value=self.value
        ))

    def __repr__(self) -> str:
        return(self.__str__())