#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import *
    a = argv[1]
    b = argv[3]
    operators = {"+": add(a, b), "-": sub(a, b), "*": mul(a, b), "/": div(a, b)}
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    if argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)




