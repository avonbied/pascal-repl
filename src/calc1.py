# Imports the Interpreter logic
from interpreter import Interpreter as Interpreter

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