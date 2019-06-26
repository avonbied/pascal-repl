class Token(object):
    def __init__(self, tupleProps):
        # token type : tokenTypes[n]
        self.type = tupleProps[0]
        # token name : PLUS, MINUS, etc.
        self.name = tupleProps[1]
        # token value : [0-9] | + | - | None
        self.value = tupleProps[2]

    def __str__(self):
        # String form of Object
        # Examples:
        #   Token(TERM, INTEGER, 2)
        #   Token(OPERATOR, PLUS, '+')
        return("Token({type}, {name}, {value})".format(
            type=self.type,
            name=self.name,
            value=repr(self.value)
        ))

    def __repr__(self):
        return(self.__str__())
    
    def __eq__(self, otherObj):
        return(self.type == otherObj.type and self.name == otherObj.name and self.value == otherObj.value)

    def match(self, typeObj, matchFlag):
        result = True
        if matchFlag > 0:
            if matchFlag > 1:
                result = result and (self.value == typeObj.value)
            result = result and (self.name == typeObj.name)
        result = result and (self.type == typeObj.type)
        return(result)

    def copy(self, value):
        result = Token((self.type, self.name, value))
        return(result)