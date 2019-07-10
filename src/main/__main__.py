# Imports the Interpreter logic
from .interpreter import Interpreter as Interpreter
from .lexer import Lexer as Lexer
from .logger import Logger as Logger

def main():
    while True:
        try:
            text = input("calc>  ")
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        lexer.analyze()
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)

if __name__ == "__main__":
    main()