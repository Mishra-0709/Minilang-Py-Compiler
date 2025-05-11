# Entry point for the MiniLang interpreter.
import miniparser
#print(dir(miniparser))  # Debug: check what's inside

from miniparser import parser  # Import the parser

def main():
    print("MiniLang Interpreter")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            line = input(">>> ")
        except EOFError:
            break

        if line.strip() == 'exit':
            break

        if line:
            result = parser.parse(line)
            if result is not None:
                print(result)

if __name__ == "__main__":
    main()
