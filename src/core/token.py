# -*- coding: utf-8 -*-
"""Token Class

This class contains information for token patterns.  Instances
  will have a type and value.  The value property is a sequence
  of related characters.  This relation is defined elsewhere.

Input: "<type>", "<value>"
Output: {type:<str>, value:<str>}
"""
from .errorSender import ErrorSender as ErrorSender

class Token(Sender):
    def __init__(self, type, value, log):
        # token type : tokenTypes[n] ie PLUS, MINUS, etc.
        self.__type = type if type is not None else ""
        # token value : [0-9] | + | - | None
        self.__value = value if value is not None else ""

        # Debug log reference
        self.__log = log

    @property
    def value(self):
        return(self.__value)

    @property
    def type(self):
        return(self.__type)

    def __error(self, msg, info):
        self.__log.log(("Token", msg, info))

    def copy(self, value):
        if value is None:
            result = Token(self.type, self.value)
            return(result)
        result = Token(self.type, value)
        return(result)

    def __eq__(self, otherObj):
        if otherObj is None:
            return(False)
        try:
            return(self.type == otherObj.type and self.value == otherObj.value)
        except:
            self.__error("Types can't be compared", {"value1":self, "value2":otherObj})

    def __str__(self):
        # String form of Object
        # Examples:
        #   Token(LITERAL, 2)
        #   Token(OPERATOR, '+')
        return("Token({type}, {value})".format(
            type=self.type,
            value=self.value
        ))

    def __repr__(self):
        return(self.__str__())