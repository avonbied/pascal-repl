# -*- coding: utf-8 -*-
"""Token Class

This class contains information for token patterns.  Instances
  will have a type and value.  The value property is a sequence
  of related characters.  This relation is defined elsewhere.

Input: "<type>", "<value>"
Output: {type:<str>, value:<str>}
"""
class Token(object):
    def __init__(self, type, value):
        # token type : tokenTypes[n] ie PLUS, MINUS, etc.
        self._type = type
        # token value : [0-9] | + | - | None
        self._value = value

    @property    
    def value(self):
        return(self._value)
    
    @property
    def type(self):
        return(self._type)

    def copy(self, value):
        if value is None:
            result = Token(self.type, self._value)
            return(result)
        else:
            result = Token(self.type, value)
            return(result)

    def __eq__(self, otherObj):
        if otherObj is None:
            return(False)
        return(self.type == otherObj.type and self.value == otherObj.value)

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