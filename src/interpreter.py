from enum import Enum
from token import Token as Token
#from operation import Operation as Op

## TOKEN LIST ##
# Common Token List #
EOF = Token(("EOF", "EOF", None))
## OPERATORS
PLUS = Token(("OPERATOR", "PLUS", "+"))
NEG = Token(("OPERATOR", "NEG", "-"))
MULT = Token(("OPERATOR", "MULT", "*"))
DIV = Token(("OPERATOR", "DIV", "/"))
MOD = Token(("OPERATOR", "MOD", "%"))
## TERMS
INTEGER = Token(("TERM", "INTEGER", 0))
STRING = Token(("TERM", "STRING", ""))
# EOF indicates the End-Of-File (aka end of input)
# INTEGER[], OPERATOR[], CHAR[], EOF
# types = list(EOF, PLUS, NEG, MULT, DIV, MOD)

_T = ("EOF" "OPERATOR" "TERM")


class Interpreter(object):
    def __init__(self, text):
        # Client input string
        self.text = text
        # Index in input string
        self.pos = 0
        # Type of current token
        self.currentToken = EOF
        self.currentChar = self.text[self.pos]
        # Input Buffer
        self.buffer = ()

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
        return(int(result))

    def getNextToken(self):
        # Lexical Analyzer
        # Breaks sentences into tokens.
        while self.currentChar is not None:
            if self.currentChar.isspace():
                self.skipWhitespace()
                continue
            if self.currentChar.isdigit():
                return(INTEGER.copy(self.integer()))
            elif self.currentChar == '+':
                self.nextPos()
                return(PLUS)
            elif self.currentChar == '-':
                self.nextPos()
                return(NEG)

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
        return(EOF)

    def tokenPop(self, tokenType, matchFlag=0):
        # if the token is of the tokenType goto nextToken
        # else raise error
        if self.currentToken.match(tokenType, matchFlag):
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
        if op == PLUS:
            self.tokenPop(PLUS, 1)
        else:
            self.tokenPop(NEG, 1)

        # we expect the current token to be a digit
        right = self.currentToken

        self.tokenPop(INTEGER)
        # after the above call the currentToken is set to EOF token

        while self.currentToken != EOF:
            if self.currentToken.tokenType({"type":"OPERATOR"}, 0) and not left.tokenType({"type":"TERM"}):
                self.error()
            else:
                op = self.currentToken
        if op == PLUS:
            result = left.value + right.value
        else:
            result = left.value - right.value
        return result