# Token List
# EOF indicates the End-Of-File (aka end of input)
# INTEGER[], OPERATOR[], CHAR[], EOF
INTEGER, PLUS, MINUS, EOF = "INTEGER","PLUS","MINUS","EOF"

class Token(object):
    def __init__(self, type, value):
        # token type : tokenList[n]
        self.type = type
        # token value : [0-9] | + | - | None
        self.value = value

    def __str__(self):
        # String form of Object
        # Examples:
        #   Token(INTEGER, 2)
        #   Token(PLUS, '+')
        return("Token({type}, {value})".format(
            type=self.type,
            value=repr(self.value)
        ))

    def __repr__(self):
        return(self.__str__())

class Interpreter(object):
    def __init__(self, text):
        # Client input string
        self.text = text
        # Index in input string
        self.pos = 0
        # Type of current token
        self.currentToken = None
        self.currentChar = self.text[self.pos]

    def error(self):
        raise Exception("Error parsing input")

    def nextPos(self):
        # Move the "pos" pointer and set the "currentChar" variable
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.currentChar = None
        else:
            self.currentChar = self.text[self.pos]

    def skipWhitespace(self):
        while self.currentChar is not None and self.currentChar.isspace():
            self.nextPos()

    def integer(self):
        # Returns an (multidigit) integer from input
        result = ""
        while self.currentChar is not None and self.currentChar.isdigit():
            result += self.currentChar
            self.nextPos()
        return int(result)

    def getNextToken(self):
        # Lexical Analyzer
        # Breaks sentences into tokens.
        while self.currentChar is not None:
            if self.currentChar.isspace():
                self.skipWhitespace()
                continue
            if self.currentChar.isdigit():
                return(Token(INTEGER, self.integer()))
            elif self.currentChar == '+':
                self.nextPos()
                return(Token(PLUS, '+'))
            elif self.currentChar == '-':
                self.nextPos()
                return(Token(MINUS, '-'))

        # text = self.text

        # # is self.pos past the last char in self.text?
        # # if so, return EOF because there isn't much to parse
        # if self.pos > (len(text) - 1):
        #     return(Token(EOF, None))

        # # Get character at position self.pos
        # currentChar = text[self.pos]

        # # if character is a digit then
        # # - convert it to an integer
        # # - create INTEGER token
        # # - increment self.pos
        #     # NOTE - index until !INTEGER
        # if currentChar.isdigit():
        #     token = Token(INTEGER, int(currentChar))
        #     self.pos += 1
        #     return token
        # # if character is a + then
        # # - convert it to an integer
        # # - create INTEGER token
        # # - increment self.pos
        # if currentChar == '+':
        #     token = Token(PLUS, currentChar)
        #     self.pos += 1
        #     return token

            self.error()
        return(Token(EOF, None))

    def tokenPop(self, tokenType):
        # if the token is of the tokenType goto nextToken
        # else raise error
        if self.currentToken.type == tokenType:
            self.currentToken = self.getNextToken()
        else:
            self.error()

    def expr(self):
        # expr -> INTEGER PLUS INTEGER

        # set current token to the first token from input
        self.currentToken = self.getNextToken()

        # we expect the current token to be a single digit
        left = self.currentToken
        self.tokenPop(INTEGER)

        # we expect the current token to be a '+'
        op = self.currentToken
        if op.type == PLUS:
            self.tokenPop(PLUS)
        else:
            self.tokenPop(MINUS)

        # we expect the current token to be a digit
        right = self.currentToken
        self.tokenPop(INTEGER)
        # after the above call the currentToken is set to EOF token

        if op.type == PLUS:
            result = left.value + right.value
        else:
            result = left.value - right.value
        return result