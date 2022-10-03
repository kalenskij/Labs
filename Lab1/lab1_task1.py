import argparse


parser = argparse.ArgumentParser(description="Parse a line")
parser.add_argument("Number1", type=int, nargs="?")
parser.add_argument("Operator", type=str, nargs="?")
parser.add_argument("Number2", type=int, nargs="?")
args = parser.parse_args()
try:
    print(eval(str(args.Number1) + args.Operator + str(args.Number2)))
except ZeroDivisionError:
    print("Division by zero")
except SyntaxError:
    print("Syntax Error (Probably wrong operator)")
except TypeError:
    print("Type error (some arguments maybe missing)")
