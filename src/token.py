# -*- coding: utf-8 -*-
"""Token Class

This class contains information for 
"""
class Token(object):
    def __init__(self, type, value):
        # token type : tokenTypes[n] ie PLUS, MINUS, etc.
        self.type = type
        # token value : [0-9] | + | - | None
        self.value = value

    def __str__(self):
        # String form of Object
        # Examples:
        #   Token(LITERAL, 2)
        #   Token(OPERATOR, '+')
        return("Token({type}, {value})".format(
            type=self.type,
            value=repr(self.value)
        ))

    def __repr__(self):
        return(self.__str__())
    
    def __eq__(self, otherObj):
        return(self.type == otherObj.type and self.value == otherObj.value)

    def isType(self, typeObj):
        return(self.type == typeObj.type)

    def copy(self, value):
        result = Token(self.type, value)
        return(result)