# Token List
# EOF indicates the End-Of-File (aka end of input)
INTEGER, PLUS, EOF = "INTEGER","PLUS","EOF"

class Token(object):
    def __init__(self, type, value):
        # token type : tokenList[i]
        self.type = type
        # token value : [0-9] | + | None
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

    def error(self):
        raise Exception("Error parsing input")

    def getNextToken(self):
        # Lexical Analyzer
        # Breaks sentences into tokens.
        text = self.text

        # is self.pos past the last char in self.text?
        # if so, return EOF because there isn't much to parse
        if self.pos > (len(text) - 1):
            return(Token(EOF, None))

        # Get character at position self.pos
        currentChar = text[self.pos]

        # if character is a digit then
        # - convert it to an integer
        # - create INTEGER token
        # - increment self.pos
            # NOTE - index until !INTEGER
        if currentChar.isdigit():
            token = Token(INTEGER, int(currentChar))
            self.pos += 1
            return token
        # if character is a + then
        # - convert it to an integer
        # - create INTEGER token
        # - increment self.pos
        if currentChar == '+':
            token = Token(PLUS, currentChar)
            self.pos += 1
            return token

        self.error()

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
        self.tokenPop(PLUS)

        # we expect the current token to be a digit
        right = self.currentToken
        self.tokenPop(INTEGER)
        # after the above call the currentToken is set to EOF token

        result = left.value + right.value
        return result

def main():
    while True:
        try:
            text = input("calc>  ")
        except EOFError:
            break
        if not text:
            continue
        interpeter = Interpreter(text)
        result = interpeter.expr()
        print(result)

if __name__ == "__main__":
    main()